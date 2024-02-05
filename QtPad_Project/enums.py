from PySide6.QtWidgets import (
                                QApplication,
                                QMainWindow,
                                QGraphicsView,
                                QGraphicsScene,
                                QGraphicsObject,
                                QTextEdit,
                                QMenu,
                                QWidgetAction,
                                QWidget,
                                QLabel,
                                QSpinBox,
                                QStyleFactory,
                                QColorDialog,
                                QFileDialog,
                                QDialog,
                                QListWidgetItem,
                                QMessageBox, QButtonGroup,
                                QUndoView)
from PySide6.QtGui import (QPageSize,
                                               QGradient,
                                               QBrush,
                                               QTextCharFormat,
                           QTextListFormat,
                                               QTextCursor,
                           QFont,
                           QColor,
                           QPalette,
                           QPixmap,
                           QAction,
                           QIcon,
                           qRgba,
                           QImage,
                           QPyTextObject,
                           QTextFormat,
                           QTransform,
                           QTextDocument,
                           QPolygonF,
                           QPen,
                           QPainter, QUndoStack,
                           QUndoCommand,
                           QTextOption,QRegularExpressionValidator, QDoubleValidator,QValidator,QActionGroup)

from PySide6.QtCore import QRegularExpression, QSignalBlocker, QLocale, QDateTime, Qt , QRectF, QPointF,QPoint, Signal, QEvent, QSize, QSizeF, QMimeData, QDataStream, QByteArray, QIODevice
from mainWindow import Ui_MainWindow
from textColorWidget import Ui_TextColorWidget
from backgroundColorWidget import Ui_BackgroundColorWidget
from imageSizeChangeDialog import Ui_ImageSizeChangeDialog
from dateandtimedialog import Ui_DateAndTimeDialog
from replaceDialog import Ui_ReplaceDialog
from pasteDialog import Ui_PasteDialog
from findDialog import Ui_FindDialog
from textListMenu import Ui_ListFormatSelector
from paragraphDialog import Ui_ParagraphDialog
from tabStopDialog import Ui_TabStopDialog
import sys

UNDO_APPENDTEXT_ID = 1
UNDO_INPUTMETHOD_ID = 2

g_pageSizeF = QPageSize(QPageSize.A4).size(QPageSize.Point)
g_pageSize = g_pageSizeF.toSize()

KeepAnchor = QTextCursor.KeepAnchor
PreviousCharacter = QTextCursor.PreviousCharacter
NextCharacter = QTextCursor.NextCharacter
FontPropertiesSpecifiedOnly = QTextCharFormat.FontPropertiesSpecifiedOnly

AlignSuperScript = QTextCharFormat.AlignSuperScript
AlignNormal = QTextCharFormat.AlignNormal
AlignSubScript = QTextCharFormat.AlignSubScript

ImageProperty = 1
ImageObject = QTextFormat.UserObject

g_doc_leftMargin = 4.0
g_doc_rightMargin = 4.0

A4 = QPageSize.A4
Point = QPageSize.Point
Inch = QPageSize.Inch
Pica = QPageSize.Pica
Millimeter = QPageSize.Millimeter

Black = QColor(0, 0, 0)
White = QColor(255, 255, 255)
ShallowGray = QColor(204, 204, 204)
Gray = QColor(165, 165, 165)
DenseGray = QColor(102, 102, 102)
CharCoal = QColor(  51,   51,    51)
Black = QColor( 0, 0, 0)
Red = QColor(255, 0, 0)
FleshOrange = QColor(255, 102, 0)
FleshYellow = QColor(255, 255, 0)
FleshGreen = QColor(    0, 176, 80)
FleshBlue = QColor(    0,   77, 187)
FleshPurple = QColor(155,   0, 211)
CalmRed = QColor(192, 80, 77)
CalmBrown = QColor(247, 150, 70)
CalmGreen = QColor(155, 187, 89)
CalmLightBlue = QColor(75, 172, 198)
CalmBlue = QColor(79, 129, 189)
CalmPurple = QColor(128, 100, 162)
NaturalRed = QColor(209, 99, 73)
NaturalOrange = QColor(209, 144, 73)
NaturalYellow = QColor(204, 180, 0)
NaturalGreen = QColor(143, 176, 140)
NaturalBlue = QColor(100, 107, 134)
NaturalBrown = QColor(158, 124, 124)
PastelRed = QColor(221, 132, 132)
PastelOrange = QColor(243, 164, 71)
PastelYellow = QColor(223, 206, 4)
PastelGreen = QColor(165, 181, 146)
PastelBlue = QColor(128, 158, 194)
PastelPurple = QColor(156, 133, 192)

RegExpInch  = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})\"?')
RegExpcm = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})?(cm)?')
RegExppt = QRegularExpression('(?:0|[1-9]\d{0,2})(?:\.\d{1,2})?(pt)?')
RegExppi = QRegularExpression('(?:0|[1-9]\d{0,1})(?:\.\d{1,2})?(pi)?')

DeRegExpInch = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|\")?$')
DeRegExpcm = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|cm)?$')
DeRegExppt = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|pt)?$')
DeRegExppi = QRegularExpression(r'(\d+(\.\d{1,2})?)(?:pt|pi)?$')

import uuid
