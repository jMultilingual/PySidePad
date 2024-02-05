from enums import *
from ui_components import *
from components import *

class BaseUndoCommand(QUndoCommand):

    def __init__(self, doc, undotext, parent=None):
        super().__init__(undotext, parent)
        self.doc = doc
        self.textEdit = doc.parent()
        tc = self.textEdit.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
      
        bf = tc.blockFormat()
        self.blockNumber =tc.block().blockNumber()
        self.selectedText = tc.selectedText()
        self.html = tc.selection().toHtml()
        
        
    def document(self):
        return self.doc

class AppendTextUndoCommand(BaseUndoCommand):


    def __init__(self, doc, text, pos, undotext, parent=None):
        super().__init__(doc, undotext, parent)
        
        self.doc = doc
        self.text = text
        self.pos = pos
        self.firstPos = pos

        
    def __add__(self, other):

        tc = self.doc.parent().textCursor()    
        self.text += other.text
        self.pos = other.pos
        

    def id(self):

        return  UNDO_APPENDTEXT_ID
        
    def redo(self):

        tc = self.doc.parent().textCursor()
        tc.setPosition(self.firstPos)
        tc.insertText(self.text)

            

    def undo(self):

        tc = self.doc.parent().textCursor()
        tc.setPosition(self.firstPos)
        tc.setPosition(self.firstPos + len(self.text), KeepAnchor)
        tc.deleteChar()
   
    def mergeWith(self, other):

       
        
        if other:
            
            if other.id() != self.id() or  self.doc.findBlock(self.pos) != self.doc.findBlock(other.pos) or self.pos != other.pos - 1:
                return False
        else:
            return False
        
        self += other

        return True

