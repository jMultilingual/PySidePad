from PySide6.QtWidgets import (QApplication,
                               QMainWindow)
from mainWindow import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setupUi(self)


def main():
    app = QApplication()
    m = MainWindow()
    m.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
