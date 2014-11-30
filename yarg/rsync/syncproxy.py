import time
import datetime
from threading import Thread

from yarg.synchandler import SyncHandler
from yarg.syncobserver import SyncObserver


POLL_INTERVAL = 0.1


class SyncProxy(SyncHandler, SyncObserver):
    def __init__(self, profile, handler_popen, observer, manager):
        self._profile = profile
        self._handler_popen = handler_popen
        self._manager = manager
        self._observer = observer
        self._watcher_thread = Thread(target=self._watch_handler, name=self._profile.name, daemon=True)
        self._watcher_thread.start()

    def _watch_handler(self):
        print('Sync watcher thread started')
        while self._handler_popen.poll() is None:
            print('Polling rsync')
            time.sleep(POLL_INTERVAL)
        print('Rsync exited')
        retcode = self._handler_popen.poll()
        if retcode == 0:
            self.completed()
        else:
            self.failed(str(retcode))

    def abort(self):
        self._handler_popen.kill()
        self._watcher_thread.join(2 * POLL_INTERVAL)

    def completed(self):
        print('Sync completed')
        self._manager.remove_sync(self._profile.name)
        self._profile.last_sync = datetime.datetime.now()
        self._observer.completed()

    def failed(self, error_code):
        self._manager.remove_sync(self._profile.name)
        self._observer.failed(error_code)

    def aborted(self):
        self._manager.remove_sync()
        self._observer.aborted()

    def status_update(self, message):
        self._observer.status_update(message)