class InputMethodTextUndoCommand(BaseUndoCommand):

    def __init__(self, doc, text, pos, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        self.doc = doc
        self.text = text
        self.pos = pos
        self.init = True
       
        
    def id(self):
        return UNDO_INPUTMETHOD_ID
        
    def redo(self):

        if not self.init:
            tc = self.doc.parent().textCursor()
            tc.setPosition(self.pos)
            tc.insertText(self.text)

        else:
            self.init = False

    def undo(self):

        tc = self.doc.parent().textCursor()
        tc.setPosition(self.pos)
        tc.movePosition(NextCharacter, KeepAnchor, len(self.text))
        tc.deleteChar()

class DeleteTextUndoCommand(BaseUndoCommand):

    def __init__(self, doc, isBack, undotext, parent=None):
        super().__init__(doc, undotext, parent)
        self.isBack = isBack

       
        self.deletedHtml = ""
        self.qb = QByteArray()
        self.labels = []
        self.qbs  = []
        self.preventDeleteLabels = []
        
    def redo(self):
        self.qbs = []
        self.preventDeleteLabels = []
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
    
        #一文字消去の場合
        if not tc.hasSelection():
            
            if self.isBack:
                charFormat = tc.charFormat()
                tc.movePosition(PreviousCharacter, KeepAnchor)    
                
            else:
                charFormat = tc.charFormat()
                tc.movePosition(NextCharacter, KeepAnchor)
                
            if tc.selectedText() == chr(0xfffc):      
                
                label = charFormat.property(ImageProperty)                    
                label.setVisible(False)
                label.setParent(None)
                out = QDataStream(self.qb, QIODevice.WriteOnly)
                label.save(out)
                self.labels.append(label)
                tc.deleteChar()              
 
                return
            self.deletedHtml = tc.selection().toHtml()
            tc.deleteChar()
        #複数文字消去の場合
        else:

            self.cleanChildWidgets(
                tc.selectionStart(),
                len(tc.selectedText()),
                0)
        
    def cleanRecursion(self, tc, selectionStart,                                                   
                                                   fr,
                                                   charsRemoved,
                                                   charsAdded):      
        
        tc = self.document().find(chr(0xfffc), selectionStart)
        
   
        if not tc.isNull():
            selectionStart = tc.selectionStart()
            selectionEnd = tc.selectionEnd()
            
            if (fr <=  selectionStart 
                 <= fr + charsRemoved ):            
                char = tc.charFormat()
                label = char.property(ImageProperty)
                label.setVisible(False)
                label.setParent(None)
                qb = QByteArray()
                out = QDataStream(qb, QIODevice.WriteOnly)
                out.writeUInt64(selectionStart)
                label.save(out)
                self.preventDeleteLabels.append(label)
                self.qbs.append(qb)
                self.cleanRecursion(tc, selectionEnd, fr, charsRemoved, charsAdded)
                
    def cleanChildWidgets(self, fr, charsRemoved, charsAdded):

        
        if charsRemoved > 1 :
            tc = self.document().parent().textCursor()
            tc.setPosition(self.selectionStart)
            tc.setPosition(self.selectionEnd, KeepAnchor)
            self.deletedHtml = tc.selection().toHtml()
         
            tc = self.document().find(chr(0xfffc), fr)
            if not tc.isNull():
                self.cleanRecursion(tc,
                                        0,
                                        fr,
                                        charsRemoved,
                                        charsAdded)
                
            tc = self.doc.parent().textCursor()
            tc.setPosition(self.selectionStart)
            tc.setPosition(self.selectionEnd, KeepAnchor)
            tc.deleteChar()
    

    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        
        if self.qbs:
            tc.insertHtml(self.deletedHtml)
         
            for qb in self.qbs:
                out = QDataStream(qb, QIODevice.ReadOnly)
                pos = out.readInt64()
                tc.setPosition(pos)
                l = ImageLabel(False, QPixmap(), QSize(32, 32), True, "QLabel{background-color: white;}", t)
                l.load(out)
                l.setVisible(True)
                l.setParent(t)
                char = tc.charFormat()
                char.setObjectType(ImageObject)
                char.setProperty(ImageProperty, l)
                tc.insertText(chr(0xfffc), char)

        else:
            tc.insertHtml(self.deletedHtml)

        
    

class CutUndoCommand(BaseUndoCommand):

    def __init__(self, doc, undotext, parent=None):
        super().__init__(doc, undotext, parent)


        t = self.doc.parent()
        #PasteUndoCommandのために。
        if self.selectionStart != self.selectionEnd:
            t.createMimeDataFromSelection() 
        self.mimeData =   t.mimeData
        
    def redo(self):
        t = self.doc.parent()
        tc =  t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

        t.cleanRecursion(tc,tc.selectionStart(),
                    tc.selectionStart(),
                    len(tc.selectedText()),
                    0)        
        
        tc.deleteChar()
        
    def undo(self):
        t = self.doc.parent()
        tc =  t.textCursor()
        tc.setPosition(self.selectionStart)
        t.insertFromMimeData(self.mimeData)
           


        
class PasteUndoCommand(CutUndoCommand):

    def __init__(self, doc, undoText, parent=None):
        super().__init__(doc, undoText, parent)     
        
    def redo(self):  
        
        t = self.doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.position() 
        super().undo()
        tc = t.textCursor()
        self.selectionEnd = tc.position()
        print(self.mimeData)
    def undo(self):
        super().redo()
        
class SetCurrentFontUndoCommand(BaseUndoCommand):

    def __init__(self, doc, font, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.font = font
        self.fonts = []
        
    def redo(self):
        
        self.fonts.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                self.fonts.append(charFont)
                charFormat.setFont(self.font,
                                   FontPropertiesSpecifiedOnly )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fonts.append(charFont)
            charFormat.setFont(self.font)
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                #SpecifiesOnlyを外すとうまくいく
                charFormat.setFont(self.fonts[i])

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFont(self.fonts[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class SetCurrentFontSizeUndoCommand(BaseUndoCommand):
    def __init__(self, doc, fontSize, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.fontSize = fontSize
        self.fontSizes = []
        
    def redo(self):
        
        self.fontSizes.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
            
                self.fontSizes.append(charFormat.fontPointSize())
                charFormat.setFontPointSize(self.fontSize)
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fontSizes.append(charFont)
            charFormat.setFontPointSize(self.fontSize)
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFormat.setFontPointSize(self.fontSizes[i])

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFontPointSize(self.fontSizes[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class CrementFontSizeUndoCommand(BaseUndoCommand):
    def __init__(self, doc,  crement, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()      
        self.fontSizes = []
        self.crement = crement

    def redo(self):
        
        self.fontSizes.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        
        start = tc.selectionStart()
        end = tc.selectionEnd()
        
        tc.beginEditBlock()
        for pos in range(start, end):
            tc.setPosition(pos)
            tc.setPosition(pos+1, KeepAnchor)

            charFormat = tc.charFormat()
            pointSize = charFormat.font().pointSize()
            
            self.fontSizes.append(pointSize)
            if self.crement == "fontUpperToolButton":
                charFormat.setFontPointSize(pointSize + 1)
            else:
                if pointSize > 1:
                    charFormat.setFontPointSize(pointSize - 1)
            
            tc.setCharFormat(charFormat)
        tc.endEditBlock()
     

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)      
        
        start = tc.selectionStart()
        end = tc.selectionEnd()
        i = 0

        tc.beginEditBlock()
        for pos in range(start, end):
            tc.setPosition(pos)
            tc.setPosition(pos+1, KeepAnchor)

            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFontPointSize(self.fontSizes[i])

            tc.setCharFormat(charFormat)
            i += 1
     
        tc.endEditBlock()
           
    
class SetBoldUndoCommand(BaseUndoCommand):

    def __init__(self, doc, isFontDecoration, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.isFontDecoration = isFontDecoration
        self.fontDecorations = []
        
    def redo(self):
        
        self.fontDecorations.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                self.fontDecorations.append(charFont.bold())
                charFormat.setFontWeight(
                    QFont.Bold if self.isFontDecoration else QFont.Normal
                    )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fontDecorations.append(charFont)
            charFormat.setWeight(
                QFont.Bold if self.isFontDecoration else QFont.Normal
                )
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFont.setBold(self.fontDecorations[i])
                charFormat.setFont(charFont)

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFont(self.fontDecorations[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class SetItalicUndoCommand(SetBoldUndoCommand):

    def __init__(self, doc, isFontDecoration, undoText, parent=None):
        super().__init__(doc, isFontDecoration, undoText ,parent)
        
    def redo(self):
        
        self.fontDecorations.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                self.fontDecorations.append(charFont.italic())
                charFormat.setFontItalic(
                    self.isFontDecoration
                    )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fontDecorations.append(charFont)
            charFormat.setFontItalic(
                self.isFontDecoration
                )
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFont.setItalic(self.fontDecorations[i])
                charFormat.setFont(charFont)

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFont(self.fontDecorations[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class SetUnderlineUndoCommand(SetBoldUndoCommand):

    def __init__(self, doc, isFontDecoration, undoText, parent=None):
        super().__init__(doc, isFontDecoration, undoText ,parent)
        
    def redo(self):
        
        self.fontDecorations.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                self.fontDecorations.append(charFont.underline())
                charFormat.setFontUnderline(
                    self.isFontDecoration
                    )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fontDecorations.append(charFont)
            charFormat.setFontUnderline(
                self.isFontDecoration
                )
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFont.setUnderline(self.fontDecorations[i])
                charFormat.setFont(charFont)

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFontUnderline(self.fontDecorations[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class SetStrikeOutUndoCommand(SetBoldUndoCommand):

    def __init__(self, doc, isFontDecoration, undoText, parent=None):
        super().__init__(doc, isFontDecoration, undoText ,parent)
        
    def redo(self):
        
        self.fontDecorations.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                self.fontDecorations.append(charFont.strikeOut())
                charFormat.setFontStrikeOut(
                    self.isFontDecoration
                    )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            self.fontDecorations.append(charFont.strikeOut())
            charFormat.setFontStrikeOut(
                self.isFontDecoration
                )
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                charFont = charFormat.font()
                charFont.setStrikeOut(self.fontDecorations[i])
                charFormat.setFont(charFont)

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            charFont = charFormat.font()
            charFormat.setFontStrikeOut(self.fontDecorations[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class SetVerticalAlignmentUndoCommand(SetBoldUndoCommand):

    def __init__(self, doc, isFontDecoration, undoText, parent=None):
        super().__init__(doc, isFontDecoration, undoText ,parent)
        
    def redo(self):
        
        self.fontDecorations.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                self.fontDecorations.append(charFormat.verticalAlignment())
                charFormat.setVerticalAlignment(
                    self.isFontDecoration
                    )
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()

            self.fontDecorations.append(charFormat.verticalAlignment())
            charFormat.setVerticalAlignment(
                    self.isFontDecoration
          
                )
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)

       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0

            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
               
                charFormat.setVerticalAlignment(self.fontDecorations[i])
                

                tc.setCharFormat(charFormat)
                i += 1
         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()

            charFormat.setVerticalAlignment(self.fontDecorations[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

class TextColorUndoCommand(BaseUndoCommand):
  

    def __init__(self, doc, color, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.color = color
        self.colors = []
        
    def redo(self):
        
        self.colors.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                
                self.colors.append(charFormat.foreground())
                charFormat.setForeground(self.color)
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            
            self.colors.append(charFormat.foreground())
            charFormat.setForeground(self.color)
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor) 
                charFormat = tc.charFormat()    
                #SpecifiesOnlyを外すとうまくいく
                charFormat.setForeground(self.colors[i])
                tc.setCharFormat(charFormat)
                i += 1         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()    
            charFormat.setForeground(self.colors[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)


class HighlightColorUndoCommand(BaseUndoCommand):
  

    def __init__(self, doc, color, undoText, parent=None):
        super().__init__(doc, undoText ,parent)

        t = doc.parent()
        tc = t.textCursor()
        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.color = color
        self.colors = []
        
    def redo(self):
        
        self.colors.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                
                self.colors.append(charFormat.background())
                charFormat.setBackground(self.color)
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            
            self.colors.append(charFormat.background())
            charFormat.setBackground(self.color)
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor) 
                charFormat = tc.charFormat()    
                #SpecifiesOnlyを外すとうまくいく
                charFormat.setBackground(self.colors[i])
                tc.setCharFormat(charFormat)
                i += 1         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()    
            charFormat.setBackground(self.colors[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)   

class PlusIndentUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, direction, undotext, parent=None):
        super().__init__(doc, undotext, parent)
        
        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.indentPointer = doc.parent().indentPointer
        self.direction = direction
    
        
    def redo(self):
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        leftMargin = blockFormat.indent()
        if leftMargin < g_pageSizeF.width() - 36:           
            
            self.indentPointer.indentChanged.emit(blockFormat.indent() + 36)
            self.indentPointer.m_point += 36
            self.indentPointer.update()

    def undo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        leftMargin = blockFormat.indent()      
        if leftMargin -36  >= 0:

            self.indentPointer.indentChanged.emit(blockFormat.indent() - 36)
            self.indentPointer.m_point -= 36
            self.indentPointer.update()

class MinusIndentUndoCommand(PlusIndentUndoCommand):
    
    def __init__(self, doc, direction, undotext, parent=None):
        super().__init__(doc, direction, undotext, parent)    
   
        
    def redo(self):
        super().undo()      

    def undo(self):
        super().redo()

class InsertListUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc,  style, undotext, parent=None):
        super().__init__(doc, undotext, parent)    

        tc = doc.parent().textCursor()
        self.pos = tc.position()
        
        self.indentPointer = doc.parent().indentPointer
        self.textIndentPointer = doc.parent().textIndentPointer
        self.style = style
        
    def redo(self):
        
        tc = QTextCursor(self.doc)
        tc.setPosition(self.pos)
        
        lf = QTextListFormat()
        lf.setStyle(self.style)
        tc.insertList(lf)
        self.doc.parent().setTextCursor(tc)
        self.indentPointer.m_point += 40
        self.textIndentPointer.m_point += 40
        self.indentPointer.update()
        self.textIndentPointer.update()

    def undo(self):
        tc = QTextCursor(self.doc)
        tc.setPosition(self.pos)
        tc.deleteChar()
        self.indentPointer.m_point -= 40
        self.textIndentPointer.m_point -= 40
        self.indentPointer.update()
        self.textIndentPointer.update()

class SetLineHeightUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc,  height, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.oldHeight = tc.blockFormat().lineHeight()/100
        self.height = height
        
    def redo(self):       
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = block.blockFormat()
        blockFormat.setLineHeight(self.height*100, 1)
        tc.setBlockFormat(blockFormat)        

    def undo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = block.blockFormat()
        blockFormat.setLineHeight(self.oldHeight*100, 1)
        tc.setBlockFormat(blockFormat)

class SetBottomMarginUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, bool, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.bool = bool
        self.bottomMargin = tc.blockFormat().bottomMargin()
        
    def redo(self):       
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = block.blockFormat()
        blockFormat.setBottomMargin(10 if self.bool else 0)  
        tc.setBlockFormat(blockFormat)
        
    def undo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = block.blockFormat()
        blockFormat.setBottomMargin(self.bottomMargin)  
        tc.setBlockFormat(blockFormat)
        
class SetAlignmentUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, alignment, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        tc = doc.parent().textCursor()
        self.blockNumber  = tc.block().blockNumber()
        self.oldAlignment = tc.blockFormat().alignment()
        self.alignment = alignment

    def redo(self):
        
        tc = QTextCursor(
            self.doc.findBlockByNumber(self.blockNumber)
            )
        blockFormat = tc.blockFormat()
        blockFormat.setAlignment(self.alignment)
        tc.setBlockFormat(blockFormat)

    def undo(self):

        tc = QTextCursor(
            self.doc.findBlockByNumber(self.blockNumber)
            )
        blockFormat = tc.blockFormat()
        blockFormat.setAlignment(self.oldAlignment)
        tc.setBlockFormat(blockFormat)

class SetBlockFormatByParagraphDialog(BaseUndoCommand):

    def __init__(self, doc, oldTextIndent, oldIndent, oldRightIndent, oldLineHeight, oldBottomMargin, oldAlignment
,                                        newTextIndent, newIndent, newRightIndent, newLineHeight, newBottomMargin, newAlignment,
                                     undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.oldIndent = oldIndent
        self.oldTextIndent = oldTextIndent
        self.oldRightIndent = oldRightIndent

        self.oldLineHeight = oldLineHeight
        self.oldBottomMargin = oldBottomMargin
        self.oldAlignment = oldAlignment

        self.newTextIndent = newTextIndent
        self.newIndent = newIndent
        self.newRightIndent = newRightIndent

        self.newLineHeight = newLineHeight
        self.newBottomMargin = newBottomMargin
        self.newAlignment = newAlignment

        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()       

    def redo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setTextIndent(self.newTextIndent)
        blockFormat.setIndent(self.newIndent)
        blockFormat.setRightMargin(self.newRightIndent )
    
        blockFormat.setLineHeight(self.newLineHeight*100, 1)
        blockFormat.setBottomMargin( self.newBottomMargin)
        blockFormat.setAlignment(self.newAlignment)
      
        tc.setBlockFormat(blockFormat)
        t = self.doc.parent()
        
        t.indentPointer.indentChanged.emit(self.newIndent)
        t.textIndentPointer.textIndentChanged.emit(self.newTextIndent)
        t.rightIndentPointer.rightIndentChanged.emit(g_pageSize.width() - self.newRightIndent)

    def undo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setTextIndent(self.oldTextIndent)
        blockFormat.setIndent(self.oldIndent)
        blockFormat.setRightMargin(self.oldRightIndent )
        blockFormat.setLineHeight(self.oldLineHeight*100, 1)
        blockFormat.setBottomMargin( self.oldBottomMargin)
        blockFormat.setAlignment(self.oldAlignment)
      
        tc.setBlockFormat(blockFormat)
        t = self.doc.parent()
        t.textIndentPointer.textIndentChanged.emit(self.oldTextIndent)
        t.indentPointer.indentChanged.emit(self.oldIndent)
        t.rightIndentPointer.rightIndentChanged.emit(self.oldRightIndent)

class LoadImageUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, image, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        self.image = image
        self.pos = doc.parent().textCursor().position()
        self.imageHandler = doc.parent().imageHandler
        self.uuid = ""
    def redo(self):

        tc = self.doc.parent().textCursor()
        tc.setPosition(self.pos)
        p = QPixmap(self.image)
        from commons import ImageLabel
        label = ImageLabel(autoFillBackground=False,
                       pixmap=p,
                       size = self.image.size(),
                       visible=True,
                       styleSheet = "QLabel{background-color: white}",
                       parent=self.doc.parent())
        label.uuid = self.uuid
        label.imageHandler = self.imageHandler
        
        char = tc.charFormat()
        char.setObjectType(ImageObject)
        char.setProperty(ImageProperty, label)
        tc.insertText(chr(0xfffc), char)
        
    def undo(self):
        
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.pos)
        tc.setPosition(self.pos+1, KeepAnchor)
        char = tc.charFormat()
        label = char.property(ImageProperty)
        label.setVisible(False)
        label.setParent(None)
        
        tc.deleteChar()


class ChangeImageUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, image, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        self.newImage = image
        l = doc.parent().customObjectPointer
        self.name = str(uuid.uuid4())
        l.setObjectName(self.name)
        p = l.pixmap()
        i = p.toImage()
        self.oldImage = i
        self.pos = doc.parent().textCursor().position()
        self.imageHandler = doc.parent().imageHandler
        self.geometry = l.geometry()
        
    def redo(self):

        label = self.doc.parent().findChild(
            ImageLabel,
            self.name)       
            
        p = QPixmap(self.newImage)
        label.setPixmap(p)
        label.resize(p.size())
        self.imageHandler.setVisible(False)
        
    def undo(self):
        
        label = self.doc.parent().findChild(
            ImageLabel,
            self.name)       
            
        p = QPixmap(self.oldImage)
        label.setPixmap(p)
        label.resize(p.size())
        self.imageHandler.setVisible(False)

class ChangeImageSizeByDialogUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, h, v, keep, undotext, parent=None):
        super().__init__(doc, undotext, parent)


        self.h = h
        self.v = v

        l = doc.parent().customObjectPointer
        self.uuid = l.uuid
        p = l.pixmap()
        i = p.toImage()
        self.doubleBuffer = QPixmap(l._doubleBuffer)
        self.oldImage = i
        self.oldSize = i.size()
        self.pos = doc.parent().textCursor().position()
        self.imageHandler = doc.parent().imageHandler
        self.geometry = l.geometry()
        
        self.aspectRatio = Qt.KeepAspectRatio if  keep else Qt.IgnoreAspectRatio
        
    def redo(self):

        label =  self.doc.parent().findChild(
            ImageLabel,
            self.uuid)
        p = label.pixmap()       
        p = p.scaled(self.h*p.size().width(), self.v*p.size().height(),
                         self.aspectRatio,
                         Qt.TransformationMode.SmoothTransformation)
        dp = label._doubleBuffer.scaled(p.size().width(), p.size().height(),
                                        self.aspectRatio,
                         Qt.TransformationMode.SmoothTransformation)
        label.setPixmap(dp)
        label.resize(dp.size())
        self.doc.parent().setFocus()

        tc = self.doc.parent().textCursor()
        tc.insertText(" ")
        tc.deleteChar()

        
    def undo(self):
        
        label =  self.doc.parent().findChild(
            ImageLabel,
            self.uuid)
        label.setPixmap(self.doubleBuffer)
        label.resize(self.doubleBuffer.size())
        self.doc.parent().setFocus()

        tc = self.doc.parent().textCursor()
        tc.insertText(" ")
        tc.deleteChar()
        
class ChangeImageSizeByMouseUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, hsize, vsize, keep, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        self.hsize = hsize
        self.vsize = vsize
        
        l = doc.parent().customObjectPointer
        self.uuid = l.uuid
        p = l.pixmap()
        i = p.toImage()
        self.doubleBuffer = QPixmap(l._doubleBuffer)
        self.oldImage = i
        self.oldSize = i.size()
        self.pos = doc.parent().textCursor().position()
        self.imageHandler = doc.parent().imageHandler
        self.geometry = l.geometry()        
        self.aspectRatio = Qt.KeepAspectRatio if  keep else Qt.IgnoreAspectRatio
        
    def redo(self):

        from commons import ImageLabel
        label =  self.doc.parent().findChild(
            ImageLabel,
            self.uuid )
        p = label.pixmap()
        transform = QTransform()
        transform.scale(self.hsize/p.size().width(), self.vsize/p.size().height())
        dp = p.transformed(transform)
##        p = p.scaled(self.hsize, self.vsize,
##                         self.aspectRatio,
##                         Qt.TransformationMode.SmoothTransformation)
##        dp = label._doubleBuffer.scaled(self.hsize, self.vsize,
##                                        self.aspectRatio,
##                         Qt.TransformationMode.SmoothTransformation)
                
        label.setPixmap(dp)
        label.resize(dp.size())
        self.doc.parent().setFocus()

        tc = self.doc.parent().textCursor()
        tc.insertText(" ")
        tc.deleteChar()

    def undo(self):

        from commons import ImageLabel
        label =  self.doc.parent().findChild(
            ImageLabel,
            self.uuid )
        label.setPixmap(self.doubleBuffer)
        label.resize(self.doubleBuffer.size())
        self.doc.parent().setFocus()

        tc = self.doc.parent().textCursor()
        tc.insertText(" ")
        tc.deleteChar()



    
class InsertDateAndTimeUndoCommand(BaseUndoCommand):
    
    def __init__(self, doc, text, undotext, parent=None):
        super().__init__(doc, undotext, parent)

        tc = doc.parent().textCursor()
        self.pos = tc.position()
        self.text = text
        self.lastPos = self.pos + len(text)
        
    def redo(self):
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.pos)
        tc.insertText(self.text)
        
    def undo(self):
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.pos)
        tc.setPosition(self.lastPos, KeepAnchor)
        tc.deleteChar()

class ClearBackgroundUndoCommand(BaseUndoCommand):

    def __init__(self, doc, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        tc = doc.parent().textCursor()
        self.selectionStart  = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.backgrounds = []

    def redo(self):
        
        self.backgrounds.clear()
        t = self.doc.parent()
        
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor)
 
                charFormat = tc.charFormat()
                
                self.backgrounds.append(charFormat.background())
                charFormat.clearBackground()
                
                tc.setCharFormat(charFormat)
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()
            
            self.backgrounds.append(charFormat.background())
            charFormat.clearBackground()
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)

        
    def undo(self):
        
        t = self.doc.parent()
        tc = t.textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
       
        if tc.hasSelection():
            start = tc.selectionStart()
            end = tc.selectionEnd()
            i = 0
            tc.beginEditBlock()
            for pos in range(start, end):
                tc.setPosition(pos)
                tc.setPosition(pos+1, KeepAnchor) 
                charFormat = tc.charFormat()    
                #SpecifiesOnlyを外すとうまくいく
                charFormat.setBackground(self.backgrounds[i])
                tc.setCharFormat(charFormat)
                i += 1         
            tc.endEditBlock()
           
        else:
            charFormat = tc.charFormat()    
            charFormat.setBackground(self.backgrounds[0])
            tc.setCharFormat(charFormat)
            t.setTextCursor(tc)
    
class SetWrapUndoCommand(BaseUndoCommand):

    def __init__(self, doc, newWrap, oldWrap , undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.oldWrap = oldWrap
        self.newWrap = newWrap

    def redo(self):

        t = self.doc.parent()
        t.setLineWrapMode(self.newWrap)
        if self.newWrap == QTextEdit.NoWrap or self.newWrap == QTextEdit.WidgetWidth:
            
            width = qApp.primaryScreen().availableSize().width()
            height = qApp.primaryScreen().availableSize().height()
            t.resize(qApp.primaryScreen().availableSize())
            
            t.mainView.setSceneRect(0, 0, width ,height)
            t.rulerView.setSceneRect(0, 0, width, 50)
        else:
            t.setLineWrapColumnOrWidth(g_pageSizeF.width())
            width = g_pageSize.width()
            height = g_pageSize.height()
            t.resize(g_pageSize)
            t.mainView.setSceneRect(0, 0, width ,height)
            t.rulerView.setSceneRect(0, 0, width, 50)

    def undo(self):

        t = self.doc.parent()
        t.setLineWrapMode(self.oldWrap)
        if self.oldWrap == QTextEdit.NoWrap or self.oldWrap == QTextEdit.WidgetWidth:
            
            width = qApp.primaryScreen().availableSize().width()
            height = qApp.primaryScreen().availableSize().height()
            t.resize(qApp.primaryScreen().availableSize())
            
            t.mainView.setSceneRect(0, 0, width ,height)
            t.rulerView.setSceneRect(0, 0, width, 50)
        else:
            t.setLineWrapColumnOrWidth(g_pageSizeF.width())
            width = g_pageSize.width()
            height = g_pageSize.height()
            t.resize(g_pageSize)
            t.mainView.setSceneRect(0, 0, width ,height)
            t.rulerView.setSceneRect(0, 0, width, 50)
        
class AllReplaceUndoCommand(BaseUndoCommand):

    def __init__(self, doc, searchText, replacedText, flags, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.searchText = searchText
        self.replacedText = replacedText
        self.flags = flags
        self.exs = []
        self.replacedPositions = []
        
    def findRecur(self, tc, text ):
        
        tc = self.doc.find(text,
                                       tc.selectionEnd(),
                                       self.flags)
        if not tc.isNull():
            self.exs.append(tc)
            
            self.findRecur(tc, text)

    def redo(self):
                
        text = self.searchText
        flags = self.flags
        replacedText = self.replacedText
        tc = QTextCursor(self.doc)
        self.exs = []        
        self.findRecur(tc, text)
        tc.beginEditBlock()
        for ex in self.exs:
            insertStartPos = ex.selectionStart()
            ex.insertText(replacedText)
            insertEndPos   = ex.position()
            self.replacedPositions.append(                
                (insertStartPos,
                 insertEndPos)
                )
        tc.endEditBlock()

    def undo(self):

        tc = QTextCursor(self.doc)
        tc.beginEditBlock()
        for replacedPosition in self.replacedPositions:
            tc.setPosition(replacedPosition[0])
            tc.setPosition(replacedPosition[1], KeepAnchor)
            tc.insertText(self.searchText)
        tc.endEditBlock()
    
       
class OneReplaceUndoCommand(BaseUndoCommand):

    def __init__(self, doc, searchText, replacedText, tc, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.selectionStart = tc.selectionStart()
        self.selectionEnd = tc.selectionEnd()
        self.replacedPosition = 0
        self.searchText = searchText
        self.replacedText = replacedText
        

    def redo(self):
        
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.selectionEnd, KeepAnchor)
        tc.insertText(self.replacedText)
        self.replacedPosition = tc.position()
        
    def undo(self):
        
        tc = self.doc.parent().textCursor()
        tc.setPosition(self.selectionStart)
        tc.setPosition(self.replacedPosition, KeepAnchor)
        tc.insertText(self.searchText)
        
class SetIndentUndoCommand(BaseUndoCommand):

    def __init__(self, doc, indent, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.indent = indent
        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.indentPointer = doc.parent().indentPointer
        self.textIndentPointer = doc.parent().textIndentPointer
        self.originalIndent =  tc.blockFormat().indent()     
    
    def redo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()

        blockFormat.setIndent(self.indent)
        tc.setBlockFormat(blockFormat)
        blockFormat = tc.blockFormat()
        textIndent = blockFormat.textIndent()        
        self.textIndentPointer.m_point = textIndent + self.indent
        self.textIndentPointer.update(False)
        self.indentPointer.m_point = self.indent
        self.indentPointer.update(False)
        
    def undo(self):
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setIndent(self.originalIndent)
        tc.setBlockFormat(blockFormat)
        self.indentPointer.m_point = self.originalIndent
        blockFormat = tc.blockFormat()
        textIndent = blockFormat.textIndent()
        self.indentPointer.update(False)
        self.textIndentPointer.m_point = textIndent + self.originalIndent
        self.textIndentPointer.update(False)

class SetTextIndentUndoCommand(BaseUndoCommand):

    def __init__(self, doc, textIndent, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.textIndent = textIndent
        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.indentPointer = doc.parent().indentPointer
        self.textIndentPointer = doc.parent().textIndentPointer
        self.originalTextIndent =  tc.blockFormat().textIndent()     
    
    def redo(self):
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)        
        blockFormat = tc.blockFormat()
        leftMargin = blockFormat.indent()
        blockFormat.setTextIndent(self.textIndent - leftMargin)
        tc.setBlockFormat(blockFormat)        
        self.textIndentPointer.m_point = leftMargin + (self.textIndent- leftMargin)        
        self.textIndentPointer.update(False)    

        
    def undo(self):
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setTextIndent(self.originalTextIndent)
        tc.setBlockFormat(blockFormat)
        self.textIndentPointer.m_point = self.originalTextIndent
        
        blockFormat = tc.blockFormat()
        textIndent = blockFormat.textIndent()        
        self.textIndentPointer.m_point = textIndent 
        self.textIndentPointer.update(False)

class SetRightIndentUndoCommand(BaseUndoCommand):

    def __init__(self, doc, rightPoint, undoText, parent=None):
        super().__init__(doc, undoText, parent)
            
        self.rightPoint = rightPoint
        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
        self.rightIndentPointer = doc.parent().rightIndentPointer
     
        self.originalRightIndent =  tc.blockFormat().rightMargin()
    
    def redo(self):
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setRightMargin(g_pageSizeF.width() - self.rightPoint)
        tc.setBlockFormat(blockFormat)
        #m_pointは、rightPoint関数で計算されるから、インデントをそのまま渡せばよい。
        self.rightIndentPointer.m_point = g_pageSizeF.width() - self.rightPoint
        self.rightIndentPointer.update(False)
        
    def undo(self):
        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        blockFormat.setRightMargin(self.originalRightIndent)
        tc.setBlockFormat(blockFormat)
        self.rightIndentPointer.m_point = self.originalRightIndent       
        self.rightIndentPointer.update(False)
  
class SetTabPositionUndoCommand(BaseUndoCommand):

    def __init__(self, doc,  tab, float, undoText, parent=None):
        super().__init__(doc, undoText, parent)

        self.tab = tab
        self.mainScene = self.tab.mainScene
        self.m_point = self.tab.m_point
        
        self.position = float
        tc = doc.parent().textCursor()
        self.blockNumber = tc.block().blockNumber()
      
    def redo(self):

        
        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        tab = QTextOption.Tab()
        tab.position = self.position
        tab.type = QTextOption.TabType.LeftTab
        tabPositions = blockFormat.tabPositions()
        tabPositions.append(tab)

        blockFormat.setTabPositions(tabPositions)
        tc.setBlockFormat(blockFormat)
        t = self.doc.parent()
        r = t.rulerObject
        s = r.scene()
        from commons  import TabPointer
        for item in s.items():
            if isinstance(item, TabPointer):
                if item.m_rect.x() == self.m_point:
                    
                    return
   
        tabPointer = TabPointer(
            self.document(), self.mainScene, self.m_point
            )
        tabPointer.setZValue(3.0)
        tabPointer.update(False)
        t.rulerScene.addItem(tabPointer)
        t.rulerScene.update()

    def undo(self):

        block = self.doc.findBlockByNumber(self.blockNumber)
        tc = QTextCursor(block)
        blockFormat = tc.blockFormat()
        tabPositions = blockFormat.tabPositions()
        tabPositions = tabPositions[:-2]
        blockFormat.setTabPositions(tabPositions)
        tc.setBlockFormat(blockFormat)
        t = self.doc.parent()
        r = t.rulerObject
        s = r.scene()
        from commons  import TabPointer
        for item in s.items():
            if isinstance(item, TabPointer):
                if item.m_rect.x() == self.position:
                    s.removeItem(item)
        s.update()
        
class MoveTabPositionUndoCommand(BaseUndoCommand):

    def __init__(self, doc,  tabPointer, fr, to, undoText, parent=None):
        super().__init__(doc, undoText, parent)
        
        self.tabPointer = tabPointer
        self.tabPointer.name = str(uuid.uuid4())
        
        self.mainScene = self.tabPointer.mainScene
        self.m_point = self.tabPointer.m_point
        self.rulerScene = tabPointer.scene()
        tc = doc.parent().textCursor()
        blockFormat = tc.blockFormat()
        self.blockNumber = tc.block().blockNumber()
        
        self.originalTabPositions = []
        for tab in blockFormat.tabPositions():
            self.originalTabPositions.append(tab.position)

        self.movedTabPositions = []
        self.to = to
        self.fr = fr
        
        
    def redo(self):
        
        block = self.doc.findBlockByNumber(
            self.blockNumber
            )
        tc = QTextCursor(block)
        blockFormat  = tc.blockFormat()
        blockFormat.setTabPositions([])
        
        tabPositions = []
        #移動した後のタブアイテムにしか過ぎない。再度Redoをしても、意味がない。
        #どこからどこへ移動したのかという情報が大切。
        #そして、移動したタブの特定も重要だ。
        from commons  import TabPointer
        tabItems = [tabItem for tabItem in  self.rulerScene.items()  if isinstance(tabItem, TabPointer)] 
        for tabItem in tabItems:
            tab = QTextOption.Tab()
            tab.type = QTextOption.LeftTab
            #self.tabPointerが、もし破壊されていたら、エラーが起きる可能性がある。
            #だから、最も保守的なのは、同じ情報でアイテムを再度作ること。
            #ワードパッドには、タブアイテムを消す操作があるのか？無ければ困る。
            if tabItem.name == self.tabPointer.name:
                tab.position = self.to
            else:
                tab.position = tabItem.m_point
            tabPositions.append(tab)
            
        tabPositions.sort(key = lambda tab: tab.position)
        blockFormat.setTabPositions(tabPositions)
        tc.setBlockFormat(blockFormat)

        for num, tabItem in enumerate(tabItems):
            if tabItem is self.tabPointer:
                tabItem.m_point = self.to
            else:
                tabItem.m_point = tabPositions[num].position          
            tabItem.update(False)
            
        self.rulerScene.update()
        
    def undo(self):
        block = self.doc.findBlockByNumber(
            self.blockNumber
            )
        tc = QTextCursor(block)
        blockFormat  = tc.blockFormat()
        blockFormat.setTabPositions([])
        from commons  import TabPointer
        tabItems = [tabItem for tabItem in  self.rulerScene.items()  if isinstance(tabItem, TabPointer)]        
        tabPositions = []
        
        for tabPosition in self.originalTabPositions:
            tab = QTextOption.Tab()
            tab.type = QTextOption.LeftTab
            tab.position = tabPosition
            tabPositions.append(tab)
        
        tabPositions.sort(key = lambda tab: tab.position)
        blockFormat.setTabPositions(tabPositions)
        t = self.document().parent()
        tc.setBlockFormat(blockFormat)
        for num, tabItem in enumerate(tabItems):
            
            tabItem.m_point = self.originalTabPositions[num]
            tabItem.update(False)
        self.rulerScene.update()
