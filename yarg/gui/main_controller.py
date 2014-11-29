from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

import yarg
from yarg.gui.profile_view_model import ProfileViewModel
from yarg.gui.listmodel import QObjectListModel
from yarg.location import Location
from yarg.profile import Profile


class MainController(QObject):
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
        self._selected_profile = ProfileViewModel(
            Profile('dummy profile', source=Location(path=['']), destination=Location(path=[''])))
        self._new_profile = None
        self._application = yarg.application.instance('yarg.conf')
        self._profile_model = QObjectListModel()
        profile_list = self._application.get_profiles().items()
        self._profile_model.append(list(map(lambda prof: ProfileViewModel(prof[1]), profile_list)))
        self._selected_profile_index = 0

    profile_model_changed = pyqtSignal()

    @pyqtProperty(QObjectListModel, constant=True)
    def profile_model(self):
        return self._profile_model

    selected_profile_changed = pyqtSignal()

    @pyqtProperty(ProfileViewModel, notify=selected_profile_changed)
    def selected_profile(self):
        return self._selected_profile

    new_profile_changed = pyqtSignal()

    @pyqtProperty(ProfileViewModel, notify=new_profile_changed)
    def new_profile(self):
        return self._new_profile

    @pyqtSlot(int)
    def profile_selection_changed(self, index):
        self._selected_profile = self._profile_model[index]
        self._selected_profile_index = index
        self.selected_profile_changed.emit()

    @pyqtSlot()
    def add_source_path_clicked(self):
        self.selected_profile.source_paths.append('')

    @pyqtSlot(int)
    def remove_source_path_clicked(self, index):
        self.selected_profile.source_paths.removeAt(index)

    @pyqtSlot()
    def add_new_profile_clicked(self):
        self._new_profile = ProfileViewModel(model=Profile(name=''))
        self.new_profile_changed.emit()

    @pyqtSlot()
    def save_new_profile_clicked(self):
        self._profile_model.append(self.new_profile)
        self._new_profile = None
        self.new_profile_changed.emit()

    @pyqtSlot()
    def discard_new_profile_clicked(self):
        self._new_profile = None
        self.new_profile_changed.emit()

    @pyqtSlot()
    def delete_profile_clicked(self):
        self._profile_model.removeAt(self._selected_profile_index)

    @pyqtSlot()
    def edit_panel_save_clicked(self):
        self._selected_profile.save_changes()

    @pyqtSlot()
    def edit_panel_close_clicked(self):
        self._selected_profile.discard_changes()