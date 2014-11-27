import subprocess
from subprocess import Popen

from yarg.profile import Profile
from yarg.synchandler import SyncHandler
from yarg.syncobserver import SyncObserver


class RSyncClient:

    def __init__(self, profile):
        self.profile = profile

        self._command = ['rsync', ]
        self._options = self._create_cli_options_from_profile()

    def _create_cli_options_from_profile(self):
        rsync_options = []
        for key, value in self.profile.rsync_options.items():

            if value is True:
                rsync_options.append("--{0}".format(key))
            elif value not in (None, False):
                rsync_options.append("--{0}={1}".format(key, value))

        src = RSyncClient._format_endpoint(None, self.profile.source.host,
                                           self.profile.source.path)
        dest = RSyncClient._format_endpoint(None, self.profile.destination.host,
                                            self.profile.destination.path)

        rsync_options.extend([src, dest])
        return rsync_options

    @staticmethod
    def _format_endpoint(user, host, path):
        src = ''

        if host:
            if user:
                src = "{0}@"
            src += host + ':'
        return src + path

    def start_sync(self):
        command = []
        command.extend(self._command)
        command.extend(self._options)
        print('RSync CLI options:', ' '.join(command))
        popen = subprocess.call(command, stderr=subprocess.STDOUT)
        return popen

    def _abort_sync(self):
        pass