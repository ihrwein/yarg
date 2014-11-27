from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject, QVariant


class RsyncOptionViewModel(QObject):
    def __init__(self, model=None, parent=None):
        '''Model should be a tuple from a dict'''
        super(RsyncOptionViewModel, self).__init__(parent)
        self._key = model[0]
        #self._value = QVariant(model[1])
        self._value = model[1]
        self._option_type = 'undefined'
        if isinstance(model[1], bool):
            self._option_type = 'bool'
        elif isinstance(model[1], str):
            self._option_type = 'string'
        elif isinstance(model[1], float):
            self._option_type = 'float'
        # isinstance(True, int) == True !!
        elif isinstance(model[1], int):
            self._option_type = 'int'

    @pyqtProperty(str, constant=True)
    def option_type(self):
        return self._option_type

    @pyqtProperty(str, constant=True)
    def key(self):
        return self._key

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