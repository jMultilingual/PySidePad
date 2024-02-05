from PySide6.QtWidgets import (QApplication,
                               QTextEdit,
                               QGraphicsView,
                               QGraphicsScene,
                               )
from PySide6.QtGui import QPageSize#new
import sys

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)#new
g_pageSize   = g_pageSizeF.toSize()#new

def main():

    app = QApplication()
    g = QGraphicsView()
    s = QGraphicsScene()
    g.setScene(s)
    t = QTextEdit()
    t.resize(g_pageSize)#new
    s.addWidget(t)
    g.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
