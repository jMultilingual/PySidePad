from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QGraphicsView,
                               QGraphicsScene,
                               QTextEdit)

from PySide6.QtGui import (QPageSize,
                           QGradient,
                           QBrush)

from mainWindow import Ui_MainWindow
import sys

g_pageSizeF = QPageSize(
    QPageSize.A4).size(QPageSize.Point)

g_pageSize = g_pageSizeF.toSize()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setupUi(self)
        s = QGraphicsScene()
        b = QBrush(QGradient.Preset.SaltMountain)
        s.setBackgroundBrush(b)
        self.mainView.setScene(s)
        t = QTextEdit(size = g_pageSize)
        s.addWidget(t)

        self.fontComboBox.currentFontChanged.connect(
            t.setCurrentFont
            )#new

       

        self.fontPointSizeComboBox.currentTextChanged.connect(
            lambda i: t.setFontPointSize(float(i)))#new


def main():
    app = QApplication()
    m = MainWindow()
    m.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
