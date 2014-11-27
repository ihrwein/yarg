from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject

from yarg.gui.listmodel import QObjectListModel
from yarg.gui.rsync_option_view_model import RsyncOptionViewModel


class ProfileViewModel(QObject):
    def __init__(self, model, parent=None):
        super(ProfileViewModel, self).__init__(parent)
        self.model = model
        self._rsync_options = QObjectListModel()
        for item in sorted(model.rsync_options.items(), key=lambda opt: opt[0]):
            self._rsync_options.append(RsyncOptionViewModel(item))

    name_changed = pyqtSignal()

    @pyqtProperty(str, notify=name_changed)
    def name(self):
        return self.model.name

    @name.setter
    def name(self, val):
        if self._name != val:
            self.model.name = val
            self.name_changed.emit()

    @pyqtProperty(QObjectListModel, constant=True)
    def rsync_options(self):
        return self._rsync_options

    def save_changes(self):
        for option in self._rsync_options:
            self.model.rsync_options[option.key] = option._value

    def discard_changes(self):
        for option in self._rsync_options:
            option.value = self.model.rsync_options[option.key]