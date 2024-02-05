from enums import *

class ImageSizeChangeDialog(QDialog, Ui_ImageSizeChangeDialog):#new↓

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

        self.checkBox.toggled.connect(self.block)

    def block(self, bool):

    
        self.hSpinBox.blockSignals(not bool)
        self.vSpinBox.blockSignals(not bool)

class PasteDialog(QDialog, Ui_PasteDialog):
    Text = "テキスト"
    def __init__(self, edit, parent=None):
        super().__init__(parent)

        self.edit = edit
        self.setupUi(self)

        self.listWidget.itemClicked.connect(
            self.showResultMessage
            )

    def showResultMessage(self, item):
        if item.text() == PasteDialog.Text:
            p = QPixmap(
                ":\images\clipboard-paste_image.png"
                )
            self.iconLabel.setPixmap(p)
            self.explanationLabel.setText(
                """クリップボードの内容を書式なしテキストとしてドキュメントに
                挿入します。""")

class ListFormatSelector(QWidget, Ui_ListFormatSelector):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)

class ParagraphDialog(QDialog, Ui_ParagraphDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


class TabStopDialog(QDialog, Ui_TabStopDialog):

    def __init__(self, unit = Point, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.unit = unit
        
    def acceptValue(self):
        
        item = QListWidgetItem()
        text = self.tabStopLineEdit.text()

        if self.unit == Inch:
            if "." not in text:
                text += '.00"'
                
        elif self.unit == Point:
            if "." not in text:

                text += ".00pt"
      
                
        elif self.unit ==  Milli:
            if "." not in text:
                text += ".00cm"

        elif self.unit == Pica:
            if "." not in text:
                text += ".00pi"
                
        
            
        found = self.tabStopListWidget.findItems(text, Qt.MatchFixedString)
        if not found:
            
            item.setText(text)        
            self.tabStopListWidget.addItem(item)
            self.tabStopLineEdit.clear()
            self.tabStopListWidget.sortItems()

class FindDialog(QDialog, Ui_FindDialog):
    Capture = "Qtパッド"
    Information = "ドキュメントの検索が終わりました。"

    def __init__(self, edit, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.edit = edit
        self.count = 0
        self.searchNextPushButton.clicked.connect(
            self.searchText)

    def documentFlags(self):
        flags = QTextDocument.FindFlag()
        if self.wholeWordsCheckBox.isChecked():
            flags != QTextDocument.FindWholeWords
        if self.findCaseSensitivelyCheckBox.isChecked():
            flags != QTextDocument.FindCaseSensitively
        return flags

    def setExtraSelection(self, tc):
        ex = QTextEdit.ExtraSelection()
        ex.cursor  = tc
        ex.format = QTextCharFormat()
        ex.format.setForeground(Qt.blue)
        ex.format.setBackground(Qt.yellow)
        self.edit.setExtraSelections([ex])

    def information(self):
        QMessageBox.information(
            None,
            FindDialog.Capture,
            FindDialog.Information)

    def searchText(self):
        text = self.searchTextLineEdit.text()
        if not text:
            return
        flags = self.documentFlags()
        exs = self.edit.extraSelections()
        tc = self.edit.textCursor()
        pos = tc.position()
        if exs:
            tc = self.edit.document().find(
                text, exs[0].cursor.position(), flags
                )
        else:
            tc = self.edit.document().find(
                text, tc.position(), flags
                )

        if not tc.isNull():
            if (self.count == 1
                and pos < tc.position()):
                self.information()
                self.count = -1
            self.setExtraSelection(tc)
        else:
            self.count = 1
            tc = self.edit.document().find(text, 0, flags)
            if not tc.isNull():
                if exs:
                    if exs[0].cursor == tc:
                        self.information()
                self.setExtraSelection(tc)
            else:
                self.information()

    def closeEvent(self, event):
        self.edit.setExtraSelections([])
        super().closeEvent(event)

class ReplaceDialog(Ui_ReplaceDialog, FindDialog):

    Capture = "Qtパッド"
    Information = "ドキュメントの検索が終わりました。"

    def __init__(self, edit, parent=None):
        super().__init__(edit, parent)
        self.setupUi(self)
        self.searchNextPushButton.clicked.connect(
            self.searchText
            )
        self.replaceNextPushButton.clicked.connect(
            self.replaceText
            )
        self.replaceAllPushButton.clicked.connect(
            self.allReplace
            )

    def allReplace(self):

        tc = self.edit.textCursor()
        text = self.searchTextLineEdit.text()
        if not text:
            return
        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        exs = []
        self.findRecur(
            QTextCursor(
                self.edit.document()), text, exs, flags
            )
        for ex in exs:
            ex.insertText(replacedText)

    def findRecur(self, tc, text, exs, flags):
        tc = self.edit.document().find(text,
                                       tc.selectionEnd(),
                                       flags)
        if not tc.isNull():
            exs.append(tc)
            self.findRecur(tc, text, exs, flags)
    
    def replaceText(self):
        tc = self.edit.textCursor()
        pos = tc.position()
        text = self.searchTextLineEdit.text()
        if not text:
            return
        exs = self.edit.extraSelections()
        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        if not exs:
            tc = self.edit.document().find(
                text, pos, flags
                )
            if not tc.isNull():
                self.setExtraSelection(tc)
                return
            else:
                self.information()
        else:
            tc = QTextCursor(exs[0].cursor)
            tc.insertText(replacedText)
            tc = self.edit.document().find(
                text,
                tc.position(),
                flags)
            if not tc.isNull():
                self.setExtraSelection(tc)
                return
            else:
                self.count = 1

                tc = self.edit.document().find(text,
                                               0,
                                               flags)
                if not tc.isNull():
                    
                    if (self.count == 1 and tc.position() < pos):
                        self.setExtraSelection(tc)
                    
                    else:
                        self.information()
                        self.edit.setExtraSelections([])
                else:
                    self.count = 0
                    self.information()
                    self.edit.setExtraSelections([])

    def allReplace(self):

        tc = self.edit.textCursor()
        text = self.searchTextLineEdit.text()

        if not text:
            return

        flags = self.documentFlags()
        replacedText = self.replacedLineEdit.text()
        exs = []
        self.findRecur(
            QTextCursor(
                self.edit.document()), text, exs, flags
            )
        tc.beginEditBlock()
        for ex in exs:
            ex.insertText(replacedText)
        tc.endEditBlock()

class DateAndTimeDialog(QDialog, Ui_DateAndTimeDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.init()

    def init(self):
        QLocale.setDefault(QLocale.Japanese)
        self.listWidget.clear()
        item1 = QListWidgetItem()
        dateTime = QDateTime.currentDateTime()

        item1.setText(QLocale().toString(dateTime))
        item2 = QListWidgetItem()
        item2.setText(QLocale().toString(
            dateTime, QLocale.ShortFormat)
                      )
        item3 = QListWidgetItem()
        item3.setText(
            QLocale().toString(
                dateTime, QLocale.NarrowFormat))
        item4 = QListWidgetItem()
        item4.setText(
            QLocale().toString(dateTime, "dddd, yyyy年MM月dd日 HH:mm:ss")
            )
        self.listWidget.insertItem(0, item1)
        self.listWidget.insertItem(1, item2)
        self.listWidget.insertItem(2, item3)
        self.listWidget.insertItem(3, item4)

class TextColorWidget(QWidget, Ui_TextColorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
class BackgroundColorWidget(QWidget, Ui_BackgroundColorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
