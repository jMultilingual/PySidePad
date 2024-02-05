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
                                QSpinBox,
                                QStyleFactory,
                                QColorDialog,
                                QFileDialog,
                                QDialog,
                                QListWidgetItem,
                                QMessageBox, QButtonGroup)
from PySide6.QtGui import (QPageSize,
                                               QGradient,
                                               QBrush,
                                               QTextCharFormat,
                           QTextListFormat,
                                               QTextCursor,
                           QFont,
                           QColor,
                           QPalette,
                           QPixmap,
                           QAction,
                           QIcon,
                           qRgba,
                           QImage,
                           QPyTextObject,
                           QTextFormat,
                           QTransform,
                           QTextDocument,
                           QPolygonF,
                           QPen,
                           QPainter,
                           QTextOption,QRegularExpressionValidator, QDoubleValidator,QValidator,QActionGroup)

from PySide6.QtCore import QRegularExpression, QSignalBlocker, QLocale, QDateTime, Qt , QRectF, QPointF,QPoint, Signal, QEvent, QSize, QSizeF, QMimeData, QDataStream, QByteArray, QIODevice
from mainWindow import Ui_MainWindow
from textColorWidget import Ui_TextColorWidget
from backgroundColorWidget import Ui_BackgroundColorWidget
from imageSizeChangeDialog import Ui_ImageSizeChangeDialog
from dateandtimedialog import Ui_DateAndTimeDialog
from replaceDialog import Ui_ReplaceDialog
from pasteDialog import Ui_PasteDialog
from findDialog import Ui_FindDialog
from textListMenu import Ui_ListFormatSelector
from paragraphDialog import Ui_ParagraphDialog
from tabStopDialog import Ui_TabStopDialog
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

g_doc_leftMargin = 4.0
g_doc_rightMargin = 4.0

A4 = QPageSize.A4
Point = QPageSize.Point
Inch = QPageSize.Inch
Pica = QPageSize.Pica
Millimeter = QPageSize.Millimeter

Black = QColor(0, 0, 0)
White = QColor(255, 255, 255)
ShallowGray = QColor(204, 204, 204)
Gray = QColor(165, 165, 165)
DenseGray = QColor(102, 102, 102)
CharCoal = QColor(  51,   51,    51)
Black = QColor( 0, 0, 0)
Red = QColor(255, 0, 0)
FleshOrange = QColor(255, 102, 0)
FleshYellow = QColor(255, 255, 0)
FleshGreen = QColor(    0, 176, 80)
FleshBlue = QColor(    0,   77, 187)
FleshPurple = QColor(155,   0, 211)
CalmRed = QColor(192, 80, 77)
CalmBrown = QColor(247, 150, 70)
CalmGreen = QColor(155, 187, 89)
CalmLightBlue = QColor(75, 172, 198)
CalmBlue = QColor(79, 129, 189)
CalmPurple = QColor(128, 100, 162)
NaturalRed = QColor(209, 99, 73)
NaturalOrange = QColor(209, 144, 73)
NaturalYellow = QColor(204, 180, 0)
NaturalGreen = QColor(143, 176, 140)
NaturalBlue = QColor(100, 107, 134)
NaturalBrown = QColor(158, 124, 124)
PastelRed = QColor(221, 132, 132)
PastelOrange = QColor(243, 164, 71)
PastelYellow = QColor(223, 206, 4)
PastelGreen = QColor(165, 181, 146)
PastelBlue = QColor(128, 158, 194)
PastelPurple = QColor(156, 133, 192)

RegExpInch  = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})\"?')
RegExpcm = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})?(cm)?')
RegExppt = QRegularExpression('(?:0|[1-9]\d{0,2})(?:\.\d{1,2})?(pt)?')
RegExppi = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})?(pi)?')

