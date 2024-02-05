# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'replaceDialog.ui'
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

class Ui_ReplaceDialog(object):
    def setupUi(self, ReplaceDialog):
        if not ReplaceDialog.objectName():
            ReplaceDialog.setObjectName(u"ReplaceDialog")
        ReplaceDialog.resize(400, 164)
        self.layoutWidget = QWidget(ReplaceDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 20, 87, 121))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.searchNextPushButton = QPushButton(self.layoutWidget)
        self.searchNextPushButton.setObjectName(u"searchNextPushButton")

        self.verticalLayout_2.addWidget(self.searchNextPushButton)

        self.replaceNextPushButton = QPushButton(self.layoutWidget)
        self.replaceNextPushButton.setObjectName(u"replaceNextPushButton")

        self.verticalLayout_2.addWidget(self.replaceNextPushButton)

        self.replaceAllPushButton = QPushButton(self.layoutWidget)
        self.replaceAllPushButton.setObjectName(u"replaceAllPushButton")

        self.verticalLayout_2.addWidget(self.replaceAllPushButton)

        self.cancelButton = QPushButton(self.layoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)

        self.widget = QWidget(ReplaceDialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 243, 110))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.searchTextLabel = QLabel(self.widget)
        self.searchTextLabel.setObjectName(u"searchTextLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.searchTextLabel)

        self.searchTextLineEdit = QLineEdit(self.widget)
        self.searchTextLineEdit.setObjectName(u"searchTextLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.searchTextLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.replacedTextLabel = QLabel(self.widget)
        self.replacedTextLabel.setObjectName(u"replacedTextLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.replacedTextLabel)

        self.replacedLineEdit = QLineEdit(self.widget)
        self.replacedLineEdit.setObjectName(u"replacedLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.replacedLineEdit)


        self.verticalLayout_3.addLayout(self.formLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.wholeWordsCheckBox = QCheckBox(self.widget)
        self.wholeWordsCheckBox.setObjectName(u"wholeWordsCheckBox")

        self.verticalLayout.addWidget(self.wholeWordsCheckBox)

        self.findCaseSensitivelyCheckBox = QCheckBox(self.widget)
        self.findCaseSensitivelyCheckBox.setObjectName(u"findCaseSensitivelyCheckBox")

        self.verticalLayout.addWidget(self.findCaseSensitivelyCheckBox)


        self.verticalLayout_3.addLayout(self.verticalLayout)

#if QT_CONFIG(shortcut)
        self.searchTextLabel.setBuddy(self.searchTextLineEdit)
        self.replacedTextLabel.setBuddy(self.replacedLineEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ReplaceDialog)
        self.cancelButton.clicked.connect(ReplaceDialog.close)

        QMetaObject.connectSlotsByName(ReplaceDialog)
    # setupUi

    def retranslateUi(self, ReplaceDialog):
        ReplaceDialog.setWindowTitle(QCoreApplication.translate("ReplaceDialog", u"Dialog", None))
        self.searchNextPushButton.setText(QCoreApplication.translate("ReplaceDialog", u"\u6b21\u3092\u691c\u7d22(&F)", None))
        self.replaceNextPushButton.setText(QCoreApplication.translate("ReplaceDialog", u"\u7f6e\u63db\u3057\u3066\u6b21\u306b(&R)", None))
        self.replaceAllPushButton.setText(QCoreApplication.translate("ReplaceDialog", u"\u5168\u3066\u7f6e\u63db(&A)", None))
        self.cancelButton.setText(QCoreApplication.translate("ReplaceDialog", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
        self.searchTextLabel.setText(QCoreApplication.translate("ReplaceDialog", u"\u691c\u7d22\u3059\u308b\u6587\u5b57\u5217(&N):", None))
        self.replacedTextLabel.setText(QCoreApplication.translate("ReplaceDialog", u"\u7f6e\u63db\u5f8c\u306e\u6587\u5b57\u5217(&P):", None))
        self.wholeWordsCheckBox.setText(QCoreApplication.translate("ReplaceDialog", u"\u5358\u8a9e\u5358\u4f4d\u3067\u63a2\u3059(&W)", None))
        self.findCaseSensitivelyCheckBox.setText(QCoreApplication.translate("ReplaceDialog", u"\u5927\u6587\u5b57\u3068\u5c0f\u6587\u5b57\u3092\u533a\u5225\u3059\u308b(&C)", None))
    # retranslateUi

