from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject, QVariant


class RsyncOptionViewModel(QObject):
    def __init__(self, model=None, parent=None):
        super(RsyncOptionViewModel, self).__init__(parent)
        self._key = model['key']
        self._hint = model['hint']
        self._value = model['value']
        self._option_type = model['type']

    @pyqtProperty(str, constant=True)
    def option_type(self):
        return self._option_type

    @pyqtProperty(str, constant=True)
    def key(self):
        return self._key

    @pyqtProperty(str, constant=True)
    def hint(self):
        return self._hint

    valueChanged = pyqtSignal()

    @pyqtProperty(QVariant, notify=valueChanged)
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        casted_value = RsyncOptionViewModel.gui_type_to_option_type(self._value, val)
        if self._value != casted_value:
            self._value = casted_value
            self.valueChanged.emit()

    @staticmethod
    def gui_type_to_option_type(python_value, gui_value):
        if isinstance(gui_value, str):
            return type(python_value)(gui_value)
        else:
            return gui_value