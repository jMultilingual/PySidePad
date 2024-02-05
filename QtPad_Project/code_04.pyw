from PySide6.QtWidgets import (QApplication,
                               QTextEdit,
                               QGraphicsView,
                               QGraphicsScene,
                               )
from PySide6.QtGui import (QPageSize,
                           QBrush,#new
                           QGradient#new
                           )
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize   = g_pageSizeF.toSize()

def main():

    app = QApplication()
    g = QGraphicsView()
    s = QGraphicsScene()
    brush = QBrush(
        QGradient.Preset.SaltMountain
        )#new
    s.setBackgroundBrush(brush)#new
    g.setScene(s)
    t = QTextEdit()
    t.resize(g_pageSize)
    s.addWidget(t)
    g.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
