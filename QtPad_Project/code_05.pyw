from PySide6.QtWidgets import (QApplication,
                               QTextEdit,
                               QGraphicsView,
                               QGraphicsScene,
                               )
from PySide6.QtGui import (QPageSize,
                           QBrush,
                           QGradient
                           )
from PySide6.QtCore import Qt #new
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize   = g_pageSizeF.toSize()

class TextEdit(QTextEdit):#new↓

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
    g = QGraphicsView()
    s = QGraphicsScene()
    brush = QBrush(
        QGradient.Preset.SaltMountain
        )
    s.setBackgroundBrush(brush)
    g.setScene(s)
    t = TextEdit() #new
    
    s.addWidget(t)
    g.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
