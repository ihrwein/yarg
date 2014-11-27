from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

from yarg.gui.profile_view_model import ProfileViewModel
from yarg.gui.listmodel import QObjectListModel
from yarg.profile import Profile


class MainController(QObject):
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
        self._selected_profile = ProfileViewModel(Profile('dummy profile', {}))
        self.profiles = [Profile('Profile1',
                                 rsync_options={'float_option': 42.42, 'bool_option': True,
                                                'string_option': 'some string', 'string_option2': 'some string2',
                                                'int_option': 42}), Profile('Profile2')]
        self._profile_model = QObjectListModel()
        self._profile_model.append(list(map(lambda prof: ProfileViewModel(prof), self.profiles)))
        self._selected_profile_index = 0

    profile_model_changed = pyqtSignal()

    @pyqtProperty(QObjectListModel, constant=True)
    def profile_model(self):
        return self._profile_model

    selected_profile_changed = pyqtSignal()

    @pyqtProperty(ProfileViewModel, notify=selected_profile_changed)
    def selected_profile(self):
        return self._selected_profile

    @pyqtSlot(int)
    def profile_selection_changed(self, index):
        self._selected_profile = self._profile_model[index]
        self._selected_profile_index = index
        self.selected_profile_changed.emit()

    @pyqtSlot()
    def add_new_profile_clicked(self):
        self._profile_model.append(ProfileViewModel(Profile('Profile xx')))

    @pyqtSlot()
    def delete_profile_clicked(self):
        self._profile_model.removeAt(self._selected_profile_index)

    @pyqtSlot()
    def edit_panel_save_clicked(self):
        self._selected_profile.save_changes()

    @pyqtSlot()
    def edit_panel_close_clicked(self):
        self._selected_profile.discard_changes()