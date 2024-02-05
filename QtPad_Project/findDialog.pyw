# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'findDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_FindDialog(object):
    def setupUi(self, FindDialog):
        if not FindDialog.objectName():
            FindDialog.setObjectName(u"FindDialog")
        FindDialog.resize(410, 145)
        self.widget = QWidget(FindDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 40, 220, 24))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.searchTextLabel = QLabel(self.widget)
        self.searchTextLabel.setObjectName(u"searchTextLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.searchTextLabel)

        self.searchTextLineEdit = QLineEdit(self.widget)
        self.searchTextLineEdit.setObjectName(u"searchTextLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.searchTextLineEdit)

        self.widget1 = QWidget(FindDialog)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 70, 173, 48))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wholeWordsCheckBox = QCheckBox(self.widget1)
        self.wholeWordsCheckBox.setObjectName(u"wholeWordsCheckBox")

        self.verticalLayout.addWidget(self.wholeWordsCheckBox)

        self.findCaseSensitivelyCheckBox = QCheckBox(self.widget1)
        self.findCaseSensitivelyCheckBox.setObjectName(u"findCaseSensitivelyCheckBox")

        self.verticalLayout.addWidget(self.findCaseSensitivelyCheckBox)

        self.widget2 = QWidget(FindDialog)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(280, 40, 77, 56))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchNextPushButton = QPushButton(self.widget2)
        self.searchNextPushButton.setObjectName(u"searchNextPushButton")

        self.verticalLayout_2.addWidget(self.searchNextPushButton)

        self.cancelButton = QPushButton(self.widget2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)

#if QT_CONFIG(shortcut)
        self.searchTextLabel.setBuddy(self.searchTextLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(FindDialog)

        QMetaObject.connectSlotsByName(FindDialog)
    # setupUi

    def retranslateUi(self, FindDialog):
        FindDialog.setWindowTitle(QCoreApplication.translate("FindDialog", u"Dialog", None))
        self.searchTextLabel.setText(QCoreApplication.translate("FindDialog", u"\u691c\u7d22\u3059\u308b\u6587\u5b57\u5217(&N):", None))
        self.wholeWordsCheckBox.setText(QCoreApplication.translate("FindDialog", u"\u5358\u8a9e\u5358\u4f4d\u3067\u63a2\u3059(&W)", None))
        self.findCaseSensitivelyCheckBox.setText(QCoreApplication.translate("FindDialog", u"\u5927\u6587\u5b57\u3068\u5c0f\u6587\u5b57\u3092\u533a\u5225\u3059\u308b(&C)", None))
        self.searchNextPushButton.setText(QCoreApplication.translate("FindDialog", u"\u6b21\u3092\u691c\u7d22(&F)", None))
        self.cancelButton.setText(QCoreApplication.translate("FindDialog", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
    # retranslateUi

