# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'textListMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_ListFormatSelector(object):
    def setupUi(self, ListFormatSelector):
        if not ListFormatSelector.objectName():
            ListFormatSelector.setObjectName(u"ListFormatSelector")
        ListFormatSelector.resize(332, 383)
        self.gridLayout = QGridLayout(ListFormatSelector)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nothingLabel = QLabel(ListFormatSelector)
        self.nothingLabel.setObjectName(u"nothingLabel")
        self.nothingLabel.setMinimumSize(QSize(100, 100))
        self.nothingLabel.setMaximumSize(QSize(100, 100))
        self.nothingLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}\n"
"")
        self.nothingLabel.setFrameShape(QFrame.Box)
        self.nothingLabel.setFrameShadow(QFrame.Raised)
        self.nothingLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.nothingLabel, 0, 0, 1, 1)

        self.discLabel = QLabel(ListFormatSelector)
        self.discLabel.setObjectName(u"discLabel")
        self.discLabel.setMinimumSize(QSize(100, 100))
        self.discLabel.setMaximumSize(QSize(100, 100))
        self.discLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.discLabel.setFrameShape(QFrame.Box)
        self.discLabel.setFrameShadow(QFrame.Raised)
        self.discLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.discLabel, 0, 1, 1, 1)

        self.circleLabel = QLabel(ListFormatSelector)
        self.circleLabel.setObjectName(u"circleLabel")
        self.circleLabel.setMinimumSize(QSize(100, 100))
        self.circleLabel.setMaximumSize(QSize(100, 100))
        self.circleLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.circleLabel.setFrameShape(QFrame.Box)
        self.circleLabel.setFrameShadow(QFrame.Raised)
        self.circleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.circleLabel, 0, 2, 1, 1)

        self.decimalLabel = QLabel(ListFormatSelector)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setMinimumSize(QSize(100, 100))
        self.decimalLabel.setMaximumSize(QSize(100, 100))
        self.decimalLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.decimalLabel.setFrameShape(QFrame.Box)
        self.decimalLabel.setFrameShadow(QFrame.Raised)
        self.decimalLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.decimalLabel, 1, 0, 1, 1)

        self.squareLabel = QLabel(ListFormatSelector)
        self.squareLabel.setObjectName(u"squareLabel")
        self.squareLabel.setMinimumSize(QSize(100, 100))
        self.squareLabel.setMaximumSize(QSize(100, 100))
        self.squareLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.squareLabel.setFrameShape(QFrame.Box)
        self.squareLabel.setFrameShadow(QFrame.Raised)
        self.squareLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.squareLabel, 1, 1, 1, 1)

        self.lowerAlphaLabel = QLabel(ListFormatSelector)
        self.lowerAlphaLabel.setObjectName(u"lowerAlphaLabel")
        self.lowerAlphaLabel.setMinimumSize(QSize(100, 100))
        self.lowerAlphaLabel.setMaximumSize(QSize(100, 100))
        self.lowerAlphaLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.lowerAlphaLabel.setFrameShape(QFrame.Box)
        self.lowerAlphaLabel.setFrameShadow(QFrame.Raised)
        self.lowerAlphaLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lowerAlphaLabel, 1, 2, 1, 1)

        self.upperAlphaLabel = QLabel(ListFormatSelector)
        self.upperAlphaLabel.setObjectName(u"upperAlphaLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upperAlphaLabel.sizePolicy().hasHeightForWidth())
        self.upperAlphaLabel.setSizePolicy(sizePolicy)
        self.upperAlphaLabel.setMinimumSize(QSize(100, 100))
        self.upperAlphaLabel.setMaximumSize(QSize(100, 100))
        self.upperAlphaLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.upperAlphaLabel.setFrameShape(QFrame.Box)
        self.upperAlphaLabel.setFrameShadow(QFrame.Raised)
        self.upperAlphaLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.upperAlphaLabel, 2, 0, 1, 1)

        self.lowerRomanLabel = QLabel(ListFormatSelector)
        self.lowerRomanLabel.setObjectName(u"lowerRomanLabel")
        self.lowerRomanLabel.setMinimumSize(QSize(100, 100))
        self.lowerRomanLabel.setMaximumSize(QSize(100, 100))
        self.lowerRomanLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.lowerRomanLabel.setFrameShape(QFrame.Box)
        self.lowerRomanLabel.setFrameShadow(QFrame.Raised)
        self.lowerRomanLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.lowerRomanLabel, 2, 1, 1, 1)

        self.upperRomanLabel = QLabel(ListFormatSelector)
        self.upperRomanLabel.setObjectName(u"upperRomanLabel")
        self.upperRomanLabel.setMinimumSize(QSize(100, 100))
        self.upperRomanLabel.setMaximumSize(QSize(100, 100))
        self.upperRomanLabel.setSizeIncrement(QSize(0, 0))
        self.upperRomanLabel.setStyleSheet(u"QLabel{background-color:rgb(255, 255, 255)}")
        self.upperRomanLabel.setFrameShape(QFrame.Box)
        self.upperRomanLabel.setFrameShadow(QFrame.Raised)
        self.upperRomanLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.upperRomanLabel, 2, 2, 1, 1)


        self.retranslateUi(ListFormatSelector)

        QMetaObject.connectSlotsByName(ListFormatSelector)
    # setupUi

    def retranslateUi(self, ListFormatSelector):
        ListFormatSelector.setWindowTitle(QCoreApplication.translate("ListFormatSelector", u"Form", None))
        self.nothingLabel.setText(QCoreApplication.translate("ListFormatSelector", u"\u306a\u3057", None))
        self.discLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1"
                        ";\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul></body></html>", None))
        self.circleLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margi"
                        "n-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul type=\"circle\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul></body></html>\n"
"\n"
"", None))
        self.decimalLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1"
                        ";\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol></body></html>", None))
        self.squareLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ul type=\"square\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul type=\"square\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margi"
                        "n-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul>\n"
"<ul type=\"square\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ul></body></html>", None))
        self.lowerAlphaLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol type=\"a\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"a\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0"
                        "px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"a\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol></body></html>\n"
"\n"
"", None))
        self.upperAlphaLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol type=\"A\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"A\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0"
                        "px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"A\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol></body></html>", None))
        self.lowerRomanLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol type=\"i\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"i\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0"
                        "px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"i\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol></body></html>", None))
        self.upperRomanLabel.setText(QCoreApplication.translate("ListFormatSelector", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Yu Gothic UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<ol type=\"I\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"I\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0"
                        "px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol>\n"
"<ol type=\"I\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">______</li></ol></body></html>", None))
    # retranslateUi

