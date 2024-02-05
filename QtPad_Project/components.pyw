from enums import *
from ui_components import *


class ImageObjectInterface(QPyTextObject):

    def __init__(self, parent=None):
        super().__init__(parent)

    def intrinsicSize(
        self, doc, posInDocument, format
        ):
        image = format.property(ImageProperty)
        return QSizeF(image.size())

    def drawObject(
        self, painter, rect, doc, posInDocument, format
        ):

        image = format.property(ImageProperty)
        image.render(painter, rect.topLeft().toPoint())
        image.move(rect.topLeft().toPoint())

class ImageLabel(QLabel):

    ImageObject = QTextFormat.UserObject
    ImageProperty = QTextFormat.UserProperty

    def __init__(self, autoFillBackground,
                 pixmap, size, visible, styleSheet, parent):
        super().__init__(parent)

        self.setAutoFillBackground(autoFillBackground)
        self.setPixmap(pixmap)
        self.setVisible(visible)
        self.setStyleSheet(styleSheet)
        self._doubleBuffer = pixmap
        self.setObjectName(str(uuid.uuid4()))

    def mousePressEvent(self, event):

        self.parent().customObjectPointer = self
        self.imageHandler.setRect(self.geometry())
        for child in self.imageHandler.childItems():
            child.setCenter()
            child.setVisible(True)
            child.setCustomObject(self)
        self.imageHandler.setCustomObject(self)
        self.imageHandler.setVisible(True)
        super().mousePressEvent(event)


    def save(self, out):
        out.writeBool(self.autoFillBackground())
        out.writeQString(self.styleSheet())
        out.writeQString(self.objectName())
        out << self.size()
        out << self.pixmap()
        out << self._doubleBuffer

    def load(self, out):
        self.setAutoFillBackground(out.readBool())
        self.setStyleSheet(out.readQString())
        self.setObjectName(out.readQString())
        size = QSize()
        out >> size
        pixmap = QPixmap()
        out >> pixmap
        self.resize(size)
        self.setPixmap(pixmap)
        pixmap = QPixmap()
        out >> pixmap
        self._doubleBuffer = pixmap



class WidgetAction(QWidgetAction):

    colorLabelPress = Signal(QLabel)
    colorLabelPressWithPixmap = Signal(
        QLabel, QPixmap
        )
    backgroundColorLabelPress = Signal(QLabel)
    listFormatLabelPress = Signal(QLabel)
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setDefaultWidget(TextColorWidget())

    def createWidget(self, widget):

        if (
            widget.objectName() ==
            "textColorMenu"
            ):
            self.w = self.defaultWidget()
            self.w.setParent(widget)
        elif (
            widget.objectName() ==
            "backgroundColorMenu"):
            self.w = BackgroundColorWidget(
                widget
                )
        elif (
            widget.objectName()
            == "listFormatSelectorMenu"):
            self.w = ListFormatSelector(widget)
            
        for child in self.w.children():
                child.installEventFilter(self)

        return self.w
        

    def eventFilter(self, obj, event):

      
        if (event.type() == QEvent.MouseButtonPress):
            p = obj.parent()
            objectName = p.objectName()
            if objectName == "TextColorWidget":
                self.colorLabelPress.emit(obj)
                pixmap = QPixmap(32, 32)
                pixmap.fill(
                    obj.palette().color(QPalette.Window))
                self.colorLabelPressWithPixmap.emit(obj, pixmap)

            elif objectName == "BackgroundColorWidget":
                
                self.backgroundColorLabelPress.emit(obj)
            
            elif objectName == "ListFormatSelector":
                
                self.listFormatLabelPress.emit(obj)
                
        return super().eventFilter(obj, event)
