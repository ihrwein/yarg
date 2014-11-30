from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty


class SourcePathViewModel(QObject):
    def __init__(self, text, parent=None):
        super(QObject, self).__init__(parent)
        self._text = text

    text_changed = pyqtSignal()

    @pyqtProperty(str, notify=text_changed)
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        if self._text != val:
            self._text = val
            self.text_changed.emit()
