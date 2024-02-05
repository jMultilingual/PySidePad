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
                                QColorDialog)
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
                           
                           )

from PySide6.QtCore import Qt , Signal, QEvent#new
from mainWindow import Ui_MainWindow
from textColorWidget import Ui_TextColorWidget
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize = g_pageSizeF.toSize()

KeepAnchor = QTextCursor.KeepAnchor
FontPropertiesSpecifiedOnly = QTextCharFormat.FontPropertiesSpecifiedOnly

AlignSuperScript = QTextCharFormat.AlignSuperScript
AlignNormal = QTextCharFormat.AlignNormal
AlignSubScript = QTextCharFormat.AlignSubScript

class WidgetAction(QWidgetAction):#new↓

    colorLabelPress = Signal(QLabel)
    colorLabelPressWithPixmap = Signal(
        QLabel, QPixmap
        )

    def __init__(self, parent=None):
        super().__init__(parent)

    def eventFilter(self, obj, event):

        if (event.type() == QEvent.MouseButtonPress):
            self.colorLabelPress.emit(obj)
            pixmap = QPixmap(32, 32)
            pixmap.fill(
                obj.palette().color(QPalette.Window)
                )
            self.colorLabelPressWithPixmap.emit(
                obj,pixmap
                )
        return super().eventFilter(obj, event)
    

class TextColorWidget(QWidget, Ui_TextColorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

class TextEdit(QTextEdit):

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
        
        self.textColorMenu = QMenu()
        self.textColorWidgetAction = WidgetAction(
            self.textColorMenu
            )
        self.textColorWidget = TextColorWidget()
        self.textColorWidgetAction.setDefaultWidget(
            self.textColorWidget
            )

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
            self.textColorWidgetAction
            )
        self.textColorMenu.addSeparator()
        self.textColorMenu.addAction(otherColorAction)
        self.textColorMenuToolButton.setMenu(
            self.textColorMenu
            )

        for child in self.textColorWidget.children():
            child.installEventFilter(
                self.textColorWidgetAction
                )

        self.textColorWidgetAction.colorLabelPress.connect(
            t.setTextColorByAction
            )#new

        self.textColorWidgetAction.colorLabelPressWithPixmap["QLabel*", "QPixmap"].connect(
            lambda label, pixmap: autoAction.setIcon(QIcon(pixmap))
            )

        autoAction.triggered.connect(
            lambda bool: t.setTextColor(
                autoAction.icon().pixmap(
                    32, 32).toImage().pixel(0, 0)
                )
            )

        self.colorDialog = QColorDialog()
        self.colorDialog.colorSelected.connect(t.setTextColor)
        otherColorAction.triggered.connect(self.colorDialog.exec)
        
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
