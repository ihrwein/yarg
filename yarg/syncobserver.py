class SyncObserver:

    def completed(self):
        pass

    def failed(self, error_code):
        pass

    def status_update(self, message):
        pass

    def aborted(self):
        pass
