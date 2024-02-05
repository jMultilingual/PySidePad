# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paragraphDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ParagraphDialog(object):
    def setupUi(self, ParagraphDialog):
        if not ParagraphDialog.objectName():
            ParagraphDialog.setObjectName(u"ParagraphDialog")
        ParagraphDialog.resize(340, 375)
        self.horizontalLayout_5 = QHBoxLayout(ParagraphDialog)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.indentGroupBox = QGroupBox(ParagraphDialog)
        self.indentGroupBox.setObjectName(u"indentGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.indentGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.leftLabel = QLabel(self.indentGroupBox)
        self.leftLabel.setObjectName(u"leftLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.leftLabel)

        self.leftLineEdit = QLineEdit(self.indentGroupBox)
        self.leftLineEdit.setObjectName(u"leftLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.leftLineEdit)

        self.rightLabel = QLabel(self.indentGroupBox)
        self.rightLabel.setObjectName(u"rightLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rightLabel)

        self.rightLineEdit = QLineEdit(self.indentGroupBox)
        self.rightLineEdit.setObjectName(u"rightLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rightLineEdit)

        self.firstLineLabel = QLabel(self.indentGroupBox)
        self.firstLineLabel.setObjectName(u"firstLineLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.firstLineLabel)

        self.firstLineEdit = QLineEdit(self.indentGroupBox)
        self.firstLineEdit.setObjectName(u"firstLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.firstLineEdit)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.verticalLayout_2.addWidget(self.indentGroupBox)

        self.lineHeightGroupBox = QGroupBox(ParagraphDialog)
        self.lineHeightGroupBox.setObjectName(u"lineHeightGroupBox")
        self.horizontalLayout = QHBoxLayout(self.lineHeightGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout_2.setHorizontalSpacing(100)
        self.label = QLabel(self.lineHeightGroupBox)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineHeightComboBox = QComboBox(self.lineHeightGroupBox)
        self.lineHeightComboBox.addItem("")
        self.lineHeightComboBox.addItem("")
        self.lineHeightComboBox.addItem("")
        self.lineHeightComboBox.addItem("")
        self.lineHeightComboBox.setObjectName(u"lineHeightComboBox")
        self.lineHeightComboBox.setMaximumSize(QSize(100, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineHeightComboBox)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.tenPointPlusCheckBox = QCheckBox(self.lineHeightGroupBox)
        self.tenPointPlusCheckBox.setObjectName(u"tenPointPlusCheckBox")
        self.tenPointPlusCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.tenPointPlusCheckBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.lineHeightGroupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.alignmentLabel = QLabel(ParagraphDialog)
        self.alignmentLabel.setObjectName(u"alignmentLabel")

        self.horizontalLayout_3.addWidget(self.alignmentLabel)

        self.alignmentComboBox = QComboBox(ParagraphDialog)
        self.alignmentComboBox.addItem("")
        self.alignmentComboBox.addItem("")
        self.alignmentComboBox.addItem("")
        self.alignmentComboBox.addItem("")
        self.alignmentComboBox.setObjectName(u"alignmentComboBox")

        self.horizontalLayout_3.addWidget(self.alignmentComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tabPushButton = QPushButton(ParagraphDialog)
        self.tabPushButton.setObjectName(u"tabPushButton")

        self.horizontalLayout_4.addWidget(self.tabPushButton)

        self.buttonBox = QDialogButtonBox(ParagraphDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

#if QT_CONFIG(shortcut)
        self.leftLabel.setBuddy(self.leftLineEdit)
        self.rightLabel.setBuddy(self.rightLineEdit)
        self.firstLineLabel.setBuddy(self.firstLineEdit)
        self.label.setBuddy(self.lineHeightComboBox)
        self.alignmentLabel.setBuddy(self.alignmentComboBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ParagraphDialog)
        self.buttonBox.accepted.connect(ParagraphDialog.accept)
        self.buttonBox.rejected.connect(ParagraphDialog.reject)

        QMetaObject.connectSlotsByName(ParagraphDialog)
    # setupUi

    def retranslateUi(self, ParagraphDialog):
        ParagraphDialog.setWindowTitle(QCoreApplication.translate("ParagraphDialog", u"\u6bb5\u843d", None))
        self.indentGroupBox.setTitle(QCoreApplication.translate("ParagraphDialog", u"\u30a4\u30f3\u30c7\u30f3\u30c8", None))
        self.leftLabel.setText(QCoreApplication.translate("ParagraphDialog", u"\u5de6(&L):", None))
        self.leftLineEdit.setText(QCoreApplication.translate("ParagraphDialog", u"cm", None))
        self.rightLabel.setText(QCoreApplication.translate("ParagraphDialog", u"\u53f3(&R):", None))
        self.rightLineEdit.setText(QCoreApplication.translate("ParagraphDialog", u"cm", None))
        self.firstLineLabel.setText(QCoreApplication.translate("ParagraphDialog", u"\u6700\u521d\u306e\u884c(&F)", None))
        self.firstLineEdit.setText(QCoreApplication.translate("ParagraphDialog", u"cm", None))
        self.lineHeightGroupBox.setTitle(QCoreApplication.translate("ParagraphDialog", u"\u9593\u9694", None))
        self.label.setText(QCoreApplication.translate("ParagraphDialog", u"\u884c\u9593(&S):", None))
        self.lineHeightComboBox.setItemText(0, QCoreApplication.translate("ParagraphDialog", u"1.0", None))
        self.lineHeightComboBox.setItemText(1, QCoreApplication.translate("ParagraphDialog", u"1.15", None))
        self.lineHeightComboBox.setItemText(2, QCoreApplication.translate("ParagraphDialog", u"1.5", None))
        self.lineHeightComboBox.setItemText(3, QCoreApplication.translate("ParagraphDialog", u"2.0", None))

        self.tenPointPlusCheckBox.setText(QCoreApplication.translate("ParagraphDialog", u"\u6bb5\u843d\u5f8c\u306b\uff11\uff10\u30dd\u30a4\u30f3\u30c8\u306e\u30b9\u30da\u30fc\u30b9\u3092\u8ffd\u52a0\u3059\u308b(&A)", None))
        self.alignmentLabel.setText(QCoreApplication.translate("ParagraphDialog", u"\u6574\u5217(&A):", None))
        self.alignmentComboBox.setItemText(0, QCoreApplication.translate("ParagraphDialog", u"\u5de6", None))
        self.alignmentComboBox.setItemText(1, QCoreApplication.translate("ParagraphDialog", u"\u53f3", None))
        self.alignmentComboBox.setItemText(2, QCoreApplication.translate("ParagraphDialog", u"\u4e2d\u592e", None))
        self.alignmentComboBox.setItemText(3, QCoreApplication.translate("ParagraphDialog", u"\u4e21\u7aef\u63c3\u3048", None))

        self.tabPushButton.setText(QCoreApplication.translate("ParagraphDialog", u"\u30bf\u30d6(&T)...", None))
    # retranslateUi

