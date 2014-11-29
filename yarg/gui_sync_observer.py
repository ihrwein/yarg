from yarg.syncobserver import SyncObserver


class GuiSyncObserver(SyncObserver):
    def __init__(self, profile_view_model=None, gui_controller=None):
        self._gui_controller = gui_controller
        self.profile_view_model = profile_view_model

    def completed(self):
        self._gui_controller.sync_completed(self.profile_view_model)

    def failed(self, error_code):
        self._gui_controller.sync_failed(self.profile_view_model)

    def status_update(self, message):
        pass

    def aborted(self):
        pass
