from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QGraphicsView,
                                QGraphicsScene,
                                QTextEdit,
                                QMenu,
                                QWidgetAction,
                                QWidget,
                                QLabel, 
                                QStyleFactory,
                                QColorDialog,
                                QFileDialog)
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
                           QPyTextObject,#new
                           QTextFormat#new
                           )

from PySide6.QtCore import Qt , Signal, QEvent, QSizeF, QMimeData, QDataStream, QByteArray, QIODevice
from mainWindow import Ui_MainWindow
from textColorWidget import Ui_TextColorWidget
from backgroundColorWidget import Ui_BackgroundColorWidget
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize = g_pageSizeF.toSize()

KeepAnchor = QTextCursor.KeepAnchor
FontPropertiesSpecifiedOnly = QTextCharFormat.FontPropertiesSpecifiedOnly

AlignSuperScript = QTextCharFormat.AlignSuperScript
AlignNormal = QTextCharFormat.AlignNormal
AlignSubScript = QTextCharFormat.AlignSubScript

ImageProperty = 1#new
ImageObject = QTextFormat.UserObject#new

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
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.imageObjectInterface = ImageObjectInterface()
        docLayout = self.document().documentLayout()
        docLayout.registerHandler(
            ImageObject, self.imageObjectInterface
            )

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

            ds.writeQString(
                tc.selection().toHtml())
            
            start = tc.selectionStart()

            while True:
                tc = self.document().find(
                    chr(0xfffc), searchStart
                    )

                if not tc.isNull():

                    ds.writeUInt64(
                        tc.selectionStart() - absoluteStart
                        )
                    charFormat = tc.charFormat()
                    ds.writeUInt16(charFormat.objectType())
                    ds << charFormat.property(
                        ImageProperty
                        )
                    
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
            tc.insertHtml(ds.readQString())
            tc.setKeepPositionOnInsert(False)
            while not ds.atEnd():
                rs = ds.readUInt64()
                tc.setPosition(pos + rs)
                ot = ds.readUInt16()
                image = QImage()
                ds >> image
                char = tc.charFormat()
                char.setObjectType(ot)
                char.setProperty(
                    ImageProperty, image
                    )
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
##            tc.insertImage(i)
            char = tc.charFormat()
            char.setObjectType(ImageObject)
            char.setProperty(ImageProperty, i)
            tc.insertText(chr(0xfffc), char)

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
        s  = QGraphicsScene()
        b = QBrush(QGradient.Preset.SaltMountain)
        s.setBackgroundBrush(b)
        self.mainView.setScene(s)
        t = TextEdit()
        s.addWidget(t)
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
        painter.drawImage(rect ,image)
        
        
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