DeRegExpInch = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|\")?$')
DeRegExpcm = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|cm)?$')
DeRegExppt = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|pt)?$')
DeRegExppi = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|pi)?$')

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
    listFormatLabelPress = Signal(QLabel)
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
        elif (
            widget.objectName()
            == "listFormatSelectorMenu"):
            self.w = ListFormatSelector(widget)
            
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
            
            elif objectName == "ListFormatSelector":
                
                self.listFormatLabelPress.emit(obj)
                
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

        self.cursorPositionChanged.connect(self.spoit)

    def showTabStopDialog(self):

        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        tabPositions = blockFormat.tabPositions()
     
        unit = Point
        if self.mainWindow. unitToolButtonInch.isChecked():
            v = QRegularExpressionValidator(RegExpInch)
            unit = Inch
        elif self.mainWindow.unitToolButtonMilli.isChecked():
            v = QRegularExpressionValidator(RegExpcm)
            unit = Milli
        elif self.mainWindow.unitToolButtonPoint.isChecked():
            v = QRegularExpressionValidator(RegExppt)
            unit = Point
        elif self.mainWindow.unitToolButtonPica.isChecked():
            v = QRegularExpressionValidator(RegExppi)
            unit = Pica
        d = TabStopDialog(unit)
        for tabPosition in tabPositions:
            l = QListWidgetItem()
            position = tabPosition.position
            if self.mainWindow. unitToolButtonInch.isChecked():
                inch = self.points_to_inches(position)
                l.setText(f'{inch:.2f}"')
                
            elif self.mainWindow.unitToolButtonMilli.isChecked():
                cm = self.points_to_centimeters(position)
                l.setText(f"{cm:.2f}cm")     
                
            elif self.mainWindow.unitToolButtonPoint.isChecked():
                l.setText(f"{position}pt")               
                
            elif self.mainWindow.unitToolButtonPica.isChecked():
                pica = self.points_to_pica(position)
                l.setText(f"{pica:.2f}pi")
                
            d.tabStopListWidget.addItem(l)
        if d.tabStopListWidget.count():
            d.tabStopAllClearButton.setEnabled(True)
            
        d.tabStopLineEdit.setValidator(v)
        d.tabStopLineEdit.textChanged.connect(lambda : d.tabStopSetButton.setEnabled(len(d.tabStopLineEdit.text()) > 0))
        d.tabStopAllClearButton.clicked.connect(d.tabStopListWidget.clear)
        d.tabStopClearButton.clicked.connect(
            lambda : d.tabStopListWidget.takeItem(d.tabStopListWidget.currentRow())
            )
        d.tabStopListWidget.itemClicked.connect(lambda : d.tabStopClearButton.setEnabled(True))
        d.tabStopListWidget.itemClicked.connect(lambda item: d.tabStopLineEdit.setText(item.text()))
        d.tabStopListWidget.itemClicked.connect(lambda item: d.tabStopSetButton.setEnabled(True))
        d.tabStopSetButton.clicked.connect(d.acceptValue)
        if d.exec() == QDialog.Accepted:

           
            
            newTabPositions  = []
            for c in range(d.tabStopListWidget.count()):
                    item = d.tabStopListWidget.item(c)
                    text = item.text()
                    if self.mainWindow. unitToolButtonInch.isChecked():
                        text = text[:-1]
                        
                    elif self.mainWindow.unitToolButtonMilli.isChecked():
                        text = text[:-2]
            
                    elif self.mainWindow.unitToolButtonPoint.isChecked():
                        text = text[:-2]

                    elif self.mainWindow.unitToolButtonPica.isChecked():
                        text = text[:-2]
                    
                    tabPosition = float(text)
                    newTabPositions.append(tabPosition)

            tc = self.textCursor()
            blockFormat = tc.blockFormat()
            tabPositions = []
            for tabPosition in newTabPositions:
                tab = QTextOption.Tab()
                tab.position = tabPosition
                tabPositions.append(tab)
            blockFormat.setTabPositions(tabPositions)    
            tc.setBlockFormat(blockFormat)
            items = []
            for item in self.rulerScene.items():
                if isinstance(item, TabPointer):
                    self.rulerScene.removeItem(item)

            for newTabPosition in newTabPositions:
                tabItem = TabPointer(self.document(), self.mainScene, newTabPosition)
                self.rulerScene.addItem(tabItem)
                tabItem.update(False)

            self.rulerScene.update()
                
            

    def points_to_inches(self, points):
        # 1 inch = 72 points
        return points / 72.0

    def points_to_centimeters(self, points):
        # 1 inch = 2.54 cm
        return points / 72.0 * 2.54

    def points_to_pica(self, points):
        # 1 pica = 1/6 inch
        return points / (12.0)
    
    def showParagraphDialog(self):

        d = ParagraphDialog()

        for child in d.children():
            child.blockSignals(True)
            
        d.tabPushButton.clicked.connect(self.showTabStopDialog)
        d.tabPushButton.clicked.connect(d.reject)
        d.tabPushButton.clicked.connect(d.close)
        
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        textIndent = blockFormat.textIndent()
        indent = blockFormat.indent()
        rightIndent = blockFormat.rightMargin()
        alignment = blockFormat.alignment()
        lineHeight = blockFormat.lineHeight()
        bottomMargin = blockFormat.bottomMargin()

        if self.mainWindow.unitToolButtonInch.isChecked():
            textIndent = self.points_to_inches(textIndent)
            indent = self.points_to_inches(indent)
            rightIndent = self.points_to_inches(rightIndent)
        
            width = self.points_to_inches(g_pageSize.width())
            v = QRegularExpressionVaidator()
            d.leftLineEdit.setValidator(v)
            d.rightLineEdit.setValidator(v)
            d.firstLineEdit.setValidator(v)
            d.leftLineEdit.setText(f'{indent:.2f}"')            
            d.rightLineEdit.setText(f'{rightIndent:.2f}"')
            d.firstLineEdit.setText(f'{textIndent:.2f}"')
            
        elif self.mainWindow.unitToolButtonMilli.isChecked():
            
            textIndent = self.points_to_centimeters(textIndent)
            indent = self.points_to_centimeters(indent)
            rightIndent = self.points_to_centimeters(rightIndent)
            width = self.points_to_centimeters(g_pageSize.width())
            
            v = QRegularExpressionValidator(RegExpcm)
            d.leftLineEdit.setValidator(v)
            d.rightLineEdit.setValidator(v)
            d.firstLineEdit.setValidator(v)
            d.leftLineEdit.setText(f"{indent:.2f}cm")
            d.rightLineEdit.setText(f"{rightIndent:.2f}cm")
            d.firstLineEdit.setText(f"{textIndent:.2f}cm")

        elif self.mainWindow.unitToolButtonPoint.isChecked():
            v = QRegularExpressionValidator(RegExppt)
            d.leftLineEdit.setValidator(v)
            d.rightLineEdit.setValidator(v)
            d.firstLineEdit.setValidator(v)
            d.leftLineEdit.setText(f"{indent:.2f}")            
            d.rightLineEdit.setText(f"{rightIndent:.2f}")
            d.firstLineEdit.setText(f"{textIndent:.2f}")

        elif self.mainWindow.unitToolButtonPica.isChecked():
            v = QRegularExpressionValidator(RegExppi)
            textIndent = self.points_to_pica(textIndent)
            indent = self.points_to_pica(indent)
            rightIndent = self.points_to_pica(rightIndent)
            width = self.points_to_pica(g_pageSize.width())
            
            d.leftLineEdit.setValidator(v)
            d.rightLineEdit.setValidator(v)
            d.firstLineEdit.setValidator(v)
            d.leftLineEdit.setText(f"{indent:.2f}pi")
            d.rightLineEdit.setText(f"{rightIndent:.2f}pi")
            d.firstLineEdit.setText(f"{textIndent:.2f}pi")
        
        
        d.lineHeightComboBox.setCurrentIndex(d.lineHeightComboBox.findText(f"{float(lineHeight/100)}"))
        d.tenPointPlusCheckBox.setChecked(bottomMargin==10)
        if alignment == Qt.AlignLeft:
            d.alignmentComboBox.setCurrentIndex(0)
        elif alignment == Qt.AlignCenter:
            d.alignmentComboBox.setCurrentIndex(2)
        elif alignment == Qt.AlignRight:
            d.alignmentComboBox.setCurrentIndex(1)
        elif alignment == Qt.AlignJustify:
            d.alignmentComboBox.setCurrentIndex(3)
        #ここまでスポイト
        
        for child in d.children():
            child.blockSignals(False)
        if d.exec() == QDialog.Accepted:
            tc = self.textCursor()
            blockFormat = tc.blockFormat()

            
            
            if self.mainWindow.unitToolButtonInch.isChecked():
                textIndent = float(d.firstLineEdit.text()[:-2])
                indent = float(d.leftLineEdit.text()[:-2])
                rightIndent = float(d.rightLineEdit.text()[:-2])
                textIndent = self.inches_to_points(textIndent)
                indent = self.inches_to_points(indent)
                rightIndent  = self.inches_to_points(rightIndent)

            elif self.mainWindow.unitToolButtonMilli.isChecked():
                textIndent = float(d.firstLineEdit.text()[:-2])
                indent = float(d.leftLineEdit.text()[:-2])
                rightIndent = float(d.rightLineEdit.text()[:-2])
                
                textIndent = self.inches_to_points(textIndent)
                indent = self.inches_to_points(indent)
                rightIndent  = self.inches_to_points(rightIndent)
                
            elif self.mainWindow.unitToolButtonPoint.isChecked():
                pass

            elif self.mainWindow.unitToolButtonPica.isChecked():
                textIndent = float(d.firstLineEdit.text()[:-2])
                indent = float(d.leftLineEdit.text()[:-2])
                rightIndent = float(d.rightLineEdit.text()[:-2])
                textIndent = self.pica_to_points(textIndent)
                indent = self.pica_to_points(indent)
                rightIndent  = self.pica_to_points(rightIndent)
            newAlignment = Qt.AlignLeft
            if d.alignmentComboBox.currentIndex() == 0:
                newAlignment  = Qt.AlignLeft
            elif d.alignmentComboBox.currentIndex() == 2:
                newAlignment = Qt.AlignRight
            elif d.alignmentComboBox.currentIndex() == 1:
                newAlignment = Qt.AlignCenter
                
            elif d.alignmentComboBox.currentIndex() == 3:
                newAlignment = Qt.AlignJustify

            tc = self.textCursor()
            blockFormat = tc.blockFormat()
            blockFormat.setTextIndent(textIndent)
            blockFormat.setIndent(indent)
            blockFormat.setRightMargin(rightIndent )
    
            blockFormat.setLineHeight(float(d.lineHeightComboBox.currentText())*100, 1)
            blockFormat.setBottomMargin(10 if d.tenPointPlusCheckBox.isChecked() else 0)
            blockFormat.setAlignment(newAlignment )
      
            tc.setBlockFormat(blockFormat)     
        
            self.indentPointer.indentChanged.emit(indent )
            self.textIndentPointer.textIndentChanged.emit(textIndent)
            self.rightIndentPointer.rightIndentChanged.emit(
                g_pageSizeF.width() - rightIndent)
    def spoit(self):
        
        tc = self.textCursor()
        blockFormat = tc.blockFormat()

        textIndent = blockFormat.textIndent()
        indent = blockFormat.indent()
        rightIndent = blockFormat.rightMargin()       
        alignment = blockFormat.alignment()
        lineHeight  = blockFormat.lineHeight()/100
        hasBottomMargin = blockFormat.bottomMargin() == 10
        
        charFormat = tc.charFormat()
        isBold = charFormat.fontWeight() == QFont.Bold
        isItalic = charFormat.fontItalic()
        isUnderline = charFormat.fontUnderline()
        isStrikeout = charFormat.fontStrikeOut()

        isSuperScript = (charFormat.verticalAlignment()
                         == QTextCharFormat.VerticalAlignment.AlignSuperScript)
        isSubScript = (charFormat.verticalAlignment()
                       == QTextCharFormat.VerticalAlignment.AlignSubScript)
        

        children = []
        for child in self.mainWindow.tabWidget.children():
            children.append(QSignalBlocker(child))
     
            
        
        if lineHeight == 1.0:
            
            self.mainWindow.lineHeight_1_0.setChecked(True)
    
        elif lineHeight == 1.15:
         
            self.mainWindow.lineHeight_1_15.setChecked(True)
    
        elif lineHeight == 1.5:
        
            self.mainWindow.lineHeight_1_5.setChecked(True)
   
        elif lineHeight == 2.0:
            
            self.mainWindow.lineHeight_2_0.setChecked(True)
          
        
    
        self.mainWindow.lineHeightPlus10.setChecked(hasBottomMargin)

        
        font = charFormat.font()

        
        
        
        self.indentPointer.m_point = indent
        self.textIndentPointer.m_point = textIndent + indent
        self.rightIndentPointer.m_point = rightIndent
        self.textIndentPointer.blockSignals(True)
        self.textIndentPointer.update()
        self.textIndentPointer.blockSignals(False)
        self.indentPointer.blockSignals(True)
        self.indentPointer.update()
        self.indentPointer.blockSignals(False)

        self.rightIndentPointer.blockSignals(True)
        self.rightIndentPointer.update()
        self.rightIndentPointer.blockSignals(False)
        self.rulerView.scene().update()
        self.mainWindow.fontComboBox.setCurrentFont(font)
        found = self.mainWindow.fontPointSizeComboBox.findText(str(font.pointSize()))
        
        if found:
            blocker = QSignalBlocker( self.mainWindow.fontPointSizeComboBox)
            self.mainWindow.fontPointSizeComboBox.setCurrentIndex(found)
            blocker.unblock()
        self.mainWindow.boldToolButton.setChecked(isBold)
        self.mainWindow.italicToolButton.setChecked(isItalic)
        self.mainWindow.underlineToolButton.setChecked(isUnderline)
        self.mainWindow.strikeOutToolButton.setChecked(isStrikeout)
        self.mainWindow.superScriptToolButton.setChecked(isSubScript)
        if alignment == Qt.AlignLeft:
            self.mainWindow.alignLeftToolButton.setChecked(True)
        elif alignment == Qt.AlignRight:
            self.mainWindow.alignRightToolButton.setChecked(True)
        elif alignment == Qt.AlignJustify:
            self.mainWindow.alignJustifyToolButton.setChecked(True)
        elif alignment == Qt.AlignCenter:
            self.mainWindow.alignCenterToolButton.setChecked(True)
        
        
        
        for child in children:
            child.unblock()

    def setNoWrap(self):

        self.setLineWrapMode(QTextEdit.NoWrap)

        width = qApp.primaryScreen().availableSize().width()
        height = qApp.primaryScreen().availableSize().height()
        self.resize(qApp.primaryScreen().availableSize())

    def setWidgetWidth(self):

        self.setLineWrapMode(QTextEdit.WidgetWidth)
        width = qApp.primaryScreen().availableSize().width()
        height = qApp.primaryScreen().availableSize().height()
        self.resize(qApp.primaryScreen().availableSize())

    def setFixedPixelWidth(self):
        self.setLineWrapMode(
            QTextEdit.LineWrapMode.FixedPixelWidth
            )
        self.setLineWrapColumnOrWidth(g_pageSizeF.width())

    def setAlignment(self, button, bool):
        tc = self.textCursor()        
        blockFormat = tc.blockFormat()   
        dic = {"alignLeftToolButton":Qt.AlignLeft,
               "alignCenterToolButton":Qt.AlignCenter,
               "alignRightToolButton":Qt.AlignRight,
              "alignJustifyToolButton":Qt.AlignJustify}
        
   
        blockFormat = tc.blockFormat()
        blockFormat.setAlignment(dic[button.objectName()])
        tc.setBlockFormat(blockFormat)
        
    def setBottomMargin(self, bool):
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        blockFormat.setBottomMargin(10 if bool else 0)
        tc.setBlockFormat(blockFormat)

    def setLineHeight(self, height):
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        blockFormat.setLineHeight(height*100, 1)
        tc.setBlockFormat(blockFormat)

    def insertTextList(self, label):
        
        tc = self.textCursor()
        lf = QTextListFormat()
        if label.objectName() == "nothingLabel":
            
            pass

        elif label.objectName() == "discLabel":
            lf.setStyle(QTextListFormat.Style.ListDisc)

        elif label.objectName() == "circleLabel":
            lf.setStyle(QTextListFormat.Style.ListCircle)

        elif label.objectName() == "decimalLabel":
            lf.setStyle(QTextListFormat.Style.ListDecimal)

        elif label.objectName() == "squareLabel":
            lf.setStyle(QTextListFormat.Style.ListSquare)

        elif label.objectName() == "lowerAlphaLabel":
            lf.setStyle(QTextListFormat.Style.ListLowerAlpha)
            
        elif label.objectName() == "lowerAlphaLabel":
            lf.setStyle(QTextListFormat.Style.ListLowerAlpha)
            
        elif label.objectName() == "upperAlphaLabel":
            lf.setStyle(QTextListFormat.Style.ListUpperAlpha)

        elif label.objectName() == "lowerRomanLabel":
            lf.setStyle(QTextListFormat.Style.ListLowerRoman)
            
        elif label.objectName() == "upperRomanLabel":
            lf.setStyle(QTextListFormat.Style.ListUpperRoman)

        tc.insertList(lf)
        self.indentPointer.m_point += 40
        self.textIndentPointer.m_point += 40
        self.indentPointer.update()
        self.textIndentPointer.update()

    def moveTabPosition(self, float):

        tabPointer = self.sender()
        scene = tabPointer.scene()
        items = scene.items()
        tabItems = [
            tabItem for tabItem in
            items if isinstance(tabItem, TabPointer)]
  
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        blockFormat.setTabPositions([])
        tabPositions = []
        
        for tabItem in tabItems:
            tab = QTextOption.Tab()
            tab.type = QTextOption.LeftTab
            tab.position = tabItem.m_point
            tabPositions.append(tab)
        tabPositions.sort(
            key = lambda tab: tab.position
            )
        blockFormat.setTabPositions(tabPositions)
        tc.setBlockFormat(blockFormat)

    def plusIndent(self):

        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        indent = blockFormat.indent()
        if (indent < g_pageSizeF.width() - 36):
            self.indentPointer.indentChanged.emit(
                indent + 36)
            self.indentPointer.m_point += 36
            self.indentPointer.update()

    def minusIndent(self):
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        indent = blockFormat.indent()
        if indent - 36>= 0:
            self.indentPointer.indentChanged.emit(
                blockFormat.indent() - 36
                )
            self.indentPointer.m_point -= 36
            self.indentPointer.update()
    

    def showPasteDialog(self):
        d = PasteDialog(self)
        d.listWidget.clear()
        tc = self.textCursor()
        item = QListWidgetItem()
        item.setText(PasteDialog.Text)
        d.listWidget.addItem(item)

        if QDialog.Accepted == d.exec():
            if d.listWidget.selectedItems():
                if (d.listWidget.selectedItems()[0].text() == PasteDialog.Text):
                    self.paste()

    def setTextIndent(self, float):
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        indent = blockFormat.indent()
        blockFormat.setTextIndent(float - indent)
        tc.setBlockFormat(blockFormat)
        self.textIndentPointer.m_point = indent + (float - indent)
        self.textIndentPointer.update()

    def setIndent(self, float):

        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        blockFormat.setIndent(float)
        tc.setBlockFormat(blockFormat)

        blockFormat = tc.blockFormat()
        textIndent = blockFormat.textIndent()
        self.textIndentPointer.m_point = (textIndent + float)
        self.textIndentPointer.update()

    def setRightIndent(self, float):
        tc = self.textCursor()
        blockFormat = tc.blockFormat()
        blockFormat.setRightMargin(
            g_pageSizeF.width() - float
            )
        tc.setBlockFormat(blockFormat)

    def setTabPosition(self, tab, float):
        
        tc = self.textCursor()

        blockFormat = tc.blockFormat()
        tab.type = QTextOption.TabType.LeftTab
        tab.position = float
        tabPositions = blockFormat.tabPositions()
        tabPositions.append(tab)
        blockFormat.setTabPositions(tabPositions)
        tc.setBlockFormat(blockFormat)
        
        
            
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

    def showTimeDialog(self):
        d = DateAndTimeDialog()
        if d.exec() == QDialog.Accepted:
            item = d.listWidget.currentItem()
            tc = self.textCursor()
            tc.insertText(item.text())

    def showSearchDialog(self):

        d = FindDialog(self)
        d.exec()

    def showReplaceDialog(self):

        d = ReplaceDialog(self)
        d.exec()
    
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
        rulerScene = QGraphicsScene()
        rulerScene.setBackgroundBrush(b)
        self.rulerView.setScene(rulerScene)
        t = TextEdit()
        t.mainWindow = self
        t.rulerView = self.rulerView
        t.rulerScene = rulerScene
        t.mainScene = mainScene
        
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

        self.timeToolButton.clicked.connect(t.showTimeDialog)

        self.allSelectionToolButton.clicked.connect(t.selectAll)
        self.searchToolButton.clicked.connect(t.showSearchDialog)
        self.replaceToolButton.clicked.connect(t.showReplaceDialog)

        self.pastePushIconButton.clicked.connect(t.paste)
        self.cutToolButton.clicked.connect(t.cut)
        self.copyToolButton.clicked.connect(t.copy)

        self.pasteToolButtonMenu = QMenu()
        self.plainPasteAction = QAction("貼り付け(&P)", triggered = t.paste)
        self.selectionPasteAction = QAction(
            "形式を選択して貼り付け(&S)", triggered=t.showPasteDialog)
        self.pasteToolButtonMenu.addAction(self.plainPasteAction)
        self.pasteToolButtonMenu.addAction(self.selectionPasteAction)
        self.pasteToolButton.setMenu(
            self.pasteToolButtonMenu
            )

        rulerObject = RulerObject(t.document(), mainScene)
        rulerScene.addItem(rulerObject)
        textIndentPointer = IndentPointer(
            t.document(), mainScene, IndentPointer.TextIndent
            )
        rulerScene.addItem(textIndentPointer)
        indentPointer = IndentPointer(
            t.document(), mainScene, IndentPointer.Indent)
        rulerScene.addItem(indentPointer)
        rightIndentPointer = IndentPointer(
            t.document(), mainScene, IndentPointer.RightIndent)
        rulerScene.addItem(rightIndentPointer)
        indentPointer.textIndentPointer = textIndentPointer
        textIndentPointer.indentPointer = indentPointer
        textIndentPointer.update()
        indentPointer.update()
        rightIndentPointer.update()
        t.indentPointer = indentPointer
        t.rightIndentPointer = rightIndentPointer
        t.textIndentPointer = textIndentPointer

        textIndentPointer.textIndentChanged.connect(
            t.setTextIndent
            )
        indentPointer.indentChanged.connect(t.setIndent)
        rightIndentPointer.rightIndentChanged.connect(
            t.setRightIndent
            )
        t.document().setIndentWidth(1)

        self.indentToolButton.clicked.connect(t.plusIndent)
        self.unIndentToolButton.clicked.connect(t.minusIndent)

        self.listToolButtonMenu = QMenu(
            objectName = "listFormatSelectorMenu"
            )
        self.listToolButton.setMenu(
            self.listToolButtonMenu
            )
        self.listToolButtonMenu.addAction(self.widgetAction)
        self.widgetAction.listFormatLabelPress.connect(t.insertTextList)

        self.lineHeightToolButtonMenu = QMenu()
        self.lineHeight_1_0 = QAction(
            text="1.0", checkable=True, checked=True
            )
        self.lineHeight_1_15 = QAction(
            text="1.15", checkable=True
            )
        self.lineHeight_1_5  = QAction(
            text="1.5", checkable=True
            )
        self.lineHeight_2_0 = QAction(
            text="2.0", checkable=True
            )

        actionGroup = QActionGroup(self)
        actionGroup.addAction(self.lineHeight_1_0)
        actionGroup.addAction(self.lineHeight_1_15)
        actionGroup.addAction(self.lineHeight_1_5)
        actionGroup.addAction(self.lineHeight_2_0)

        self.lineHeightPlus10 = QAction(
            text="段落後に１０ポイントのスペースを追加する(&A)",
            checkable = True, checked=True
            )
        self.lineHeightToolButtonMenu.addAction(
            self.lineHeight_1_0
            )
        self.lineHeightToolButtonMenu.addAction(
            self.lineHeight_1_15
            )
        self.lineHeightToolButtonMenu.addAction(
            self.lineHeight_1_5
            )
        self.lineHeightToolButtonMenu.addAction(
            self.lineHeight_2_0
            )
        self.lineHeightToolButtonMenu.addAction(
            self.lineHeightPlus10
            )

        self.lineHeightToolButton.setMenu(
            self.lineHeightToolButtonMenu
            )
        self.lineHeight_1_0.triggered.connect(
            lambda: t.setLineHeight(1.0)
            )
        self.lineHeight_1_15.triggered.connect(
            lambda:t.setLineHeight(1.15)
            )
        self.lineHeight_1_5.triggered.connect(
            lambda:t.setLineHeight(1.5)
            )
        self.lineHeight_2_0.triggered.connect(
            lambda:t.setLineHeight(2.0)
            )

        self.lineHeightPlus10.toggled.connect(
            lambda bool: t.setBottomMargin(bool)
            )
        self.lineHeightPlus10.toggled.emit(
            self.lineHeightPlus10.isChecked()
            )

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.addButton(self.alignLeftToolButton)
        self.buttonGroup.addButton(self.alignRightToolButton)
        self.buttonGroup.addButton(self.alignCenterToolButton)
        self.buttonGroup.addButton(self.alignJustifyToolButton)

        self.buttonGroup.buttonToggled["QAbstractButton*", bool].connect(t.setAlignment)

        self.zoomSpinBox = QSpinBox(
            minimum = 0,
            maximum = 200,
            value = 100,
            singleStep = 10,
            valueChanged = self.do_scale
            )
        self.statusBar().addPermanentWidget(
            self.zoomSpinBox
            )

        self.mainView.installEventFilter(self)
        t.installEventFilter(self)

        self.zoomInToolButton.clicked.connect(
            lambda: self.zoomSpinBox.valueChanged.emit(
                self.zoomSpinBox.value() + 10)
            )
        self.zoomOutToolButton.clicked.connect(
            lambda: self.zoomSpinBox.valueChanged.emit(
                self.zoomSpinBox.value() - 10)
            )
        self.zoomAdjustToolButton.clicked.connect(
            lambda: self.zoomSpinBox.valueChanged.emit(100)
            )

        self.rulerCheckBox.toggled.connect(
            self.rulerView.setVisible
            )
        self.statusBarCheckBox.toggled.connect(
            self.statusBar().setVisible
            )

        self.wrapToolButtonNothing = QAction(
            "なし(&N)", checkable=True, triggered=t.setNoWrap
            )

        self.wrapToolButtonWindow = QAction(
            "ウィンドウの端に合わせる(&W)",
            checkable=True,
            triggered = t.setWidgetWidth
            )

        self.wrapToolButtonRuler = QAction(
            "ルーラ―に合わせる(&R)", checkable=True, checked=True,
            triggered = t.setFixedPixelWidth
            )

        wrapButtonGroup = QActionGroup(self)
        wrapButtonGroup.addAction(self.wrapToolButtonNothing)
        wrapButtonGroup.addAction(self.wrapToolButtonWindow)
        wrapButtonGroup.addAction(self.wrapToolButtonRuler)

        self.wrapToolButton.addAction(self.wrapToolButtonNothing)
        self.wrapToolButton.addAction(self.wrapToolButtonWindow)
        self.wrapToolButton.addAction(self.wrapToolButtonRuler)

        self.unitToolButtonInch = QAction("インチ(&I)", checkable=True, toggled=rulerObject.calcMarkings)
        self.unitToolButtonMilli = QAction("cm(&C)", checkable=True, toggled=rulerObject.calcMarkings)
        self.unitToolButtonPoint = QAction("ポイント(&P)", checkable=True, checked=True, toggled=rulerObject.calcMarkings)        
        self.unitToolButtonPica = QAction("パイカ(&S)", checkable=True, toggled=rulerObject.calcMarkings)
        
        unitButtonGroup = QActionGroup(self)
        unitButtonGroup.addAction(self.unitToolButtonInch)
        unitButtonGroup.addAction(self.unitToolButtonMilli)
        unitButtonGroup.addAction(self.unitToolButtonPoint)
        unitButtonGroup.addAction(self.unitToolButtonPica)
    
        self.unitToolButton.addAction(self.unitToolButtonInch)
        self.unitToolButton.addAction(self.unitToolButtonMilli)
        self.unitToolButton.addAction(self.unitToolButtonPoint)
        self.unitToolButton.addAction(self.unitToolButtonPica)

        self.paragraphDialogToolButton.clicked.connect(
            t.showParagraphDialog
            )
        
        
    def eventFilter(self, obj, event):
        if (event.type() == QEvent.Wheel
            and event.modifiers() == Qt.ControlModifier):
            if event.angleDelta().y() > 0:
                if self.zoomSpinBox.value() < self.zoomSpinBox.maximum():
                    self.do_scale(
                        self.zoomSpinBox.value() + 10
                        )
                elif event.angleDelta().y() < 0:
                    if self.zoomSpinBox.value() > 0:
                        self.do_scale(
                            self.zoomSpinBox.value()
                            -10
                            )
        elif isinstance(obj, TextEdit):
            if event.type() == QEvent.Wheel:
                self.mainView.verticalScrollBar().wheelEvent(
                    event
                    )
        return super().eventFilter(obj, event)
    
    def do_scale(self, value):
        self.mainView.resetTransform()
        self.rulerView.resetTransform()
        self.zoomSpinBox.blockSignals(True)
        self.zoomSpinBox.setValue(value)
        self.zoomSpinBox.blockSignals(False)
        factor = self.zoomSpinBox.value()/100
        self.mainView.scale(factor, factor)
        self.rulerView.scale(factor, 1)
        
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

