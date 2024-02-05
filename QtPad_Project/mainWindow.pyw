# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
    QFrame, QGraphicsView, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QSizePolicy,
    QStatusBar, QTabWidget, QToolButton, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 911)
        self.action_I = QAction(MainWindow)
        self.action_I.setObjectName(u"action_I")
        self.action_I.setCheckable(True)
        self.action_I.setMenuRole(QAction.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainVLayout = QVBoxLayout()
        self.mainVLayout.setSpacing(0)
        self.mainVLayout.setObjectName(u"mainVLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(849, 150))
        self.tabWidget.setMaximumSize(QSize(16777215, 150))
        self.fileTab = QWidget()
        self.fileTab.setObjectName(u"fileTab")
        self.tabWidget.addTab(self.fileTab, "")
        self.homeTab = QWidget()
        self.homeTab.setObjectName(u"homeTab")
        self.horizontalLayout = QHBoxLayout(self.homeTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clipboardGridLayout = QGridLayout()
        self.clipboardGridLayout.setObjectName(u"clipboardGridLayout")
        self.clipboardLabel = QLabel(self.homeTab)
        self.clipboardLabel.setObjectName(u"clipboardLabel")
        self.clipboardLabel.setAlignment(Qt.AlignCenter)

        self.clipboardGridLayout.addWidget(self.clipboardLabel, 2, 0, 1, 2)

        self.pastePushIconButton = QToolButton(self.homeTab)
        self.pastePushIconButton.setObjectName(u"pastePushIconButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pastePushIconButton.sizePolicy().hasHeightForWidth())
        self.pastePushIconButton.setSizePolicy(sizePolicy1)
        self.pastePushIconButton.setFocusPolicy(Qt.NoFocus)
        self.pastePushIconButton.setStyleSheet(u"QToolButton {background:url(:/images/paste.png) center no-repeat}")
        self.pastePushIconButton.setAutoRaise(True)

        self.clipboardGridLayout.addWidget(self.pastePushIconButton, 0, 0, 1, 1)

        self.cutToolButton = QToolButton(self.homeTab)
        self.cutToolButton.setObjectName(u"cutToolButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cutToolButton.sizePolicy().hasHeightForWidth())
        self.cutToolButton.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamilies([u"Meiryo UI"])
        font.setPointSize(9)
        self.cutToolButton.setFont(font)
        self.cutToolButton.setFocusPolicy(Qt.NoFocus)
        self.cutToolButton.setStyleSheet(u"QToolButton{background: url(:/images/cut.png) left no-repeat}")
        self.cutToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.cutToolButton.setAutoRaise(True)

        self.clipboardGridLayout.addWidget(self.cutToolButton, 0, 1, 1, 1)

        self.copyToolButton = QToolButton(self.homeTab)
        self.copyToolButton.setObjectName(u"copyToolButton")
        sizePolicy2.setHeightForWidth(self.copyToolButton.sizePolicy().hasHeightForWidth())
        self.copyToolButton.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"Meiryo UI"])
        self.copyToolButton.setFont(font1)
        self.copyToolButton.setFocusPolicy(Qt.NoFocus)
        self.copyToolButton.setStyleSheet(u"QToolButton{background:url(:/images/copy.png) left no-repeat}")
        self.copyToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.copyToolButton.setAutoRaise(True)

        self.clipboardGridLayout.addWidget(self.copyToolButton, 1, 1, 1, 1)

        self.pasteToolButton = QToolButton(self.homeTab)
        self.pasteToolButton.setObjectName(u"pasteToolButton")
        sizePolicy2.setHeightForWidth(self.pasteToolButton.sizePolicy().hasHeightForWidth())
        self.pasteToolButton.setSizePolicy(sizePolicy2)
        self.pasteToolButton.setFont(font1)
        self.pasteToolButton.setFocusPolicy(Qt.NoFocus)
        self.pasteToolButton.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.pasteToolButton.setAutoRaise(True)

        self.clipboardGridLayout.addWidget(self.pasteToolButton, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.clipboardGridLayout)

        self.fontVBoxLayout = QVBoxLayout()
        self.fontVBoxLayout.setObjectName(u"fontVBoxLayout")
        self.fontFamilyHBoxLayout = QHBoxLayout()
        self.fontFamilyHBoxLayout.setObjectName(u"fontFamilyHBoxLayout")
        self.fontComboBox = QFontComboBox(self.homeTab)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setFocusPolicy(Qt.NoFocus)

        self.fontFamilyHBoxLayout.addWidget(self.fontComboBox)

        self.fontPointSizeComboBox = QComboBox(self.homeTab)
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.addItem("")
        self.fontPointSizeComboBox.setObjectName(u"fontPointSizeComboBox")
        self.fontPointSizeComboBox.setFocusPolicy(Qt.NoFocus)

        self.fontFamilyHBoxLayout.addWidget(self.fontPointSizeComboBox)

        self.fontUpperToolButton = QToolButton(self.homeTab)
        self.fontUpperToolButton.setObjectName(u"fontUpperToolButton")
        self.fontUpperToolButton.setFocusPolicy(Qt.NoFocus)
        self.fontUpperToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-size-up.png) center no-repeat}")
        self.fontUpperToolButton.setAutoRaise(True)

        self.fontFamilyHBoxLayout.addWidget(self.fontUpperToolButton)

        self.fontDownerToolButton = QToolButton(self.homeTab)
        self.fontDownerToolButton.setObjectName(u"fontDownerToolButton")
        self.fontDownerToolButton.setFocusPolicy(Qt.NoFocus)
        self.fontDownerToolButton.setStyleSheet(u"QToolButton{background: url(:/images/edit-size-down.png) center no-repeat}")
        self.fontDownerToolButton.setAutoRaise(True)

        self.fontFamilyHBoxLayout.addWidget(self.fontDownerToolButton)


        self.fontVBoxLayout.addLayout(self.fontFamilyHBoxLayout)

        self.charFormatHorizontalLayout = QHBoxLayout()
        self.charFormatHorizontalLayout.setObjectName(u"charFormatHorizontalLayout")
        self.boldToolButton = QToolButton(self.homeTab)
        self.boldToolButton.setObjectName(u"boldToolButton")
        self.boldToolButton.setFocusPolicy(Qt.NoFocus)
        self.boldToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-bold.png) center no-repeat}")
        self.boldToolButton.setCheckable(True)
        self.boldToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.boldToolButton)

        self.italicToolButton = QToolButton(self.homeTab)
        self.italicToolButton.setObjectName(u"italicToolButton")
        self.italicToolButton.setFocusPolicy(Qt.NoFocus)
        self.italicToolButton.setStyleSheet(u"QToolButton{background: url(:/images/edit-italic.png) center no-repeat}")
        self.italicToolButton.setCheckable(True)
        self.italicToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.italicToolButton)

        self.underlineToolButton = QToolButton(self.homeTab)
        self.underlineToolButton.setObjectName(u"underlineToolButton")
        self.underlineToolButton.setFocusPolicy(Qt.NoFocus)
        self.underlineToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-underline.png) center no-repeat}")
        self.underlineToolButton.setCheckable(True)
        self.underlineToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.underlineToolButton)

        self.strikeOutToolButton = QToolButton(self.homeTab)
        self.strikeOutToolButton.setObjectName(u"strikeOutToolButton")
        self.strikeOutToolButton.setFocusPolicy(Qt.NoFocus)
        self.strikeOutToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-strike.png) center no-repeat}")
        self.strikeOutToolButton.setCheckable(True)
        self.strikeOutToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.strikeOutToolButton)

        self.subScriptToolButton = QToolButton(self.homeTab)
        self.subScriptToolButton.setObjectName(u"subScriptToolButton")
        self.subScriptToolButton.setFocusPolicy(Qt.NoFocus)
        self.subScriptToolButton.setStyleSheet(u"QToolButton{background: url(:/images/edit-subscript.png) center no-repeat}")
        self.subScriptToolButton.setCheckable(True)
        self.subScriptToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.subScriptToolButton)

        self.superScriptToolButton = QToolButton(self.homeTab)
        self.superScriptToolButton.setObjectName(u"superScriptToolButton")
        self.superScriptToolButton.setFocusPolicy(Qt.NoFocus)
        self.superScriptToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-superscript.png) center no-repeat}")
        self.superScriptToolButton.setCheckable(True)
        self.superScriptToolButton.setAutoRaise(True)

        self.charFormatHorizontalLayout.addWidget(self.superScriptToolButton)

        self.fontColorHBoxLayout = QHBoxLayout()
        self.fontColorHBoxLayout.setSpacing(0)
        self.fontColorHBoxLayout.setObjectName(u"fontColorHBoxLayout")
        self.fontColorHBoxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.textColorToolButton = QToolButton(self.homeTab)
        self.textColorToolButton.setObjectName(u"textColorToolButton")
        self.textColorToolButton.setAutoRaise(False)

        self.fontColorHBoxLayout.addWidget(self.textColorToolButton)

        self.textColorMenuToolButton = QToolButton(self.homeTab)
        self.textColorMenuToolButton.setObjectName(u"textColorMenuToolButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textColorMenuToolButton.sizePolicy().hasHeightForWidth())
        self.textColorMenuToolButton.setSizePolicy(sizePolicy3)
        self.textColorMenuToolButton.setStyleSheet(u"")
        self.textColorMenuToolButton.setCheckable(True)
        self.textColorMenuToolButton.setPopupMode(QToolButton.InstantPopup)
        self.textColorMenuToolButton.setAutoRaise(True)
        self.textColorMenuToolButton.setArrowType(Qt.NoArrow)

        self.fontColorHBoxLayout.addWidget(self.textColorMenuToolButton)


        self.charFormatHorizontalLayout.addLayout(self.fontColorHBoxLayout)

        self.fontBackgroundColorHBoxLayout = QHBoxLayout()
        self.fontBackgroundColorHBoxLayout.setSpacing(0)
        self.fontBackgroundColorHBoxLayout.setObjectName(u"fontBackgroundColorHBoxLayout")
        self.backgroundColorToolButton = QToolButton(self.homeTab)
        self.backgroundColorToolButton.setObjectName(u"backgroundColorToolButton")
        self.backgroundColorToolButton.setAutoRaise(False)

        self.fontBackgroundColorHBoxLayout.addWidget(self.backgroundColorToolButton)

        self.backgroundColorMenuToolButton = QToolButton(self.homeTab)
        self.backgroundColorMenuToolButton.setObjectName(u"backgroundColorMenuToolButton")
        self.backgroundColorMenuToolButton.setStyleSheet(u"")
        self.backgroundColorMenuToolButton.setCheckable(True)
        self.backgroundColorMenuToolButton.setPopupMode(QToolButton.InstantPopup)
        self.backgroundColorMenuToolButton.setAutoRaise(True)
        self.backgroundColorMenuToolButton.setArrowType(Qt.NoArrow)

        self.fontBackgroundColorHBoxLayout.addWidget(self.backgroundColorMenuToolButton)


        self.charFormatHorizontalLayout.addLayout(self.fontBackgroundColorHBoxLayout)


        self.fontVBoxLayout.addLayout(self.charFormatHorizontalLayout)

        self.fontLabel = QLabel(self.homeTab)
        self.fontLabel.setObjectName(u"fontLabel")
        self.fontLabel.setAlignment(Qt.AlignCenter)

        self.fontVBoxLayout.addWidget(self.fontLabel)


        self.horizontalLayout.addLayout(self.fontVBoxLayout)

        self.paragraphVBoxLayout = QVBoxLayout()
        self.paragraphVBoxLayout.setObjectName(u"paragraphVBoxLayout")
        self.indentHBoxLayout = QHBoxLayout()
        self.indentHBoxLayout.setObjectName(u"indentHBoxLayout")
        self.indentToolButton = QToolButton(self.homeTab)
        self.indentToolButton.setObjectName(u"indentToolButton")
        self.indentToolButton.setFocusPolicy(Qt.NoFocus)
        self.indentToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-indent.png) center no-repeat}")
        self.indentToolButton.setAutoRaise(True)

        self.indentHBoxLayout.addWidget(self.indentToolButton)

        self.unIndentToolButton = QToolButton(self.homeTab)
        self.unIndentToolButton.setObjectName(u"unIndentToolButton")
        self.unIndentToolButton.setFocusPolicy(Qt.NoFocus)
        self.unIndentToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-indent.png) center no-repeat}")
        self.unIndentToolButton.setAutoRaise(True)

        self.indentHBoxLayout.addWidget(self.unIndentToolButton)

        self.listToolButton = QToolButton(self.homeTab)
        self.listToolButton.setObjectName(u"listToolButton")
        self.listToolButton.setFocusPolicy(Qt.NoFocus)
        self.listToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-list.png) center no-repeat}")
        self.listToolButton.setPopupMode(QToolButton.InstantPopup)
        self.listToolButton.setAutoRaise(True)

        self.indentHBoxLayout.addWidget(self.listToolButton)

        self.lineHeightToolButton = QToolButton(self.homeTab)
        self.lineHeightToolButton.setObjectName(u"lineHeightToolButton")
        self.lineHeightToolButton.setFocusPolicy(Qt.NoFocus)
        self.lineHeightToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-line-spacing.png) center no-repeat}")
        self.lineHeightToolButton.setAutoRaise(True)

        self.indentHBoxLayout.addWidget(self.lineHeightToolButton)


        self.paragraphVBoxLayout.addLayout(self.indentHBoxLayout)

        self.alignmentHBoxLayout = QHBoxLayout()
        self.alignmentHBoxLayout.setObjectName(u"alignmentHBoxLayout")
        self.alignLeftToolButton = QToolButton(self.homeTab)
        self.alignLeftToolButton.setObjectName(u"alignLeftToolButton")
        self.alignLeftToolButton.setFocusPolicy(Qt.NoFocus)
        self.alignLeftToolButton.setStyleSheet(u"QToolButton { background : url(:/images/edit-alignment.png) center no-repeat}")
        self.alignLeftToolButton.setCheckable(True)
        self.alignLeftToolButton.setChecked(True)
        self.alignLeftToolButton.setAutoRaise(True)

        self.alignmentHBoxLayout.addWidget(self.alignLeftToolButton)

        self.alignCenterToolButton = QToolButton(self.homeTab)
        self.alignCenterToolButton.setObjectName(u"alignCenterToolButton")
        self.alignCenterToolButton.setFocusPolicy(Qt.NoFocus)
        self.alignCenterToolButton.setStyleSheet(u"QToolButton{background: url(:/images/edit-alignment-center.png) center no-repeat}")
        self.alignCenterToolButton.setCheckable(True)
        self.alignCenterToolButton.setAutoRaise(True)

        self.alignmentHBoxLayout.addWidget(self.alignCenterToolButton)

        self.alignRightToolButton = QToolButton(self.homeTab)
        self.alignRightToolButton.setObjectName(u"alignRightToolButton")
        self.alignRightToolButton.setFocusPolicy(Qt.NoFocus)
        self.alignRightToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-alignment-right.png) center no-repeat}")
        self.alignRightToolButton.setCheckable(True)
        self.alignRightToolButton.setAutoRaise(True)

        self.alignmentHBoxLayout.addWidget(self.alignRightToolButton)

        self.alignJustifyToolButton = QToolButton(self.homeTab)
        self.alignJustifyToolButton.setObjectName(u"alignJustifyToolButton")
        self.alignJustifyToolButton.setFocusPolicy(Qt.NoFocus)
        self.alignJustifyToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-alignment-justify.png) center no-repeat}")
        self.alignJustifyToolButton.setCheckable(True)
        self.alignJustifyToolButton.setAutoRaise(True)

        self.alignmentHBoxLayout.addWidget(self.alignJustifyToolButton)

        self.paragraphDialogToolButton = QToolButton(self.homeTab)
        self.paragraphDialogToolButton.setObjectName(u"paragraphDialogToolButton")
        self.paragraphDialogToolButton.setFocusPolicy(Qt.NoFocus)
        self.paragraphDialogToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-pilcrow.png) center no-repeat}")
        self.paragraphDialogToolButton.setAutoRaise(True)

        self.alignmentHBoxLayout.addWidget(self.paragraphDialogToolButton)


        self.paragraphVBoxLayout.addLayout(self.alignmentHBoxLayout)

        self.paragraphLabel = QLabel(self.homeTab)
        self.paragraphLabel.setObjectName(u"paragraphLabel")
        self.paragraphLabel.setAlignment(Qt.AlignCenter)

        self.paragraphVBoxLayout.addWidget(self.paragraphLabel)


        self.horizontalLayout.addLayout(self.paragraphVBoxLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.imageToolButton = QToolButton(self.homeTab)
        self.imageToolButton.setObjectName(u"imageToolButton")
        sizePolicy1.setHeightForWidth(self.imageToolButton.sizePolicy().hasHeightForWidth())
        self.imageToolButton.setSizePolicy(sizePolicy1)
        self.imageToolButton.setMaximumSize(QSize(30, 30))
        self.imageToolButton.setFocusPolicy(Qt.NoFocus)
        self.imageToolButton.setStyleSheet(u"QToolButton{background:url(:/images/image_header.png) center no-repeat}")
        self.imageToolButton.setAutoRaise(True)

        self.verticalLayout.addWidget(self.imageToolButton)

        self.imageMenuToolButton = QToolButton(self.homeTab)
        self.imageMenuToolButton.setObjectName(u"imageMenuToolButton")
        sizePolicy1.setHeightForWidth(self.imageMenuToolButton.sizePolicy().hasHeightForWidth())
        self.imageMenuToolButton.setSizePolicy(sizePolicy1)
        self.imageMenuToolButton.setMinimumSize(QSize(30, 30))
        self.imageMenuToolButton.setMaximumSize(QSize(30, 30))
        self.imageMenuToolButton.setPopupMode(QToolButton.InstantPopup)
        self.imageMenuToolButton.setAutoRaise(True)
        self.imageMenuToolButton.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.imageMenuToolButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.timeToolButton = QToolButton(self.homeTab)
        self.timeToolButton.setObjectName(u"timeToolButton")
        sizePolicy1.setHeightForWidth(self.timeToolButton.sizePolicy().hasHeightForWidth())
        self.timeToolButton.setSizePolicy(sizePolicy1)
        self.timeToolButton.setMaximumSize(QSize(30, 30))
        self.timeToolButton.setFocusPolicy(Qt.NoFocus)
        self.timeToolButton.setStyleSheet(u"QToolButton{background:url(:/images/Time.png) center no-repeat}")
        self.timeToolButton.setAutoRaise(True)

        self.horizontalLayout_2.addWidget(self.timeToolButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.insertLabel = QLabel(self.homeTab)
        self.insertLabel.setObjectName(u"insertLabel")
        sizePolicy1.setHeightForWidth(self.insertLabel.sizePolicy().hasHeightForWidth())
        self.insertLabel.setSizePolicy(sizePolicy1)
        self.insertLabel.setMaximumSize(QSize(200, 30))
        self.insertLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.insertLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.searchVBoxLayout = QVBoxLayout()
        self.searchVBoxLayout.setObjectName(u"searchVBoxLayout")
        self.searchToolButton = QToolButton(self.homeTab)
        self.searchToolButton.setObjectName(u"searchToolButton")
        self.searchToolButton.setFocusPolicy(Qt.NoFocus)
        self.searchToolButton.setStyleSheet(u"QToolButton{background:url(:/images/Find.png) center no-repeat}")
        self.searchToolButton.setAutoRaise(True)

        self.searchVBoxLayout.addWidget(self.searchToolButton)

        self.replaceToolButton = QToolButton(self.homeTab)
        self.replaceToolButton.setObjectName(u"replaceToolButton")
        self.replaceToolButton.setFocusPolicy(Qt.NoFocus)
        self.replaceToolButton.setStyleSheet(u"QToolButton{background:url(:/images/edit-replace.png) center no-repeat}")
        self.replaceToolButton.setAutoRaise(True)

        self.searchVBoxLayout.addWidget(self.replaceToolButton)

        self.allSelectionToolButton = QToolButton(self.homeTab)
        self.allSelectionToolButton.setObjectName(u"allSelectionToolButton")
        self.allSelectionToolButton.setFocusPolicy(Qt.NoFocus)
        self.allSelectionToolButton.setStyleSheet(u"QToolButton{background:url(:/images/selection-select.png) center no-repeat}")
        self.allSelectionToolButton.setAutoRaise(True)

        self.searchVBoxLayout.addWidget(self.allSelectionToolButton)

        self.editLabel = QLabel(self.homeTab)
        self.editLabel.setObjectName(u"editLabel")
        self.editLabel.setAlignment(Qt.AlignCenter)

        self.searchVBoxLayout.addWidget(self.editLabel)


        self.horizontalLayout.addLayout(self.searchVBoxLayout)

        self.tabWidget.addTab(self.homeTab, "")
        self.displayTab = QWidget()
        self.displayTab.setObjectName(u"displayTab")
        self.horizontalLayout_3 = QHBoxLayout(self.displayTab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zoomVerticalLayout = QVBoxLayout()
        self.zoomVerticalLayout.setObjectName(u"zoomVerticalLayout")
        self.zoomHorizontalLayout = QHBoxLayout()
        self.zoomHorizontalLayout.setObjectName(u"zoomHorizontalLayout")
        self.zoomInToolButton = QToolButton(self.displayTab)
        self.zoomInToolButton.setObjectName(u"zoomInToolButton")
        sizePolicy2.setHeightForWidth(self.zoomInToolButton.sizePolicy().hasHeightForWidth())
        self.zoomInToolButton.setSizePolicy(sizePolicy2)
        self.zoomInToolButton.setStyleSheet(u"QToolButton{background:url(:/images/magnifier-zoom-in.png) left no-repeat}")
        self.zoomInToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.zoomInToolButton.setAutoRaise(True)

        self.zoomHorizontalLayout.addWidget(self.zoomInToolButton)

        self.zoomOutToolButton = QToolButton(self.displayTab)
        self.zoomOutToolButton.setObjectName(u"zoomOutToolButton")
        sizePolicy2.setHeightForWidth(self.zoomOutToolButton.sizePolicy().hasHeightForWidth())
        self.zoomOutToolButton.setSizePolicy(sizePolicy2)
        self.zoomOutToolButton.setStyleSheet(u"QToolButton{background:url(:/images/magnifier-zoom-out.png) left no-repeat}")
        self.zoomOutToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.zoomOutToolButton.setAutoRaise(True)

        self.zoomHorizontalLayout.addWidget(self.zoomOutToolButton)

        self.zoomAdjustToolButton = QToolButton(self.displayTab)
        self.zoomAdjustToolButton.setObjectName(u"zoomAdjustToolButton")
        sizePolicy2.setHeightForWidth(self.zoomAdjustToolButton.sizePolicy().hasHeightForWidth())
        self.zoomAdjustToolButton.setSizePolicy(sizePolicy2)
        self.zoomAdjustToolButton.setStyleSheet(u"QToolButton{background:url(:/images/magnifier-zoom-actual-equal.png) left no-repeat}")
        self.zoomAdjustToolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.zoomAdjustToolButton.setAutoRaise(True)

        self.zoomHorizontalLayout.addWidget(self.zoomAdjustToolButton)


        self.zoomVerticalLayout.addLayout(self.zoomHorizontalLayout)

        self.zoomLabel = QLabel(self.displayTab)
        self.zoomLabel.setObjectName(u"zoomLabel")
        self.zoomLabel.setAlignment(Qt.AlignCenter)

        self.zoomVerticalLayout.addWidget(self.zoomLabel)


        self.horizontalLayout_3.addLayout(self.zoomVerticalLayout)

        self.displayVerticalLineLeft = QFrame(self.displayTab)
        self.displayVerticalLineLeft.setObjectName(u"displayVerticalLineLeft")
        self.displayVerticalLineLeft.setFrameShape(QFrame.VLine)
        self.displayVerticalLineLeft.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.displayVerticalLineLeft)

        self.visibleUnvisibleVBoxLayout = QVBoxLayout()
        self.visibleUnvisibleVBoxLayout.setObjectName(u"visibleUnvisibleVBoxLayout")
        self.rulerCheckBox = QCheckBox(self.displayTab)
        self.rulerCheckBox.setObjectName(u"rulerCheckBox")
        self.rulerCheckBox.setChecked(True)

        self.visibleUnvisibleVBoxLayout.addWidget(self.rulerCheckBox)

        self.statusBarCheckBox = QCheckBox(self.displayTab)
        self.statusBarCheckBox.setObjectName(u"statusBarCheckBox")
        self.statusBarCheckBox.setChecked(True)

        self.visibleUnvisibleVBoxLayout.addWidget(self.statusBarCheckBox)

        self.visibleOrUnvisibleLabel = QLabel(self.displayTab)
        self.visibleOrUnvisibleLabel.setObjectName(u"visibleOrUnvisibleLabel")
        self.visibleOrUnvisibleLabel.setAlignment(Qt.AlignCenter)

        self.visibleUnvisibleVBoxLayout.addWidget(self.visibleOrUnvisibleLabel)


        self.horizontalLayout_3.addLayout(self.visibleUnvisibleVBoxLayout)

        self.displayVerticalLineRight = QFrame(self.displayTab)
        self.displayVerticalLineRight.setObjectName(u"displayVerticalLineRight")
        self.displayVerticalLineRight.setFrameShape(QFrame.VLine)
        self.displayVerticalLineRight.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.displayVerticalLineRight)

        self.settingsVBoxLayout = QVBoxLayout()
        self.settingsVBoxLayout.setObjectName(u"settingsVBoxLayout")
        self.wrapToolButton = QToolButton(self.displayTab)
        self.wrapToolButton.setObjectName(u"wrapToolButton")
        sizePolicy2.setHeightForWidth(self.wrapToolButton.sizePolicy().hasHeightForWidth())
        self.wrapToolButton.setSizePolicy(sizePolicy2)
        self.wrapToolButton.setStyleSheet(u"QToolButton {background: url(:/images/wrapping.png) left no-repeat}")

        self.settingsVBoxLayout.addWidget(self.wrapToolButton)

        self.unitToolButton = QToolButton(self.displayTab)
        self.unitToolButton.setObjectName(u"unitToolButton")
        sizePolicy2.setHeightForWidth(self.unitToolButton.sizePolicy().hasHeightForWidth())
        self.unitToolButton.setSizePolicy(sizePolicy2)
        self.unitToolButton.setStyleSheet(u"QToolButton{background:url(:/images/Units.png) left no-repeat}")

        self.settingsVBoxLayout.addWidget(self.unitToolButton)

        self.settingsLabel = QLabel(self.displayTab)
        self.settingsLabel.setObjectName(u"settingsLabel")
        self.settingsLabel.setAlignment(Qt.AlignCenter)

        self.settingsVBoxLayout.addWidget(self.settingsLabel)


        self.horizontalLayout_3.addLayout(self.settingsVBoxLayout)

        self.tabWidget.addTab(self.displayTab, "")

        self.mainVLayout.addWidget(self.tabWidget)

        self.rulerView = QGraphicsView(self.centralwidget)
        self.rulerView.setObjectName(u"rulerView")
        self.rulerView.setMaximumSize(QSize(16777215, 50))
        self.rulerView.setFocusPolicy(Qt.NoFocus)
        self.rulerView.setFrameShape(QFrame.NoFrame)
        self.rulerView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rulerView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.mainVLayout.addWidget(self.rulerView)

        self.mainView = QGraphicsView(self.centralwidget)
        self.mainView.setObjectName(u"mainView")
        self.mainView.setFocusPolicy(Qt.StrongFocus)
        self.mainView.setFrameShape(QFrame.NoFrame)

        self.mainVLayout.addWidget(self.mainView)


        self.verticalLayout_3.addLayout(self.mainVLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_I.setText(QCoreApplication.translate("MainWindow", u"\u30a4\u30f3\u30c1(&I)", None))
#if QT_CONFIG(shortcut)
        self.action_I.setShortcut(QCoreApplication.translate("MainWindow", u"I", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fileTab), QCoreApplication.translate("MainWindow", u"\u30d5\u30a1\u30a4\u30eb", None))
        self.clipboardLabel.setText(QCoreApplication.translate("MainWindow", u"\u30af\u30ea\u30c3\u30d7\u30dc\u30fc\u30c9", None))
        self.pastePushIconButton.setText("")
        self.cutToolButton.setText(QCoreApplication.translate("MainWindow", u"\u5207\u308a\u53d6\u308a", None))
        self.copyToolButton.setText(QCoreApplication.translate("MainWindow", u"\u30b3\u30d4\u30fc", None))
        self.pasteToolButton.setText(QCoreApplication.translate("MainWindow", u"\u8cbc\u308a\u4ed8\u3051", None))
        self.fontPointSizeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.fontPointSizeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"9", None))
        self.fontPointSizeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"10", None))
        self.fontPointSizeComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"11", None))
        self.fontPointSizeComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"12", None))
        self.fontPointSizeComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"14", None))
        self.fontPointSizeComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"16", None))
        self.fontPointSizeComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"18", None))
        self.fontPointSizeComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"20", None))
        self.fontPointSizeComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"22", None))
        self.fontPointSizeComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"24", None))
        self.fontPointSizeComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"26", None))
        self.fontPointSizeComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"28", None))
        self.fontPointSizeComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"36", None))
        self.fontPointSizeComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"48", None))
        self.fontPointSizeComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"72", None))

        self.fontUpperToolButton.setText("")
        self.fontDownerToolButton.setText("")
        self.boldToolButton.setText("")
        self.italicToolButton.setText("")
        self.underlineToolButton.setText("")
        self.strikeOutToolButton.setText("")
        self.subScriptToolButton.setText("")
        self.superScriptToolButton.setText("")
        self.textColorToolButton.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.textColorMenuToolButton.setText("")
        self.backgroundColorToolButton.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.backgroundColorMenuToolButton.setText("")
        self.fontLabel.setText(QCoreApplication.translate("MainWindow", u"\u30d5\u30a9\u30f3\u30c8", None))
        self.indentToolButton.setText("")
        self.unIndentToolButton.setText("")
        self.listToolButton.setText("")
        self.lineHeightToolButton.setText("")
        self.alignLeftToolButton.setText("")
        self.alignCenterToolButton.setText("")
        self.alignRightToolButton.setText("")
        self.alignJustifyToolButton.setText("")
        self.paragraphDialogToolButton.setText("")
        self.paragraphLabel.setText(QCoreApplication.translate("MainWindow", u"\u6bb5\u843d", None))
        self.imageToolButton.setText("")
        self.imageMenuToolButton.setText("")
        self.timeToolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.insertLabel.setText(QCoreApplication.translate("MainWindow", u"\u633f\u5165", None))
        self.searchToolButton.setText("")
        self.replaceToolButton.setText("")
        self.allSelectionToolButton.setText("")
        self.editLabel.setText(QCoreApplication.translate("MainWindow", u"\u7de8\u96c6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), QCoreApplication.translate("MainWindow", u"\u30db\u30fc\u30e0", None))
        self.zoomInToolButton.setText(QCoreApplication.translate("MainWindow", u"\u62e1\u5927", None))
        self.zoomOutToolButton.setText(QCoreApplication.translate("MainWindow", u"\u7e2e\u5c0f", None))
        self.zoomAdjustToolButton.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.zoomLabel.setText(QCoreApplication.translate("MainWindow", u"\u30ba\u30fc\u30e0", None))
        self.rulerCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u30eb\u30fc\u30e9\u2015", None))
        self.statusBarCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u30b9\u30c6\u30fc\u30bf\u30b9\u30d0\u30fc", None))
        self.visibleOrUnvisibleLabel.setText(QCoreApplication.translate("MainWindow", u"\u8868\u793a\u307e\u305f\u306f\u975e\u8868\u793a", None))
        self.wrapToolButton.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u7aef\u3067\u306e\u6298\u308a\u8fd4\u3057", None))
        self.unitToolButton.setText(QCoreApplication.translate("MainWindow", u"\u5358\u4f4d", None))
        self.settingsLabel.setText(QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.displayTab), QCoreApplication.translate("MainWindow", u"\u8868\u793a", None))
    # retranslateUi

