# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dateandtimedialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QListWidget, QListWidgetItem, QSizePolicy,
    QWidget)

class Ui_DateAndTimeDialog(object):
    def setupUi(self, DateAndTimeDialog):
        if not DateAndTimeDialog.objectName():
            DateAndTimeDialog.setObjectName(u"DateAndTimeDialog")
        DateAndTimeDialog.resize(400, 300)
        self.gridLayout = QGridLayout(DateAndTimeDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(DateAndTimeDialog)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(DateAndTimeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(DateAndTimeDialog)
        self.buttonBox.accepted.connect(DateAndTimeDialog.accept)
        self.buttonBox.rejected.connect(DateAndTimeDialog.reject)

        QMetaObject.connectSlotsByName(DateAndTimeDialog)
    # setupUi

    def retranslateUi(self, DateAndTimeDialog):
        DateAndTimeDialog.setWindowTitle(QCoreApplication.translate("DateAndTimeDialog", u"\u65e5\u4ed8\u3068\u6642\u523b", None))
    # retranslateUi

