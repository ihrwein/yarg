from PyQt5.QtCore import pyqtProperty, pyqtSignal, pyqtSlot, QObject

import yarg
from yarg.gui.profile_view_model import ProfileViewModel
from yarg.gui.listmodel import QObjectListModel
from yarg.gui.source_path_view_model import SourcePathViewModel
from yarg.gui_sync_observer import GuiSyncObserver
from yarg.location import Location
from yarg.profile import Profile


class MainController(QObject):
    def __init__(self, parent=None):
        super(MainController, self).__init__(parent)
        # self._selected_profile = ProfileViewModel(
        #     Profile('dummy profile', source=Location(path=['']), destination=Location(path=[''])))
        self._new_profile = None
        self._application = yarg.application.instance()
        self._profile_model = QObjectListModel()
        profile_list = sorted(self._application.get_profiles().items(), key=lambda prof: str.lower(prof[1].name))
        self._profile_model.append(list(map(lambda prof: ProfileViewModel(prof[1]), profile_list)))
        self._selected_profile_index = 0
        self._synchronizations_in_progress = {}

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
    def add_source_path_clicked(self):
        self.selected_profile.source_paths.append(SourcePathViewModel(''))

    @pyqtSlot(int)
    def remove_source_path_clicked(self, index):
        self.selected_profile.source_paths.removeAt(index)

    @pyqtSlot()
    def add_new_profile_clicked(self):
        num = 1
        while self._application.get_profiles().get('New profile ' + str(num), None) is not None:
            num += 1
        profile = Profile('New profile ' + str(num), source=Location(path=['']), destination=Location(path=['']))
        self._application.add_new_profile(profile)
        self.profile_model.append(ProfileViewModel(model=profile))
        self._application.save_configuration()

    @pyqtSlot()
    def delete_profile_clicked(self):
        self._application.remove_profile(self._selected_profile.name)
        self._profile_model.removeAt(self._selected_profile_index)
        self._application.save_configuration()

    @pyqtSlot()
    def edit_panel_save_clicked(self):
        self._selected_profile.save_changes()
        self._application.save_configuration()

    @pyqtSlot()
    def edit_panel_close_clicked(self):
        self._selected_profile.discard_changes()

    @pyqtSlot()
    def sync_clicked(self):
        if self._synchronizations_in_progress.get(self.selected_profile.name, None) is None:
            observer = GuiSyncObserver(self.selected_profile, self)
            handler = self._application.sync_profile(self.selected_profile.name, sync_observer=observer)
            self._synchronizations_in_progress[self.selected_profile.name] = handler
            self.selected_profile.sync_in_progress = True
        else:
            print('sync already in progress')

    @pyqtSlot(str)
    def abort_sync_clicked(self, profile_name):
        handler = self._synchronizations_in_progress.get[profile_name]
        handler.abort()

    def sync_aborted(self, profile_view_model):
        self._synchronizations_in_progress.pop(profile_view_model.name, None)
        self.selected_profile.sync_in_progress = False

    def sync_completed(self, profile_view_model):
        print('{0} : sync completed'.format(profile_view_model.name))
        self._synchronizations_in_progress.pop(profile_view_model.name, None)
        profile_view_model.sync_in_progress = False
        profile_view_model.last_sync = profile_view_model.model.last_sync
        profile_view_model.out_of_sync_changed.emit()
        self._application.save_configuration()

    def sync_failed(self, profile_view_model):
        print('{0} : sync failed'.format(profile_view_model.name))
        self._synchronizations_in_progress.pop(profile_view_model.name, None)
        self.selected_profile.sync_in_progress = False