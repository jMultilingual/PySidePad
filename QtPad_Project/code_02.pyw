from PySide6.QtWidgets import (QApplication,
                               QTextEdit,
                               QGraphicsView,#new
                               QGraphicsScene,#new
                               )

import sys

def main():

    app = QApplication()
    g = QGraphicsView()#new
    s = QGraphicsScene()#new
    g.setScene(s)
    t = QTextEdit()
    s.addWidget(t)
    g.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
