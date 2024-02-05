from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QGraphicsView,
                                QGraphicsScene,
                                QGraphicsObject,
                                QTextEdit,
                                QMenu,
                                QWidgetAction,
                                QWidget,
                                QLabel, 
                                QStyleFactory,
                                QColorDialog,
                                QFileDialog,
                                QDialog)
from PySide6.QtGui import (QPageSize,
                                               QGradient,
                                               QBrush,
                                               QTextCharFormat,
                                               QTextCursor,
                           QColor,
                           QPalette,
                           QPixmap,
                           QAction,
                           QIcon,
                           qRgba,
                           QImage,
                           QPyTextObject,
                           QTextFormat,
                           QTransform)

from PySide6.QtCore import Qt , QRectF, QPointF,QPoint, Signal, QEvent, QSize, QSizeF, QMimeData, QDataStream, QByteArray, QIODevice
from mainWindow import Ui_MainWindow
from textColorWidget import Ui_TextColorWidget
from backgroundColorWidget import Ui_BackgroundColorWidget
from imageSizeChangeDialog import Ui_ImageSizeChangeDialog

import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize = g_pageSizeF.toSize()

KeepAnchor = QTextCursor.KeepAnchor
PreviousCharacter = QTextCursor.PreviousCharacter
NextCharacter = QTextCursor.NextCharacter
FontPropertiesSpecifiedOnly = QTextCharFormat.FontPropertiesSpecifiedOnly

AlignSuperScript = QTextCharFormat.AlignSuperScript
AlignNormal = QTextCharFormat.AlignNormal
AlignSubScript = QTextCharFormat.AlignSubScript

ImageProperty = 1
ImageObject = QTextFormat.UserObject

import uuid

class ImageLabel(QLabel):

    ImageObject = QTextFormat.UserObject
    ImageProperty = QTextFormat.UserProperty

    def __init__(self, autoFillBackground,
                 pixmap, size, visible, styleSheet, parent):
        super().__init__(parent)

        self.setAutoFillBackground(autoFillBackground)
        self.setPixmap(pixmap)
        self.setVisible(visible)
        self.setStyleSheet(styleSheet)
        self._doubleBuffer = pixmap
        self.setObjectName(str(uuid.uuid4()))

    def mousePressEvent(self, event):

        self.parent().customObjectPointer = self
        self.imageHandler.setRect(self.geometry())
        for child in self.imageHandler.childItems():
            child.setCenter()
            child.setVisible(True)
            child.setCustomObject(self)
        self.imageHandler.setCustomObject(self)
        self.imageHandler.setVisible(True)
        super().mousePressEvent(event)


    def save(self, out):
        out.writeBool(self.autoFillBackground())
        out.writeQString(self.styleSheet())
        out.writeQString(self.objectName())
        out << self.size()
        out << self.pixmap()
        out << self._doubleBuffer

    def load(self, out):
        self.setAutoFillBackground(out.readBool())
        self.setStyleSheet(out.readQString())
        self.setObjectName(out.readQString())
        size = QSize()
        out >> size
        pixmap = QPixmap()
        out >> pixmap
        self.resize(size)
        self.setPixmap(pixmap)
        pixmap = QPixmap()
        out >> pixmap
        self._doubleBuffer = pixmap

class ImageSizeChangeDialog(QDialog, Ui_ImageSizeChangeDialog):#new↓

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.checkBox.toggled.connect(self.block)

    def block(self, bool):

    
        self.hSpinBox.blockSignals(not bool)
        self.vSpinBox.blockSignals(not bool)

class WidgetAction(QWidgetAction):

    colorLabelPress = Signal(QLabel)
    colorLabelPressWithPixmap = Signal(
        QLabel, QPixmap
        )
    backgroundColorLabelPress = Signal(QLabel)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setDefaultWidget(TextColorWidget())

    def createWidget(self, widget):

        if (
            widget.objectName() ==
            "textColorMenu"
            ):
            self.w = self.defaultWidget()
            self.w.setParent(widget)
        elif (
            widget.objectName() ==
            "backgroundColorMenu"):
            self.w = BackgroundColorWidget(
                widget
                )

        for child in self.w.children():
                child.installEventFilter(self)

        return self.w
        

    def eventFilter(self, obj, event):

      
        if (event.type() == QEvent.MouseButtonPress):
            p = obj.parent()
            objectName = p.objectName()
            if objectName == "TextColorWidget":
                self.colorLabelPress.emit(obj)
                pixmap = QPixmap(32, 32)
                pixmap.fill(
                    obj.palette().color(QPalette.Window))
                self.colorLabelPressWithPixmap.emit(obj, pixmap)

            elif objectName == "BackgroundColorWidget":
                self.backgroundColorLabelPress.emit(obj)
                    
        
        return super().eventFilter(obj, event)
    

