from datetime import datetime

from PyQt5.QtCore import pyqtProperty, pyqtSignal, QObject

from yarg import SSHOptions

from yarg.gui.listmodel import QObjectListModel
from yarg.gui.rsync_option_view_model import RsyncOptionViewModel


class ProfileViewModel(QObject):
    def __init__(self, model, parent=None):
        super(ProfileViewModel, self).__init__(parent)
        self.model = model
        self._name = self._last_sync = self._destination_path = \
            self._remote_component = self._remote_host = \
            self._remote_port = self._remote_user = None
        self._sync_in_progress = False
        self._init_from_profile()

    def _init_from_profile(self):
        self.name = self.model.name
        self.last_sync = self.model.last_sync
        self._source_paths = QObjectListModel()
        for path in self.model.source.path:
            self._source_paths.append(path)
        self.source_paths_changed.emit()
        self.destination_path = self.model.destination.path[0]
        self.remote_component = 'Destination'
        if self.model.source.is_remote:
            self.remote_component = 'Source'
        elif not self.model.source.is_remote and not self.model.destination.is_remote:
            self.remote_component = 'Neither'
        has_ssh_config = self.remote_component != 'Neither' and self.model.sshoptions is not None
        self.remote_host = self.model.sshoptions.host if has_ssh_config and self.model.sshoptions.host is not None else ''
        self.remote_port = str(
            self.model.sshoptions.port) if has_ssh_config and self.model.sshoptions.port is not None else ''
        self.remote_user = self.model.sshoptions.user if has_ssh_config and self.model.sshoptions.user is not None else ''
        self._rsync_options = QObjectListModel()
        for item in sorted(self.model.rsync_options.items(), key=lambda opt: opt[0]):
            self._rsync_options.append(RsyncOptionViewModel(item))
        self.rsync_options_changed.emit()

    name_changed = pyqtSignal()

    @pyqtProperty(str, notify=name_changed)
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if self._name != val:
            self._name = val
            self.name_changed.emit()

    remote_component_changed = pyqtSignal()

    @pyqtProperty(str, notify=remote_component_changed)
    def remote_component(self):
        return self._remote_component

    @remote_component.setter
    def remote_component(self, val):
        if self._remote_component != val:
            self._remote_component = val
            self.remote_component_changed.emit()

    remote_host_changed = pyqtSignal()

    @pyqtProperty(str, notify=remote_host_changed)
    def remote_host(self):
        return self._remote_host

    @remote_host.setter
    def remote_host(self, val):
        if self._remote_host != val:
            self._remote_host = val
            self.remote_host_changed.emit()

    remote_port_changed = pyqtSignal()

    @pyqtProperty(str, notify=remote_port_changed)
    def remote_port(self):
        return self._remote_port

    @remote_port.setter
    def remote_port(self, val):
        if self._remote_port != val:
            self._remote_port = val
            self.remote_port_changed.emit()

    remote_user_changed = pyqtSignal()

    @pyqtProperty(str, notify=remote_user_changed)
    def remote_user(self):
        return self._remote_user

    @remote_user.setter
    def remote_user(self, val):
        if self._remote_user != val:
            self._remote_user = val
            self.remote_user_changed.emit()

    destination_path_changed = pyqtSignal()

    @pyqtProperty(str, notify=destination_path_changed)
    def destination_path(self):
        return self._destination_path

    @destination_path.setter
    def destination_path(self, val):
        if self._destination_path != val:
            self._destination_path = val
            self.destination_path_changed.emit()

    source_paths_changed = pyqtSignal()

    @pyqtProperty(QObjectListModel, notify=source_paths_changed)
    def source_paths(self):
        return self._source_paths

    last_sync_changed = pyqtSignal()

    @pyqtProperty(str, notify=last_sync_changed)
    def last_sync(self):
        if self._last_sync is not None:
            return self._last_sync.__format__('%Y-%m-%d %H:%M')
        else:
            return ''

    @last_sync.setter
    def last_sync(self, v):
        if isinstance(v, str):
            val = datetime.strptime(v, '%Y-%m-%d %H:%M')
        else:
            val = v
        if self._last_sync != val:
            self._last_sync = val
            self.last_sync_changed.emit()

    rsync_options_changed = pyqtSignal()

    @pyqtProperty(QObjectListModel, notify=rsync_options_changed)
    def rsync_options(self):
        return self._rsync_options

    sync_in_progress_changed = pyqtSignal()

    @pyqtProperty(bool, notify=sync_in_progress_changed)
    def sync_in_progress(self):
        return self._sync_in_progress

    @sync_in_progress.setter
    def sync_in_progress(self, val):
        if self._sync_in_progress != val:
            self._sync_in_progress = val
            self.sync_in_progress_changed.emit()

    def save_changes(self):
        self.model.name = self._name
        self.model.source.path.clear()
        for path in self._source_paths:
            self.model.source.path.append(path)
        self.model.destination_path = self._destination_path
        if self._remote_component == 'Neither':
            self.model.sshoptions = None
        else:
            self.model.sshoptions = SSHOptions()
            self.model.sshoptions.host = self._remote_host
            self.model.sshoptions.port = self._remote_port
            self.model.sshoptions.user = self._remote_user
        for option in self._rsync_options:
            self.model.rsync_options[option.key] = option.value

    def discard_changes(self):
        self._init_from_profile()