class RulerObject(BaseObject):

    def __init__(self, doc, mainScene, parent=None):
        super().__init__(parent)
        self.doc = doc
        self.mainScene = mainScene
        self.setRect(QRectF(0, 0, g_pageSizeF.width(), 25))

        self.unit = Point
        self.pointWidth = QPageSize(A4).size(Point).width()
        self.inchWidth = QPageSize(A4).size(Inch).width()
        self.picaWidth = QPageSize(A4).size(Pica).width()
        self.milliwidth = QPageSize(A4).size(Millimeter).width()

        self.markings = []
        self.calcMarkings()

    def mousePressEvent(self, event):
        if event.isAccepted():
            item = self.scene().itemAt(
                event.pos(), QTransform()
                )
            if not isinstance(item, IndentPointer):
                tabPointer = TabPointer(
                    self.doc,
                    self.mainScene,
                    event.scenePos().x())
                tabPointer.tabInserted.connect(
                    self.doc.parent().setTabPosition)
                tabPointer.tabPlaceChanged.connect(
                    self.doc.parent().moveTabPosition)
                self.scene().addItem(tabPointer)
                tabPointer.update(False)
                optionTab = QTextOption.Tab()
                tabPointer.tabInserted.emit(
                    optionTab, event.scenePos().x()
                    )

    def calculate_ruler_marks(self, width_points, interval_points):
        marks = []
        current_position = 0

        while current_position <= width_points:
            marks.append(current_position)
            current_position += interval_points

        return marks
    
    def points_to_inches(self, points):
        # 1 inch = 72 points
        return points / 72.0

    def points_to_centimeters(self, points):
        # 1 inch = 2.54 cm
        return points / 72.0 * 2.54

    def points_to_pica(self, points):
        # 1 pica = 1/6 inch
        return points / (12.0)
    
    def calcMarkings(self):

        sender = self.sender()
        if sender is not None:
            if sender.text().startswith("インチ"):
                self.unit = QPageSize.Inch
                
            elif sender.text().startswith("cm"):
                self.unit = QPageSize.Millimeter
                
            elif sender.text().startswith("ポイント"):
                self.unit = QPageSize.Point
                
            elif sender.text().startswith("パイカ"):
                self.unit = QPageSize.Pica

        pointWidth = self.pointWidth - (4.0+4.0)
        total_width_points = pointWidth
        interval_points = 6

        centimeter_point = self.points_to_centimeters(pointWidth)
        inch_point = self.points_to_inches(pointWidth)
        pica_point = self.points_to_pica(pointWidth)

        
        ruler_marks = self.calculate_ruler_marks(total_width_points, 6)
        inch_marks = self.calculate_ruler_marks(total_width_points, inch_point)
        pica_marks = self.calculate_ruler_marks(total_width_points, pica_point/36)

        centimeter_marks = self.calculate_ruler_marks(total_width_points, centimeter_point)


            
        if self.unit == QPageSize.Point:

            self.markings = [i   for i in range(0, int(pointWidth), 6)]

            if self.scene():
                self.scene().update()
        elif self.unit == QPageSize.Inch:       
        
            self.markings = inch_marks
            
            if self.scene():
                self.scene().update()
        elif self.unit == QPageSize.Millimeter:
  
            self.markings = centimeter_marks
            if self.scene():
                self.scene().update()
        elif self.unit == QPageSize.Pica:

            self.markings =pica_marks
            if self.scene():
                self.scene().update()

    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.save()
        pen  = painter.pen()
        pen.setStyle(Qt.NoPen)
        brush = painter.brush()
        brush.setStyle(Qt.NoBrush)
        brush.setColor(White)
        painter.setPen(pen)
        painter.setBrush(brush)            
        painter.drawRect(self.m_rect)            
        painter.restore()
        painter.save()
        pen = painter.pen()
        pen.setStyle(Qt.SolidLine)
        pen.setColor(Black)
        painter.setPen(pen)
        if self.unit == QPageSize.Point:         
            
            for marking in self.markings:                
                m = marking+ g_doc_leftMargin
                painter.drawLine(m, 9, m  , 7)         
                if marking%36 == 0:
                    painter.drawText(QRectF(m, 16, 20, 15), str(marking))     

        elif self.unit == QPageSize.Inch:
            i = 0
            for marking in self.markings:
                painter.drawLine(marking, 9, marking, 7)
                if i%10 == 0:
                    painter.drawText(QRectF(marking, 16, 20, 15), str(int(i/10)))
                i+= 1
        elif self.unit == QPageSize.Millimeter:
            i = 0
            for marking in self.markings:
                painter.drawLine(marking, 9, marking, 7)
                if i%5 == 0:
                    painter.drawText(QRectF(marking, 16, 20, 15), str(int(i)))
                i+= 1
        elif self.unit == QPageSize.Pica:
            i = 0
            for marking in self.markings:
                
                if i%12 == 0:
                    painter.drawLine(marking, 9, marking, 7)
                    if i%72 == 0:
                        painter.drawText(QRectF(marking, 16, 20, 15), str(int(i/12)))
                i+= 1
                
        painter.restore()
            
