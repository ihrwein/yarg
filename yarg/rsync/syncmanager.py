from yarg.rsync import RSyncClient
from yarg.rsync import SyncProxy


class SyncManager:

    def __init__(self):
        self._active_syncs = {}

    def sync_profile(self, profile, sync_observer):
        name = profile.name
        if name not in self._active_syncs.keys():
            client = RSyncClient(profile)

            popen = client.start_sync()
            sp = SyncProxy(name=name,
                           handler_popen=popen,
                           observer=sync_observer,
                           manager=self)

            self._active_syncs[name] = ActiveSync(sp, client)

            return sp

    def remove_sync(self, name):
        self._active_syncs.pop(name, None)


class ActiveSync:

    def __init__(self, proxy, client):
        self.proxy = proxy
        self.client = client