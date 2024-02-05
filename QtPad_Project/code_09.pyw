from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QGraphicsView,#new
                               QGraphicsScene,#new
                               QTextEdit)#new

from PySide6.QtGui import (QPageSize,
                           QGradient,
                           QBrush)

from mainWindow import Ui_MainWindow
import sys

g_pageSizeF = QPageSize(
    QPageSize.A4).size(QPageSize.Point)#new

g_pageSize = g_pageSizeF.toSize()#new


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setupUi(self)
        s = QGraphicsScene()#new↓
        b = QBrush(QGradient.Preset.SaltMountain)
        s.setBackgroundBrush(b)
        self.mainView.setScene(s)
        t = QTextEdit(size = g_pageSize)
        s.addWidget(t)
        


def main():
    app = QApplication()
    m = MainWindow()
    m.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
