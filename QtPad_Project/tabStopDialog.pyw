# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabStopDialog.ui'
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
    QGridLayout, QGroupBox, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TabStopDialog(object):
    def setupUi(self, TabStopDialog):
        if not TabStopDialog.objectName():
            TabStopDialog.setObjectName(u"TabStopDialog")
        TabStopDialog.resize(344, 289)
        self.gridLayout = QGridLayout(TabStopDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabStopGroupBox = QGroupBox(TabStopDialog)
        self.tabStopGroupBox.setObjectName(u"tabStopGroupBox")
        self.gridLayout_2 = QGridLayout(self.tabStopGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabStopLineEdit = QLineEdit(self.tabStopGroupBox)
        self.tabStopLineEdit.setObjectName(u"tabStopLineEdit")

        self.verticalLayout.addWidget(self.tabStopLineEdit)

        self.tabStopListWidget = QListWidget(self.tabStopGroupBox)
        self.tabStopListWidget.setObjectName(u"tabStopListWidget")

        self.verticalLayout.addWidget(self.tabStopListWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabStopSetButton = QPushButton(self.tabStopGroupBox)
        self.tabStopSetButton.setObjectName(u"tabStopSetButton")
        self.tabStopSetButton.setEnabled(False)
        self.tabStopSetButton.setCheckable(False)

        self.horizontalLayout.addWidget(self.tabStopSetButton)

        self.tabStopClearButton = QPushButton(self.tabStopGroupBox)
        self.tabStopClearButton.setObjectName(u"tabStopClearButton")
        self.tabStopClearButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.tabStopClearButton)

        self.tabStopAllClearButton = QPushButton(self.tabStopGroupBox)
        self.tabStopAllClearButton.setObjectName(u"tabStopAllClearButton")
        self.tabStopAllClearButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.tabStopAllClearButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.tabStopGroupBox)

        self.buttonBox = QDialogButtonBox(TabStopDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(TabStopDialog)
        self.buttonBox.accepted.connect(TabStopDialog.accept)
        self.buttonBox.rejected.connect(TabStopDialog.reject)

        QMetaObject.connectSlotsByName(TabStopDialog)
    # setupUi

    def retranslateUi(self, TabStopDialog):
        TabStopDialog.setWindowTitle(QCoreApplication.translate("TabStopDialog", u"Dialog", None))
        self.tabStopGroupBox.setTitle(QCoreApplication.translate("TabStopDialog", u"\u30bf\u30d6\u306e\u505c\u6b62\u4f4d\u7f6e(&T)", None))
        self.tabStopSetButton.setText(QCoreApplication.translate("TabStopDialog", u"\u8a2d\u5b9a(&S)", None))
        self.tabStopClearButton.setText(QCoreApplication.translate("TabStopDialog", u"\u30af\u30ea\u30a2(&C)", None))
        self.tabStopAllClearButton.setText(QCoreApplication.translate("TabStopDialog", u"\u3059\u3079\u3066\u30af\u30ea\u30a2(&L)", None))
    # retranslateUi

