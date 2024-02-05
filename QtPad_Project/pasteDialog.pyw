# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pasteDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QRadioButton, QSizePolicy,
    QWidget)
import images_rc

class Ui_PasteDialog(object):
    def setupUi(self, PasteDialog):
        if not PasteDialog.objectName():
            PasteDialog.setObjectName(u"PasteDialog")
        PasteDialog.resize(598, 380)
        self.buttonBox = QDialogButtonBox(PasteDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(500, 30, 81, 61))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(PasteDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 49, 16))
        self.label_2 = QLabel(PasteDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 30, 49, 16))
        self.pasteRadioButton = QRadioButton(PasteDialog)
        self.pasteRadioButton.setObjectName(u"pasteRadioButton")
        self.pasteRadioButton.setGeometry(QRect(20, 130, 89, 20))
        self.pasteRadioButton.setChecked(True)
        self.LinkPasteRadioButton = QRadioButton(PasteDialog)
        self.LinkPasteRadioButton.setObjectName(u"LinkPasteRadioButton")
        self.LinkPasteRadioButton.setEnabled(False)
        self.LinkPasteRadioButton.setGeometry(QRect(20, 160, 101, 20))
        self.resultGroupBox = QGroupBox(PasteDialog)
        self.resultGroupBox.setObjectName(u"resultGroupBox")
        self.resultGroupBox.setGeometry(QRect(30, 250, 531, 101))
        self.widget = QWidget(self.resultGroupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 481, 71))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.iconLabel = QLabel(self.widget)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setMinimumSize(QSize(0, 0))
        self.iconLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.iconLabel)

        self.explanationLabel = QLabel(self.widget)
        self.explanationLabel.setObjectName(u"explanationLabel")

        self.horizontalLayout.addWidget(self.explanationLabel)

        self.iconDisplayCheckBox = QCheckBox(PasteDialog)
        self.iconDisplayCheckBox.setObjectName(u"iconDisplayCheckBox")
        self.iconDisplayCheckBox.setGeometry(QRect(480, 130, 111, 20))
        self.listWidget = QListWidget(PasteDialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(130, 100, 331, 131))
        self.formatLabel = QLabel(PasteDialog)
        self.formatLabel.setObjectName(u"formatLabel")
        self.formatLabel.setGeometry(QRect(130, 60, 111, 16))
#if QT_CONFIG(shortcut)
        self.formatLabel.setBuddy(self.listWidget)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(PasteDialog)
        self.buttonBox.accepted.connect(PasteDialog.accept)
        self.buttonBox.rejected.connect(PasteDialog.reject)

        QMetaObject.connectSlotsByName(PasteDialog)
    # setupUi

    def retranslateUi(self, PasteDialog):
        PasteDialog.setWindowTitle(QCoreApplication.translate("PasteDialog", u"\u5f62\u5f0f\u3092\u9078\u629e\u3057\u3066\u8cbc\u308a\u4ed8\u3051", None))
        self.label.setText(QCoreApplication.translate("PasteDialog", u"\u30ea\u30f3\u30af\u5143:", None))
        self.label_2.setText(QCoreApplication.translate("PasteDialog", u"\u4e0d\u660e", None))
        self.pasteRadioButton.setText(QCoreApplication.translate("PasteDialog", u"\u8cbc\u308a\u4ed8\u3051(&P)", None))
        self.LinkPasteRadioButton.setText(QCoreApplication.translate("PasteDialog", u"\u30ea\u30f3\u30af\u8cbc\u308a\u4ed8\u3051(&L)", None))
        self.resultGroupBox.setTitle(QCoreApplication.translate("PasteDialog", u"\u7d50\u679c", None))
        self.iconLabel.setText("")
        self.explanationLabel.setText("")
        self.iconDisplayCheckBox.setText(QCoreApplication.translate("PasteDialog", u"\u30a2\u30a4\u30b3\u30f3\u3067\u8868\u793a(&D)", None))
        self.formatLabel.setText(QCoreApplication.translate("PasteDialog", u"\u5f35\u308a\u4ed8\u3051\u308b\u5f62\u5f0f:(&A)", None))
    # retranslateUi

