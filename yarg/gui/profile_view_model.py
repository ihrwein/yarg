from datetime import datetime

from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject

from yarg.gui.listmodel import QObjectListModel
from yarg.gui.rsync_option_view_model import RsyncOptionViewModel


class ProfileViewModel(QObject):
    def __init__(self, model, parent=None):
        super(ProfileViewModel, self).__init__(parent)
        self.model = model
        self._name = model.name
        self._source = model.source
        self._destination = model.destination
        self._last_sync = model.last_sync
        self._rsync_options = QObjectListModel()
        for item in sorted(model.rsync_options.items(), key=lambda opt: opt[0]):
            self._rsync_options.append(RsyncOptionViewModel(item))

    name_changed = pyqtSignal()

    @pyqtProperty(str, notify=name_changed)
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if self._name != val:
            self._name = val
            self.name_changed.emit()

    source_changed = pyqtSignal()

    @pyqtProperty(str, notify=source_changed)
    def source(self):
        return self._source

    @source.setter
    def source(self, val):
        if self._source != val:
            self._source = val
            self.source_changed.emit()

    destination_changed = pyqtSignal()

    @pyqtProperty(str, notify=destination_changed)
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, val):
        if self._destination != val:
            self._destination = val
            self.destination_changed.emit()

    last_sync_changed = pyqtSignal()

    @pyqtProperty(str, notify=last_sync_changed)
    def last_sync(self):
        return self._last_sync.__format__('%Y-%m-%d %H:%M')

    @last_sync.setter
    def last_sync(self, v):
        if isinstance(v, str):
            val = datetime.strptime(v, '%Y-%m-%d %H:%M')
        else:
            val = v
        if self._last_sync != val:
            self._last_sync = val
            self.last_sync_changed.emit()

    @pyqtProperty(QObjectListModel, constant=True)
    def rsync_options(self):
        return self._rsync_options

    def save_changes(self):
        for option in self._rsync_options:
            self.model.rsync_options[option.key] = option.value
        self.model.name = self.name
        self.model.source = self.source
        self.model.destination = self.destination

    def discard_changes(self):
        for option in self._rsync_options:
            option.value = self.model.rsync_options[option.key]
        self.name = self.model.name
        self.source = self.model.source
        self.destination = self.model.destination