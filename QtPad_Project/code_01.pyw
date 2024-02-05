from PySide6.QtWidgets import (QApplication,
                               QTextEdit)

import sys

def main():

    app = QApplication()
    t = QTextEdit()
    t.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
