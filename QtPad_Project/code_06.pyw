from PySide6.QtWidgets import (QApplication,
                               QTextEdit,
                               QGraphicsView,
                               QGraphicsScene,
                               QTabWidget,#new
                               QWidget,#new
                               QVBoxLayout#new
                               )
from PySide6.QtGui import (QPageSize,
                           QBrush,
                           QGradient
                           )
from PySide6.QtCore import Qt 
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize   = g_pageSizeF.toSize()

class TabWidget(QTabWidget):#new↓

    def __init__(self, parent=None):
        super().__init__(parent)

        fileMenuWidget = QWidget(fixedHeight=100)
        homeMenuWidget = QWidget(fixedHeight=100)
        displayMenuWidget = QWidget(fixedHeight=100)

        self.addTab(fileMenuWidget, "ファイル")
        self.addTab(homeMenuWidget, "ホーム")
        self.addTab(displayMenuWidget, "表示")

        

class TextEdit(QTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
            )
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
            )
        self.resize(g_pageSize)
        self.document().contentsChanged.connect(
            self.resizeToDocumentSize
            )

    def resizeToDocumentSize(self):
        doc = self.document()
        if (doc.size().height() > g_pageSize.height()):
            self.resize(
                self.size().width(), doc.size().height()
                )
 

def main():

    app = QApplication()
    w = QWidget()#new
    tab = TabWidget()#new
    t = TextEdit()#new
    
    g = QGraphicsView()
    s = QGraphicsScene()
    s.addWidget(t)
    v = QVBoxLayout()#new
    v.addWidget(tab)#new
    v.addWidget(g)#new
    w.setLayout(v)#new
    brush = QBrush(
        QGradient.Preset.SaltMountain
        )
    s.setBackgroundBrush(brush)
    g.setScene(s)
    t = TextEdit() 
    
    s.addWidget(t)
    w.show()#new
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
