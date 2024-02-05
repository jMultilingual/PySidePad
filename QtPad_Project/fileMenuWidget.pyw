# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileMenuWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)
import images_rc

class Ui_FileMenuWidget(object):
    def setupUi(self, FileMenuWidget):
        if not FileMenuWidget.objectName():
            FileMenuWidget.setObjectName(u"FileMenuWidget")
        FileMenuWidget.resize(528, 447)
        self.horizontalLayout_2 = QHBoxLayout(FileMenuWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.newFileToolButton = QToolButton(FileMenuWidget)
        self.newFileToolButton.setObjectName(u"newFileToolButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newFileToolButton.sizePolicy().hasHeightForWidth())
        self.newFileToolButton.setSizePolicy(sizePolicy)
        self.newFileToolButton.setMinimumSize(QSize(200, 50))
        icon = QIcon()
        icon.addFile(u":/images/fileopen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newFileToolButton.setIcon(icon)
        self.newFileToolButton.setIconSize(QSize(32, 32))
        self.newFileToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.newFileToolButton)

        self.openFileToolButton = QToolButton(FileMenuWidget)
        self.openFileToolButton.setObjectName(u"openFileToolButton")
        sizePolicy.setHeightForWidth(self.openFileToolButton.sizePolicy().hasHeightForWidth())
        self.openFileToolButton.setSizePolicy(sizePolicy)
        self.openFileToolButton.setMinimumSize(QSize(200, 50))
        icon1 = QIcon()
        icon1.addFile(u":/images/Open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openFileToolButton.setIcon(icon1)
        self.openFileToolButton.setIconSize(QSize(32, 32))
        self.openFileToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.openFileToolButton)

        self.fileSaveToolButton = QToolButton(FileMenuWidget)
        self.fileSaveToolButton.setObjectName(u"fileSaveToolButton")
        sizePolicy.setHeightForWidth(self.fileSaveToolButton.sizePolicy().hasHeightForWidth())
        self.fileSaveToolButton.setSizePolicy(sizePolicy)
        self.fileSaveToolButton.setMinimumSize(QSize(200, 50))
        icon2 = QIcon()
        icon2.addFile(u":/images/filesave.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileSaveToolButton.setIcon(icon2)
        self.fileSaveToolButton.setIconSize(QSize(32, 32))
        self.fileSaveToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.fileSaveToolButton)

        self.fileSaveAsToolButton = QToolButton(FileMenuWidget)
        self.fileSaveAsToolButton.setObjectName(u"fileSaveAsToolButton")
        sizePolicy.setHeightForWidth(self.fileSaveAsToolButton.sizePolicy().hasHeightForWidth())
        self.fileSaveAsToolButton.setSizePolicy(sizePolicy)
        self.fileSaveAsToolButton.setMinimumSize(QSize(200, 50))
        icon3 = QIcon()
        icon3.addFile(u":/images/filesaveas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileSaveAsToolButton.setIcon(icon3)
        self.fileSaveAsToolButton.setIconSize(QSize(32, 32))
        self.fileSaveAsToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.fileSaveAsToolButton)

        self.printToolButton = QToolButton(FileMenuWidget)
        self.printToolButton.setObjectName(u"printToolButton")
        sizePolicy.setHeightForWidth(self.printToolButton.sizePolicy().hasHeightForWidth())
        self.printToolButton.setSizePolicy(sizePolicy)
        self.printToolButton.setMinimumSize(QSize(200, 50))
        icon4 = QIcon()
        icon4.addFile(u":/images/fileprint.png", QSize(), QIcon.Normal, QIcon.Off)
        self.printToolButton.setIcon(icon4)
        self.printToolButton.setIconSize(QSize(32, 32))
        self.printToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.printToolButton)

        self.printPreviewToolButton = QToolButton(FileMenuWidget)
        self.printPreviewToolButton.setObjectName(u"printPreviewToolButton")
        sizePolicy.setHeightForWidth(self.printPreviewToolButton.sizePolicy().hasHeightForWidth())
        self.printPreviewToolButton.setSizePolicy(sizePolicy)
        self.printPreviewToolButton.setMinimumSize(QSize(200, 50))
        icon5 = QIcon()
        icon5.addFile(u":/images/Preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.printPreviewToolButton.setIcon(icon5)
        self.printPreviewToolButton.setIconSize(QSize(32, 32))
        self.printPreviewToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.printPreviewToolButton)

        self.informationToolButton = QToolButton(FileMenuWidget)
        self.informationToolButton.setObjectName(u"informationToolButton")
        sizePolicy.setHeightForWidth(self.informationToolButton.sizePolicy().hasHeightForWidth())
        self.informationToolButton.setSizePolicy(sizePolicy)
        self.informationToolButton.setMinimumSize(QSize(200, 50))
        icon6 = QIcon()
        icon6.addFile(u":/images/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.informationToolButton.setIcon(icon6)
        self.informationToolButton.setIconSize(QSize(32, 32))
        self.informationToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.informationToolButton)

        self.closeToolButton = QToolButton(FileMenuWidget)
        self.closeToolButton.setObjectName(u"closeToolButton")
        sizePolicy.setHeightForWidth(self.closeToolButton.sizePolicy().hasHeightForWidth())
        self.closeToolButton.setSizePolicy(sizePolicy)
        self.closeToolButton.setMinimumSize(QSize(200, 50))
        icon7 = QIcon()
        icon7.addFile(u":/images/filequit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeToolButton.setIcon(icon7)
        self.closeToolButton.setIconSize(QSize(32, 32))
        self.closeToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.closeToolButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.listWidget = QListWidget(FileMenuWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(FileMenuWidget)

        QMetaObject.connectSlotsByName(FileMenuWidget)
    # setupUi

    def retranslateUi(self, FileMenuWidget):
        FileMenuWidget.setWindowTitle(QCoreApplication.translate("FileMenuWidget", u"\u30d5\u30a1\u30a4\u30eb", None))
        self.newFileToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u65b0\u898f(&N)", None))
        self.openFileToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u958b\u304f(&O)", None))
        self.fileSaveToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u4e0a\u66f8\u4fdd\u5b58(&S)", None))
        self.fileSaveAsToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u540d\u524d\u3092\u4ed8\u3051\u3066\u4fdd\u5b58(&A)", None))
        self.printToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u5370\u5237(&P)", None))
        self.printPreviewToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u5370\u5237\u30d7\u30ec\u30d3\u30e5\u30fc(&G)", None))
        self.informationToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u30d0\u30fc\u30b8\u30e7\u30f3\u60c5\u5831", None))
        self.closeToolButton.setText(QCoreApplication.translate("FileMenuWidget", u"\u9589\u3058\u308b(&Q)", None))
    # retranslateUi