class TextColorWidget(QWidget, Ui_TextColorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
class BackgroundColorWidget(QWidget, Ui_BackgroundColorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
class TextEdit(QTextEdit):

    MimeKey = "createMimeDataFromSelection"
    contentsChange = Signal(int, int, int)
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.imageObjectInterface = ImageObjectInterface()
        docLayout = self.document().documentLayout()
        docLayout.registerHandler(
            ImageObject, self.imageObjectInterface
            )

        self.contentsChange[int, int, int].connect(
            self.cleanChildWidgets
            )

        self.mimeData = None

        self.customObjectPointer = None
        self.document().setParent(self)#new
    
            
    def cut(self):

        tc = self.textCursor()
        self.mimeData = self.createMimeDataFromSelection()
        self.cleanRecursion(tc, tc.selectionStart(),
                            tc.selectionStart(),
                            len(tc.selectedText()),
                            0)
        tc.deleteChar()

    def paste(self):
        if self.mimeData:
            self.insertFromMimeData(
                self.mimeData
                )
            return
        super().paste()
        
    def cleanChildWidgets(self, fr, charsRemoved, charsAdded):

        if charsRemoved > 1:
            tc =self.document().find(chr(0xfffc), fr)
            if not tc.isNull():
                self.cleanRecursion(tc, 0, fr, charsRemoved, charsAdded)
                tc = self.textCursor()
                tc.deleteChar()
                self.contentsChange[int, int, int].connect(
                    self.cleanChildWidgets
                    )

    def keyPressEvent(self, event):

        isBack = event.key() == Qt.Key_Backspace
        isDelete = event.key() == Qt.Key_Delete

        if (event.key() == Qt.Key_X
            and
            event.modifiers() == Qt.ControlModifier):
            self.cut()
            return
        elif (event.key() == Qt.Key_V
              and
              event.modifiers() == Qt.ControlModifier):

            self.paste()
            return
        
        if isBack or isDelete:
            tc = self.textCursor()
            if not tc.hasSelection():
                if isBack:
                    charFormat = tc.charFormat()
                    tc.movePosition(
                        PreviousCharacter, KeepAnchor
                        )
                else:
                    
                    tc.movePosition(
                        NextCharacter, KeepAnchor
                        )
                    charFormat = tc.charFormat()
                if tc.selectedText() == chr(0xfffc):
                    label = charFormat.property(
                        ImageProperty)
                    label.setVisible(False)
                    label.setParent(None)
                    tc.deleteChar()
                    return
            else:
                self.contentsChange.emit(
                    tc.selectionStart(),
                    len(tc.selectedText()),
                    0)

        return super().keyPressEvent(event)
    
    def cleanRecursion(self, tc, selectionStart, fr, charsRemoved, charsAdded):

        tc = self.document().find(
            chr(0xfffc), selectionStart
            )
        if not tc.isNull():
            selectionStart = tc.selectionStart()
            selectionEnd = tc.selectionEnd()
            if (fr <= selectionStart <= fr + charsRemoved):
                char = tc.charFormat()
                label = char.property(ImageProperty)
                label.setVisible(False)
                label.setParent(None)
                self.cleanRecursion(tc, selectionEnd, fr, charsRemoved, charsAdded)
                

    def createMimeDataFromSelection(self):

        tc = self.textCursor()

        if chr(0xfffc) not in tc.selectedText():
            return super().createMimeDataFromSelection()

        else:
            absoluteStart = tc.selectionStart()
            searchStart = tc.selectionStart()
            searchEnd = tc.selectionEnd()
            mimeData = QMimeData()
            qb = QByteArray()
            ds = QDataStream(
                qb, QIODevice.WriteOnly
                )
            #writeQString
            ds.writeQString(
                tc.selection().toHtml())
            
            start = tc.selectionStart()

            while True:
                tc = self.document().find(
                    chr(0xfffc), searchStart
                    )

                if not tc.isNull():
                    #writeUInt64
                    ds.writeUInt64(
                        tc.selectionStart() - absoluteStart
                        )
                    charFormat = tc.charFormat()
                    #writeUInt16
                    ds.writeUInt16(charFormat.objectType())
                    label = charFormat.property(ImageProperty)
                    #ImageLabel
                    label.save(ds)
                    
                    searchStart = tc.selectionEnd()
                    if searchStart >= searchEnd:
                        break
                else:

                    break

                mimeData.setData(
                    TextEdit.MimeKey, qb
                    )
                return mimeData
        
    def insertFromMimeData(self, mimeData):

        tc = self.textCursor()
        pos = tc.position()

        if mimeData.hasFormat(TextEdit.MimeKey):
            qb = mimeData.data(TextEdit.MimeKey)
            ds = QDataStream(qb, QIODevice.ReadOnly)
            tc.setKeepPositionOnInsert(True)
            #readQString
            tc.insertHtml(ds.readQString())
            tc.setKeepPositionOnInsert(False)
            while not ds.atEnd():
                #readUInt64
                rs = ds.readUInt64()
                tc.setPosition(pos + rs)
                #readUInt16
                ot = ds.readUInt16()
                
                label = ImageLabel(False, QPixmap(),
                                   QSize(32, 32), True, "", self)
                #ImageLabel
                label.load(ds)
                char = tc.charFormat()
                char.setObjectType(ot)
                char.setProperty(ImageProperty, label)
                tc.insertText(chr(0xfffc), char)
                tc.setPosition(pos)

            return

        super().insertFromMimeData(mimeData)
        
    def loadImage(self):

        f, _ = QFileDialog.getOpenFileName(
            None,
            self.tr("Open Image"),
            "/home/",
            self.tr(
                "Image Files (*.png *.jpg *.bmp)")
            )
        if f:
            i = QImage(f)
            tc = self.textCursor()
            p = QPixmap(i)
            label = ImageLabel(autoFillBackground=False,
                                       pixmap= p,
                           size = i.size(),
                           visible = True,
                           styleSheet="QLabel{background-color: white}",
                           parent = self)
            label.imageHandler = self.imageHandler
            char = tc.charFormat()
            char.setObjectType(ImageObject)
            char.setProperty(ImageProperty, label)
            tc.insertText(chr(0xfffc), char)

    def changeImage(self):

        if self.customObjectPointer is None:

            QMessageBox.warning(None,
                                "画像が選択されていません",
                                "画像を選択して下さい。")
            return
        f, _ = QFileDialog.getOpenFileName(None,
            self.tr("Open Image"),
            "/home/",
            self.tr(
                "Image Files (*.png *.jpg *.bmp)")
            )
        if f:
            i = QImage(f)
            tc = self.textCursor()
            p = QPixmap(i)
            label = self.customObjectPointer
            if label:
                
                label.setPixmap(p)
                label._doubleBuffer = QPixmap(p)
                label.resize(p.size())
    
    def changeImageSize(self):#new↓

        if self.customObjectPointer is None:

            QMessageBox.warning(None,
                                "画像が選択されていません",
                                "画像を選択して下さい。")
            return
        
        d = ImageSizeChangeDialog()
        if d.exec() == QDialog.Accepted:
            
            h, v = d.hSpinBox.value()/100, d.vSpinBox.value()/100
            aspectRatio = d.checkBox.isChecked()
            isKeep = d.checkBox.isChecked()
            aspectRatio = Qt.KeepAspectRatio if isKeep else Qt.IgnoreAspectRatio
            label = self.customObjectPointer
            p = label.pixmap()
##            p = p.scaled(
##                h*p.size().width(), v*p.size().height(),
##                aspectRatio,
##                Qt.TransformationMode.SmoothTransformation)
##            
##            dp = label._doubleBuffer.scaled(p.size().width(), p.size().height(),
##                    aspectRatio,
##                    Qt.TransformationMode.SmoothTransformation)
            transform = QTransform()
            transform.scale(h, v)
        
            dp = label._doubleBuffer.transformed(transform)
            label.setPixmap(dp)
            label.resize(dp.size())
            self.document().parent().setFocus()

            tc = self.document().parent().textCursor()
            tc.insertText(" ")
            tc.deleteChar()
            
    def clearBackground(self):
        tc = self.textCursor()        
        charFormat = tc.charFormat()
        charFormat.clearBackground()        
        tc.setCharFormat(charFormat)

    def setHighlightByAction(self, label):
        pal = label.palette()
        color = pal.color(QPalette.Window)
        self.setTextBackgroundColor(color)
        

    def setTextColorByAction(self, label):
        pal = label.palette()
        color = pal.color(QPalette.Window)
        self.setTextColor(color)

    def setBold(self, bool):

        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontWeight(
            QFont.Bold if bool else QFont.Normal
            )
        tc.setCharFormat(charFormat)

    def setItalic(self, bool):

        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontItalic(bool)
        tc.setCharFormat(charFormat)

    def setStrikeOut(self, bool):
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontStrikeOut(bool)
        tc.setCharFormat(charFormat)

    def setUnderline(self, bool):
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontUnderline(bool)
        tc.setCharFormat(charFormat)

    def setSuperScript(self, bool):
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setVerticalAlignment(
            AlignSuperScript if bool else NormalScript
         )
            
        tc.setCharFormat(charFormat)

    def setSubScript(self, bool):
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setVerticalAlignment(
            AlignSubScript if bool else NormalScript
            )
        tc.setCharFormat(charFormat)
        
    def setCurrentFont(self, font):

        tc = self.textCursor()
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFormat.setFont(
                    font,
                    FontPropertiesSpecifiedOnly
                    )
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
        else:

            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFont(font)
            tc.setCharFormat(charFormat)
            self.setTextCursor(tc)

    def crementPointSize(self): 
        tc = self.textCursor()
        s = self.sender()
        
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                if s.objectName() == "fontUpperToolButton":
                    
                    charFont.setPointSize(
                        charFont.pointSize() + 1
                        )
                else:
                    charFont.setPointSize(
                        charFont.pointSize() - 1
                        )
                charFormat.setFont(charFont)
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
        
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        g = self.findChild(QGraphicsView, "mainView")
        mainScene  = QGraphicsScene()
        self.mainScene = mainScene
        b = QBrush(QGradient.Preset.SaltMountain)
        mainScene.setBackgroundBrush(b)
        self.mainView.setScene(mainScene)
        t = TextEdit()
        mainScene.addWidget(t)
        t.resize(g_pageSize)
        self.fontComboBox.currentFontChanged.connect(t.setCurrentFont)
        self.fontPointSizeComboBox.currentTextChanged.connect(
            lambda i: t.setFontPointSize(float(i))
            )
        self.fontUpperToolButton.clicked.connect(t.crementPointSize)
        self.fontDownerToolButton.clicked.connect(t.crementPointSize)
        self.boldToolButton.clicked.connect(t.setBold)
        self.italicToolButton.clicked.connect(t.setItalic)
        self.strikeOutToolButton.clicked.connect(t.setStrikeOut)
        self.superScriptToolButton.clicked.connect(t.setSuperScript)
        self.subScriptToolButton.clicked.connect(t.setSubScript)

        pal = self.textColorToolButton.palette()
        pal.setColor(QPalette.ButtonText, QColor(0, 0, 0))
        self.textColorToolButton.setPalette(pal)

        pal = self.backgroundColorToolButton.palette()
        pal.setColor(
            QPalette.Button, QColor(255, 255, 255)
                     )
        self.backgroundColorToolButton.setPalette(pal)
        
        self.textColorMenu = QMenu(objectName="textColorMenu")
        self.widgetAction = WidgetAction(
            )
        self.textColorWidget = TextColorWidget()
        self.widgetAction.setDefaultWidget(
            self.textColorWidget
            )
        self.backgroundColorMenu = QMenu(objectName="backgroundColorMenu")
        self.backgroundColorMenu.addAction(self.widgetAction)
        self.backgroundColorMenuToolButton.setMenu(self.backgroundColorMenu)       

        pixmap = QPixmap(32, 32)
        pixmap.fill(qRgba(0, 0, 0, 255))
        icon = QIcon(pixmap)
        
        autoAction = QAction(
            "自動(&A)", icon=icon, parent=self.textColorMenu
            )
        icon = QIcon(":\images\Color_palette.png")
        otherColorAction = QAction(
            "他の色(&M)...", icon=icon,parent=self.textColorMenu
            )
        self.textColorMenu.addAction(autoAction)
        self.textColorMenu.addSeparator()
        self.textColorMenu.addAction(
            self.widgetAction
            )
        self.textColorMenu.addSeparator()
        self.textColorMenu.addAction(otherColorAction)
        self.textColorMenuToolButton.setMenu(
            self.textColorMenu
            )


        self.widgetAction.colorLabelPress.connect(
            t.setTextColorByAction
            )

        self.widgetAction.colorLabelPressWithPixmap["QLabel*", "QPixmap"].connect(
            lambda label, pixmap: autoAction.setIcon(QIcon(pixmap))
            )

        self.widgetAction.backgroundColorLabelPress.connect(
            t.setHighlightByAction
            )
        self.noColorAction = QAction("色なし(&N)", triggered=t.clearBackground)
        self.backgroundColorMenu.addAction(self.widgetAction)
        self.backgroundColorMenu.addAction(self.noColorAction)
        self.backgroundColorMenuToolButton.setMenu(self.backgroundColorMenu)
        

        autoAction.triggered.connect(
            lambda bool: t.setTextColor(
                autoAction.icon().pixmap(
                    32, 32).toImage().pixel(0, 0)
                )
            )

        self.colorDialog = QColorDialog()
        self.colorDialog.colorSelected.connect(t.setTextColor)
        otherColorAction.triggered.connect(self.colorDialog.exec)
    
        self.imageToolButton.clicked.connect(
            t.loadImage
            )
        self.imageAction = QAction(text="画像(&P)",
                              parent=self.imageMenuToolButton,
                              triggered=t.loadImage
                              )
        self.imageChangeAction = QAction(text="画像の変更(&G)",
                                    parent=self.imageMenuToolButton,
                                    triggered=t.changeImage
                                    )
        self.imageSizeChangeAction = QAction(text="画像のサイズ変更(&R)",
                                        parent=self.imageMenuToolButton,
                                        triggered = t.changeImageSize)#new
   
        self.imageMenu = QMenu(self.imageMenuToolButton)
        self.imageMenu.addAction(self.imageAction)
        self.imageMenu.addAction(self.imageChangeAction)#new
        self.imageMenu.addAction(self.imageSizeChangeAction)

        self.imageMenuToolButton.setMenu(self.imageMenu)

        imageHandler = ImageHandler(
            t.document(), mainScene)
        t.imageHandler = imageHandler
        mainScene.addItem(t.imageHandler)
        t.imageHandler.createChildItems()
        t.imageHandler.setVisible(False)

class ImageObjectInterface(QPyTextObject):

    def __init__(self, parent=None):
        super().__init__(parent)

    def intrinsicSize(
        self, doc, posInDocument, format
        ):
        image = format.property(ImageProperty)
        return QSizeF(image.size())

    def drawObject(
        self, painter, rect, doc, posInDocument, format
        ):

        image = format.property(ImageProperty)
        image.render(painter, rect.topLeft().toPoint())
        image.move(rect.topLeft().toPoint())
        
class BaseObject(QGraphicsObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.m_rect = QRectF()

    def setRect(self, rect):
        
        self.prepareGeometryChange()
        self.m_rect = QRectF(rect)

    def rect(self):

        return self.m_rect
        
    def paint(self, painter, option, widget):

        pass
        
    def boundingRect(self):
        
        return self.m_rect

class ImageHandler(BaseObject):

    Central = 0
    TopLeft = 1
    Top = 2
    TopRight= 3
    Left = 4
    Right = 5
    BottomLeft = 6
    Bottom = 7
    BottomRight = 8

    def __init__(
        self, doc, mainScene, place = 0, parent=None
        ):
        super().__init__(parent)
        self.doc = doc
        self.mainScene = mainScene
        self.m_place = place
        self.setFlags(QGraphicsObject.ItemIsSelectable)
        self.setAcceptHoverEvents(True)
        
        self.obj = None
        self.pixmap = QPixmap()

    def setCustomObject(self, obj):

        self.obj = obj

    def hoverEnterEvent(self, event):

        if self.parentItem():
            self.setCursor(
                Qt.CursorShape.PointingHandCursor
                )
            return super().hoverEnterEvent(event)

    def mouseMoveEvent(self, event):

        if self.obj is not None:
            parentItem = self.parentItem()
            if parentItem:
                
                parentRect = parentItem.rect()
                sceneX, sceneY = event.scenePos().x(), event.scenePos().y()
                if self.m_place in (self.BottomRight, self.TopLeft, self.TopRight, self.BottomLeft):
                    #角の場合は、KeepAspectRatioにしようかなと。
                    if self.m_place == self.BottomRight:                    
                        
                        parentRect.setBottomRight(QPoint(sceneX, sceneY))                    

                    elif self.m_place == self.TopRight:

                        parentRect.setTopRight(QPoint(sceneX, sceneY))

                    elif self.m_place == self.BottomLeft:
                        parentRect.setBottomLeft(QPoint(sceneX, sceneY))

                    elif self.m_place == self.TopLeft:
                        parentRect.setTopLeft(QPoint(sceneX, sceneY))
                        
                    parentItem.setRect(parentRect)
                    pixmap = self.obj.pixmap()
                    p = pixmap.scaled(parentRect.size().toSize(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
                    dp = self.obj._doubleBuffer.scaled(p.size(),
                                      Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
                    self.parentItem().pixmap = dp
                    
                elif self.m_place in (self.Right, self.Top, self.Left, self.Bottom):
                    if self.m_place == self.Right:
                        parentRect.setRight( sceneX)
                    elif self.m_place == self.Top:
                        parentRect.setTop(sceneY)
                    elif self.m_place == self.Left:
                        parentRect.setLeft(sceneX)
                    elif self.m_place == self.Bottom:
                        parentRect.setBottom(sceneY)

                    parentItem.setRect(parentRect)
                    pixmap = self.obj.pixmap()
             
                    p = pixmap.scaled(parentRect.size().toSize(),
                        Qt.AspectRatioMode.IgnoreAspectRatio,
                              Qt.TransformationMode.SmoothTransformation)
                    dp = self.obj._doubleBuffer.scaled(p.size(),
                                     Qt.AspectRatioMode.IgnoreAspectRatio,
                                     Qt.TransformationMode.SmoothTransformation)
                    self.parentItem().pixmap = dp           

        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

        if self.obj is not None:

                parentItem = self.parentItem()
                if parentItem:
                    
                    parentRect = parentItem.rect()
                    sceneX, sceneY = event.scenePos().x(), event.scenePos().y()
                    if self.m_place in (self.BottomRight, self.TopLeft, self.TopRight, self.BottomLeft):
                        
                        if self.m_place == self.BottomRight:                    
                            
                            parentRect.setBottomRight(QPoint(sceneX, sceneY))                    

                        elif self.m_place == self.TopRight:

                            parentRect.setTopRight(QPoint(sceneX, sceneY))
                        elif self.m_place == self.BottomLeft:
                            parentRect.setBottomLeft(QPoint(sceneX, sceneY))

                        elif self.m_place == self.TopLeft:
                            parentRect.setTopLeft(QPoint(sceneX, sceneY))               
                  
                   
                        parentItem.setRect(parentRect)
                        pixmap = self.obj.pixmap()
                        p = pixmap.scaled(parentRect.size().toSize(),
                                  Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
                        dp = self.obj._doubleBuffer.scaled(p.size(),
                                  Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
                        self.parentItem().pixmap = dp

                        
                        self.obj.setPixmap(dp)
                        self.obj.resize(dp.size())
                        self.doc.parent().setFocus()
                        self.parentItem().pixmap = QPixmap()
                        tc = self.doc.parent().textCursor()
                        tc.insertText(" ")
                        tc.deleteChar()
                        parentItem.update()
                    elif self.m_place in (self.Right, self.Top, self.Left, self.Bottom):

                        if self.m_place == self.Right:
                            parentRect.setRight( sceneX)
                        elif self.m_place == self.Top:
                            parentRect.setTop(sceneY)
                        elif self.m_place == self.Left:
                            parentRect.setLeft(sceneX)
                        elif self.m_place == self.Bottom:
                            parentRect.setBottom(sceneY)
                   
                        parentItem.setRect(parentRect)
                        pixmap = self.obj.pixmap()
                        p = pixmap.scaled(parentRect.size().toSize(),
                                      Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
                        dp = self.obj._doubleBuffer.scaled(p.size(),
                                      Qt.AspectRatioMode.IgnoreAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)

                        self.parentItem().pixmap = dp
                        self.obj.setPixmap(dp)
                        self.obj.resize(dp.size())
                        self.doc.parent().setFocus()

                        tc = self.doc.parent().textCursor()
                        tc.insertText(" ")
                        tc.deleteChar()
                        parentItem.update()
        return super().mouseReleaseEvent(event)
    
    def createChildItems(self):
        #only once
        self.topLeftHandler = ImageHandler(self.doc, self.mainScene, self.TopLeft, self)
        self.topHandler = ImageHandler(self.doc, self.mainScene, self.Top, self)
        self.topRightHandler = ImageHandler(self.doc, self.mainScene, self.TopRight, self)

        self.leftHandler = ImageHandler(self.doc, self.mainScene, self.Left, self)
        self.rightHandler = ImageHandler(self.doc, self.mainScene, self.Right, self)
        
        self.bottomLeftHandler = ImageHandler(self.doc, self.mainScene, self.BottomLeft, self)
        self.bottomHandler = ImageHandler(self.doc, self.mainScene, self.Bottom, self)
        self.bottomRightHandler = ImageHandler(self.doc, self.mainScene, self.BottomRight, self)
        
        width, height = 4, 4
        
        self.topLeftHandler.setRect(QRectF(0, 0, width, height))
        self.topHandler.setRect(QRectF(0, 0, width, height))
        self.topRightHandler.setRect(QRectF(0, 0, width, height))

        self.leftHandler.setRect(QRectF(0, 0, width, height))
        self.rightHandler.setRect(QRectF(0, 0, width, height))

        self.bottomLeftHandler.setRect(QRectF(0, 0, width, height))
        self.bottomHandler.setRect(QRectF(0, 0, width, height))
        self.bottomRightHandler.setRect(QRectF(0, 0, width, height))
    
    def paint(self, painter, option, widget):

        pen = painter.pen()
        pen.setWidth(1)
        pen.setStyle(Qt.SolidLine)
        pen.setColor(QColor(0, 0, 255, 100))
        painter.setPen(pen)
        brush = painter.brush()
        brush.setStyle(Qt.NoBrush)
        painter.setBrush(brush)
        painter.drawRect(self.m_rect)

        if not self.pixmap.isNull():
            
            painter.drawPixmap(self.m_rect.toRect(), self.pixmap)
            
    def setCenter(self):
        
        parentItem = self.parentItem()
        parentRect = parentItem.rect()
        pcx = parentRect.center().x()
        pcy = parentRect.center().y()
        pleft = parentRect.left()
        pright = parentRect.right()
        ptop = parentRect.top()
        pbottom = parentRect.bottom()
        self.prepareGeometryChange()
        
        if self.m_place == self.TopLeft:
            
            self.m_rect.moveCenter(parentRect.topLeft())
            
        elif self.m_place == self.Top:

            self.m_rect.moveCenter(QPointF(pcx,  ptop))
            
        elif self.m_place == self.TopRight:

            self.m_rect.moveCenter(parentRect.topRight())

        elif self.m_place == self.Left:
            
            self.m_rect.moveCenter(QPointF(pleft, pcy))
            
        elif self.m_place == self.Right:
            
            self.m_rect.moveCenter(QPointF(pright, pcy))
            
        elif self.m_place == self.BottomLeft:
            
            self.m_rect.moveCenter(parentRect.bottomLeft())
            
        elif self.m_place == self.Bottom:
            
            self.m_rect.moveCenter(QPointF(pcx, pbottom))
        elif self.m_place == self.BottomRight:
            
            self.m_rect.moveCenter(parentRect.bottomRight())       

    def update(self):
        if self.m_place == self.Central :
            self.setRect(self.obj.geometry())
            for child in self.childItems():
                child.setCenter()
        super().update()
        
def main():

    app = QApplication()
    app.setStyle(
        QStyleFactory.create("Fusion")
        )
    m = MainWindow()
    m.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
