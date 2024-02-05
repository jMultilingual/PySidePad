# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageSizeChangeDialog.ui'
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
    QDialogButtonBox, QFormLayout, QGridLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)
import images_rc

class Ui_ImageSizeChangeDialog(object):
    def setupUi(self, ImageSizeChangeDialog):
        if not ImageSizeChangeDialog.objectName():
            ImageSizeChangeDialog.setObjectName(u"ImageSizeChangeDialog")
        ImageSizeChangeDialog.resize(318, 120)
        self.gridLayout_2 = QGridLayout(ImageSizeChangeDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(ImageSizeChangeDialog)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ImageSizeChangeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout_2.addWidget(self.buttonBox, 0, 1, 4, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(ImageSizeChangeDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.label_3 = QLabel(ImageSizeChangeDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.hLabel = QLabel(ImageSizeChangeDialog)
        self.hLabel.setObjectName(u"hLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.hLabel)

        self.hSpinBox = QSpinBox(ImageSizeChangeDialog)
        self.hSpinBox.setObjectName(u"hSpinBox")
        self.hSpinBox.setMaximum(200)
        self.hSpinBox.setValue(100)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.hSpinBox)

        self.vLabel = QLabel(ImageSizeChangeDialog)
        self.vLabel.setObjectName(u"vLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vLabel)

        self.vSpinBox = QSpinBox(ImageSizeChangeDialog)
        self.vSpinBox.setObjectName(u"vSpinBox")
        self.vSpinBox.setMaximum(200)
        self.vSpinBox.setValue(100)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.vSpinBox)


        self.gridLayout.addLayout(self.formLayout, 0, 1, 2, 1)

        self.label_4 = QLabel(ImageSizeChangeDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{image:url(:/images/document-horizontal.png)}")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(ImageSizeChangeDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{image:url(:/images/document-vertical.png)}")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.checkBox = QCheckBox(ImageSizeChangeDialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox, 2, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.hLabel.setBuddy(self.hSpinBox)
        self.vLabel.setBuddy(self.vSpinBox)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ImageSizeChangeDialog)
        self.buttonBox.accepted.connect(ImageSizeChangeDialog.accept)
        self.buttonBox.rejected.connect(ImageSizeChangeDialog.reject)
        self.hSpinBox.valueChanged.connect(self.vSpinBox.setValue)
        self.vSpinBox.valueChanged.connect(self.hSpinBox.setValue)

        QMetaObject.connectSlotsByName(ImageSizeChangeDialog)
    # setupUi

    def retranslateUi(self, ImageSizeChangeDialog):
        ImageSizeChangeDialog.setWindowTitle(QCoreApplication.translate("ImageSizeChangeDialog", u"ImageSizeChangeDialog", None))
        self.label.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"\u5143\u306e\u753b\u50cf\u30b5\u30a4\u30ba\u3092\u57fa\u6e96\u306b\u30b5\u30a4\u30ba\u5909\u66f4\u3092\u884c\u3046", None))
        self.label_2.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"%", None))
        self.label_3.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"%", None))
        self.hLabel.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"\u6c34\u5e73\u65b9\u5411(&H):", None))
        self.vLabel.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"\u5782\u76f4\u65b9\u5411(&V):", None))
        self.label_4.setText("")
        self.label_5.setText("")
        self.checkBox.setText(QCoreApplication.translate("ImageSizeChangeDialog", u"\u7e26\u6a2a\u6bd4\u3092\u56fa\u5b9a\u3059\u308b(&L)", None))
    # retranslateUi