class IndentPointer(RulerObject):
    textIndentChanged = Signal(float)
    indentChanged = Signal(float)
    rightIndentChanged = Signal(float)

    TextIndent = 0
    Indent = 1
    RightIndent = 2

    Width = 10
    Height = 10

    def __init__(self, doc, mainScene, place = 0, parent=None):
        super().__init__(doc, parent)

        self.mainScene = mainScene
        self.setAcceptedMouseButtons(
            Qt.LeftButton
            )
        self.setFlags(
            QGraphicsObject.ItemIsSelectable
            )

        self.m_place = place
        self.m_extra = 5
        self.m_height = 10

        self.setAcceptHoverEvents(True)
        self.m_polygonF = QPolygonF()

        pen = QPen()
        pen.setStyle(Qt.PenStyle.DashDotDotLine)
        pen.setWidthF(0.5)
        pen.setColor(Black)
        self.line = self.mainScene.addLine(
            0, 0, 0, 0, pen
            )
        self.line.setZValue(0.1)

        if self.m_place == self.TextIndent:
            self.setObjectName("TextIndent")
            self.m_point = g_doc_leftMargin
            self.setRect(
                QRectF(
                    self.m_point, 0, self.Width, self.Height
                    )
                )

        elif self.m_place == self.Indent:
            self.setObjectName("Indent")
            self.m_point   = g_doc_leftMargin
            self.setRect(
                QRectF(self.m_point, self.m_height,
                       self.Width, self.Height
                       ))

        elif self.m_place == self.RightIndent:
            self.setObjectName("RightIndent")
            self.m_point = g_doc_rightMargin
            self.setRect(
                QRectF(self.rightPoint(), 0, self.Width, self.Height
                       )
                )

    def rightPoint(self):
        return g_pageSizeF.width() - self.m_point

    def mouseMoveEvent(self, event):

        pos = event.scenePos()
        self.line.prepareGeometryChange()
        self.line.setLine(
            pos.x(), 0, pos.x(), g_pageSizeF.height()
            )
        self.line.setVisible(True)
        self.update()
        self.scene().update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

        pos = event.scenePos()
        if self.m_place != IndentPointer.RightIndent:
            
            if pos.x() >= g_doc_leftMargin and pos.x() <= self.pageHalfWidth():
                
                self.m_point = pos.x()
                if self.m_place == IndentPointer.TextIndent:
                    if self.m_point < self.indentPointer.m_point:
                        self.m_point = self.indentPointer.m_point
                        
                self.setRect(
                    QRectF(QPointF(pos.x(), self.m_rect.y()), QSizeF(self.Width, self.Height))
                    )
                if self.m_place == self.Indent:
                    if self.line.x() > self.pageHalfWidth():
                        self.setRect(
                        QRectF(QPointF(g_pageSizeF.width()/2, self.m_rect.y()),
                               QSizeF(self.Width, self.Height))
                        )
                elif self.m_place == self.TextIndent:
                    if self.line.x() > g_pageSizeF.width():
                        self.setRect(
                        QRectF(QPointF(g_pageSizeF.width()-50, self.m_rect.y()),
                               QSizeF(self.Width, self.Height))
                        )
                    
                elif self.line.x() < 0:                    
                        
                    QRectF(
                        QPointF(4.0, self.m_rect.y()),
                        QSizeF(self.Width, self.Height)
                        )
                    
     
        else:
            if pos.x() >= self.pageHalfWidth() and pos.x() <= g_pageSizeF.width():
                
                self.m_point = g_pageSizeF.width() - pos.x()              
                self.setRect(
                    QRectF(QPointF(pos.x(), self.m_rect.y()), QSizeF(self.Width, self.Height))
                    )
                if self.line.x() < self.pageHalfWidth():
                    self.setRect(
                    QRectF(QPointF(self.pageHalfWidth(), self.m_rect.y()),
                           QSizeF(self.Width, self.Height))
                    )
                elif self.line.x() > g_pageSizeF.width():
                    QRectF(QPointF(g_pageSizeF.width(), self.m_rect.y()),
                           QSizeF(self.Width, self.Height)
                           )
        self.line.setVisible(False)
        self.update()
        self.scene().update()
        super().mouseReleaseEvent(event)

    def pageHalfWidth(self):

        return g_pageSizeF.width()/2
    
    def translateX(self, x):
        self.prepareGeometryChange()
        self.m_rect.translate(x, 0)

    def hoverEnterEvent(self, event):

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        event.ignore()
        
        return super().hoverEnterEvent(event)
    
    def paint(self, painter, option, widget):

        painter.setRenderHint(QPainter.Antialiasing)
        brush = painter.brush()
        brush.setStyle(Qt.SolidPattern)        
        
        if self.m_place == self.TextIndent:
            
            brush.setColor(White)
            painter.setBrush(brush)
            painter.drawPolygon(self.m_polygonF)
            
        elif self.m_place == self.Indent:
            
            brush.setColor(PastelOrange)
            painter.setBrush(brush)
            painter.drawPolygon(self.m_polygonF)   

        elif self.m_place == self.RightIndent:
            
            brush.setColor(FleshOrange )
            painter.setBrush(brush)
            
            painter.drawPolygon(self.m_polygonF)


    def update(self, emit=True):
        if hasattr(self, "m_place"):
            
            if self.m_place == self.TextIndent:
                self.m_polygonF = QPolygonF()
                self.m_polygonF.append(
                    QPointF(self.m_point, self.m_height)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point + self.m_extra, 5)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point + self.m_extra, 0)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point - self.m_extra, 0)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point -self.m_extra, 5)
                    )
                self.setRect(
                    QRectF(self.m_point, self.m_rect.y(), self.Width, self.Height)
                    )
                if emit:
                    self.textIndentChanged.emit(self.m_point)
                
                
            elif self.m_place == self.Indent:
                
                self.m_polygonF = QPolygonF()
                self.m_polygonF.append(
                    QPointF(self.m_point, 10)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point + self.m_extra, 15)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point + self.m_extra, 20)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point - self.m_extra, 20)
                    )
                self.m_polygonF.append(
                    QPointF(self.m_point - self.m_extra, 15)
                    )
                self.setRect(
                    QRectF(self.m_point, self.m_rect.y(), self.Width, self.Height)
                    )
                if emit:
                    self.indentChanged.emit(self.m_point)
      
            elif self.m_place == self.RightIndent:
                
                self.m_polygonF = QPolygonF()
                self.m_polygonF.append(
                    QPointF(self.rightPoint(), self.m_height)
                    )
                self.m_polygonF.append(
                    QPointF(self.rightPoint() + self.m_extra, 5)
                    )
                self.m_polygonF.append(
                    QPointF(self.rightPoint()+ self.m_extra, 0)
                    )
                self.m_polygonF.append(
                    QPointF(self.rightPoint()- self.m_extra, 0)
                    )
                self.m_polygonF.append(
                    QPointF(self.rightPoint()- self.m_extra, 5)
                    )
                self.setRect(
                    QRectF(self.rightPoint(), self.m_rect.y(), self.Width, self.Height)
                    )
                if emit:
                    self.rightIndentChanged.emit(self.rightPoint())        
        
        super().update()

