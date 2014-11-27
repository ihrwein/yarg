import time

from threading import Thread
from yarg.synchandler import SyncHandler
from yarg.syncobserver import SyncObserver

POLL_INTERVAL = 0.01


class SyncProxy(SyncHandler, SyncObserver):

    def __init__(self, name, handler_popen, observer, manager):
        self._name = name
        self._handler_popen = handler_popen
        self._orig_observer = observer
        self._manager = manager
        self._observer = None
        self._watcher_thread = Thread(target=self._watch_handler, name=name, args=(self, ), daemon=True)
        self._ended = False

    def _watch_handler(self):
        if not self._ended:
            if self._handler_popen.poll() is None:
                time.sleep(POLL_INTERVAL)
            else:
                retcode = self._handler_popen.retcode
                if retcode == 0:
                    self._completed()
                else:
                    self._failed(str(retcode))
                self._ended = True

    def abort(self):
        self._handler_popen.kill()
        self._ended = True
        self._watcher_thread.join(2 * POLL_INTERVAL)

    def completed(self):
        self._manager.remove_sync()
        self._observer.completed()

    def failed(self, error_code):
        self._manager.remove_sync()
        self._observer.failed()

    def aborted(self):
        self._manager.remove_sync()
        self._observer.aborted()

    def status_update(self, message):
        self._observer.status_update(message)

