from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QGraphicsView,
                                QGraphicsScene,
                                QTextEdit)
from PySide6.QtGui import (QPageSize,
                                               QGradient,
                                               QBrush,
                                               QTextCharFormat,
                                               QTextCursor
                           )

from PySide6.QtCore import Qt 
from mainWindow import Ui_MainWindow
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize = g_pageSizeF.toSize()

KeepAnchor = QTextCursor.KeepAnchor
FontPropertiesSpecifiedOnly = QTextCharFormat.FontPropertiesSpecifiedOnly

AlignSuperScript = QTextCharFormat.AlignSuperScript#new
AlignNormal = QTextCharFormat.AlignNormal#new
AlignSubScript = QTextCharFormat.AlignSubScript#new


class TextEdit(QTextEdit):

    def setBold(self, bool):#new↓

        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontWeight(
            QFont.Bold if bool else QFont.Normal
            )
        tc.setCharFormat(charFormat)

    def setItalic(self, bool):#new↓

        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontItalic(bool)
        tc.setCharFormat(charFormat)

    def setStrikeOut(self, bool):#new↓
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontStrikeOut(bool)
        tc.setCharFormat(charFormat)

    def setUnderline(self, bool):#new↓
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setFontUnderline(bool)
        tc.setCharFormat(charFormat)

    def setSuperScript(self, bool):#new↓
        tc = self.textCursor()
        charFormat = tc.charFormat()
        charFormat.setVerticalAlignment(
            AlignSuperScript if bool else NormalScript
         )
            
        tc.setCharFormat(charFormat)

    def setSubScript(self, bool):#new↓
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
        self.boldToolButton.clicked.connect(t.setBold)#new
        self.italicToolButton.clicked.connect(t.setItalic)#new
        self.strikeOutToolButton.clicked.connect(t.setStrikeOut)#new
        self.superScriptToolButton.clicked.connect(t.setSuperScript)#new
        self.subScriptToolButton.clicked.connect(t.setSubScript)#new
        
def main():

    app = QApplication()
    m = MainWindow()
    m.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