class TabPointer(IndentPointer):

    tabInserted = Signal(QTextOption.Tab, float)
    tabPlaceChanged = Signal(float, float)

    def __init__(self,
                 doc, mainScene, x, parent=None
                 ):
        super().__init__(doc, mainScene, parent)
        
        self.m_extra = 5
        self.m_polygonF = QPolygonF()
        self.start_pos = x
        self.m_point = x
        self.setRect(
                QRectF(self.m_point, 0, 10, 10)
                )
        self.setAcceptedMouseButtons(Qt.LeftButton|Qt.RightButton)
        self.setZValue(3)
        
    def mousePressEvent(self, event):  
        
        self.start_pos  = event.scenePos().x()
        return QGraphicsObject.mousePressEvent(self, event)
        
    def mouseMoveEvent(self, event):
   
        pos = event.scenePos()
        
        self.line.prepareGeometryChange()
        self.line.setLine(pos.x(), 0, pos.x(), g_pageSizeF.height())
        self.line.setVisible(True)        
        self.scene().update()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

   
        pos = event.scenePos()
     
        self.m_point = pos.x()
        self.setRect(QRectF(self.m_point, self.m_rect.y(), 5, 5))           
       
        self.line.setVisible(False)
        self.update(False)
        self.scene().update()
        
        super().mouseReleaseEvent(event)

    def paint(self, painter, option, widget):
        
        painter.setRenderHint(QPainter.Antialiasing)
        pen = painter.pen()
        pen.setStyle(Qt.SolidLine)
        pen.setWidthF(1)
        pen.setColor(Black)
        painter.setPen(pen)
        brush = painter.brush()
        brush.setStyle(Qt.SolidPattern)
        brush.setColor(Black)
        painter.setBrush(brush)
        
        painter.drawPolygon(self.m_polygonF)
    

    def update(self, emit=True):
        
        self.m_polygonF = QPolygonF()
        
        self.m_polygonF.append(QPointF(self.m_point, 5))
        self.m_polygonF.append(QPointF(self.m_point + 1, 5))
        self.m_polygonF.append(QPointF(self.m_point + 1, 10))
        self.m_polygonF.append(QPointF(self.m_point +3, 10))
        self.m_polygonF.append(QPointF(self.m_point + 3 , 15))
        self.m_polygonF.append(QPointF(self.m_point, 15))
        self.m_polygonF.append(QPointF(self.m_point, 5))
        self.setRect(QRectF(self.m_point, self.m_rect.y(), 5, 15))
        if emit:
            self.tabPlaceChanged.emit(self.start_pos, self.m_point)          

class DateAndTimeDialog(QDialog, Ui_DateAndTimeDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.init()

    def init(self):
        QLocale.setDefault(QLocale.Japanese)
        self.listWidget.clear()
        item1 = QListWidgetItem()
        dateTime = QDateTime.currentDateTime()

        item1.setText(QLocale().toString(dateTime))
        item2 = QListWidgetItem()
        item2.setText(QLocale().toString(
            dateTime, QLocale.ShortFormat)
                      )
        item3 = QListWidgetItem()
        item3.setText(
            QLocale().toString(
                dateTime, QLocale.NarrowFormat))
        item4 = QListWidgetItem()
        item4.setText(
            QLocale().toString(dateTime, "dddd, yyyy年MM月dd日 HH:mm:ss")
            )
        self.listWidget.insertItem(0, item1)
        self.listWidget.insertItem(1, item2)
        self.listWidget.insertItem(2, item3)
        self.listWidget.insertItem(3, item4)



class FindDialog(QDialog, Ui_FindDialog):
    Capture = "Qtパッド"
    Information = "ドキュメントの検索が終わりました。"

    def __init__(self, edit, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.edit = edit
        self.count = 0
        self.searchNextPushButton.clicked.connect(
            self.searchText)

    def documentFlags(self):
        flags = QTextDocument.FindFlag()
        if self.wholeWordsCheckBox.isChecked():
            flags != QTextDocument.FindWholeWords
        if self.findCaseSensitivelyCheckBox.isChecked():
            flags != QTextDocument.FindCaseSensitively
        return flags

    def setExtraSelection(self, tc):
        ex = QTextEdit.ExtraSelection()
        ex.cursor  = tc
        ex.format = QTextCharFormat()
        ex.format.setForeground(Qt.blue)
        ex.format.setBackground(Qt.yellow)
        self.edit.setExtraSelections([ex])

    def information(self):
        QMessageBox.information(
            None,
            FindDialog.Capture,
            FindDialog.Information)

    def searchText(self):
        text = self.searchTextLineEdit.text()
        if not text:
            return
        flags = self.documentFlags()
        exs = self.edit.extraSelections()
        tc = self.edit.textCursor()
        pos = tc.position()
        if exs:
            tc = self.edit.document().find(
                text, exs[0].cursor.position(), flags
                )
        else:
            tc = self.edit.document().find(
                text, tc.position(), flags
                )

        if not tc.isNull():
            if (self.count == 1
                and pos < tc.position()):
                self.information()
                self.count = -1
            self.setExtraSelection(tc)
        else:
            self.count = 1
            tc = self.edit.document().find(text, 0, flags)
            if not tc.isNull():
                if exs:
                    if exs[0].cursor == tc:
                        self.information()
                self.setExtraSelection(tc)
            else:
                self.information()

    def closeEvent(self, event):
        self.edit.setExtraSelections([])
        super().closeEvent(event)

class ReplaceDialog(Ui_ReplaceDialog, FindDialog):

    Capture = "Qtパッド"
    Information = "ドキュメントの検索が終わりました。"

    def __init__(self, edit, parent=None):
        super().__init__(edit, parent)
        self.setupUi(self)
        self.searchNextPushButton.clicked.connect(
            self.searchText
            )
        self.replaceNextPushButton.clicked.connect(
            self.replaceText
            )
        self.replaceAllPushButton.clicked.connect(
            self.allReplace
            )

    def allReplace(self):

        tc = self.edit.textCursor()
        text = self.searchTextLineEdit.text()
        if not text:
            return
        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        exs = []
        self.findRecur(
            QTextCursor(
                self.edit.document()), text, exs, flags
            )
        for ex in exs:
            ex.insertText(replacedText)

    def findRecur(self, tc, text, exs, flags):
        tc = self.edit.document().find(text,
                                       tc.selectionEnd(),
                                       flags)
        if not tc.isNull():
            exs.append(tc)
            self.findRecur(tc, text, exs, flags)
    
    def replaceText(self):
        tc = self.edit.textCursor()
        pos = tc.position()
        text = self.searchTextLineEdit.text()
        if not text:
            return
        exs = self.edit.extraSelections()
        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        if not exs:
            tc = self.edit.document().find(
                text, pos, flags
                )
            if not tc.isNull():
                self.setExtraSelection(tc)
                return
            else:
                self.information()
        else:
            tc = QTextCursor(exs[0].cursor)
            tc.insertText(replacedText)
            tc = self.edit.document().find(
                text,
                tc.position(),
                flags)
            if not tc.isNull():
                self.setExtraSelection(tc)
                return
            else:
                self.count = 1

                tc = self.edit.document().find(text,
                                               0,
                                               flags)
                if not tc.isNull():
                    
                    if (self.count == 1 and tc.position() < pos):
                        self.setExtraSelection(tc)
                    
                    else:
                        self.information()
                        self.edit.setExtraSelections([])
                else:
                    self.count = 0
                    self.information()
                    self.edit.setExtraSelections([])

    def allReplace(self):

        tc = self.edit.textCursor()
        text = self.searchTextLineEdit.text()

        if not text:
            return

        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        exs = []
        self.findRecur(
            QTextCursor(
                self.edit.document()), text, exs, flags
            )
        tc.beginEditBlock()
        for ex in exs:
            ex.insertText(replacedText)
        tc.endEditBlock()

class PasteDialog(QDialog, Ui_PasteDialog):
    Text = "テキスト"
    def __init__(self, edit, parent=None):
        super().__init__(parent)

        self.edit = edit
        self.setupUi(self)

        self.listWidget.itemClicked.connect(
            self.showResultMessage
            )

    def showResultMessage(self, item):
        if item.text() == PasteDialog.Text:
            p = QPixmap(
                ":\images\clipboard-paste_image.png"
                )
            self.iconLabel.setPixmap(p)
            self.explanationLabel.setText(
                """クリップボードの内容を書式なしテキストとしてドキュメントに
                挿入します。""")

class ListFormatSelector(QWidget, Ui_ListFormatSelector):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

class ParagraphDialog(QDialog, Ui_ParagraphDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

class TabStopDialog(QDialog, Ui_TabStopDialog):

    def __init__(self, unit = Point, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.unit = unit
        
    def acceptValue(self):
        
        item = QListWidgetItem()
        text = self.tabStopLineEdit.text()

        if self.unit == Inch:
            if "." not in text:
                text += '.00"'
                
        elif self.unit == Point:
            if "." not in text:

                text += ".00pt"
      
                
        elif self.unit ==  Milli:
            if "." not in text:
                text += ".00cm"

        elif self.unit == Pica:
            if "." not in text:
                text += ".00pi"
                
        
            
        found = self.tabStopListWidget.findItems(text, Qt.MatchFixedString)
        if not found:
            
            item.setText(text)        
            self.tabStopListWidget.addItem(item)
            self.tabStopLineEdit.clear()
            self.tabStopListWidget.sortItems()
            
class RegularExpressionValidator(QRegularExpressionValidator):

    def __init__(self, re, parent=None):
        super().__init__(re, parent)

    def validator(self, input, pos):

        pass

        
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
