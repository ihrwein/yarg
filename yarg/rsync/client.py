import subprocess
import yarg.application
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
        credentials = yarg.application.instance().get_credentials()

        suser = duser = None
        scred = credentials.get(self.profile.source.credentials, None)
        dcred = credentials.get(self.profile.destination.credentials, None)

        identity_file = None
        port = None

        if scred and scred.config.get('type', None) == 'public_key':
            identity_file = scred.identity_file

        if dcred and dcred.config.get('type', None) == 'public_key':
            identity_file = dcred.identity_file

        if self.profile.source.port:
            port = self.profile.source.port

        if self.profile.destination.port:
            port = self.profile.destination.port

        if 'rsh' in self.profile.rsync_options and self.profile.rsync_options['rsh'] == 'ssh':
            if identity_file:
                self.profile.rsync_options['rsh'] = '/usr/bin/ssh -i {0}'.format(identity_file)

            if port:
                self.profile.rsync_options['rsh'] += ' -p {0}'.format(port)

        for key, value in self.profile.rsync_options.items():

            if value is True:
                rsync_options.append("--{0}".format(key))
            elif value not in (None, False):
                rsync_options.append("--{0}={1}".format(key, value))

        if scred:
            suser = scred.user

        if dcred:
            duser = dcred.user

        src = RSyncClient._format_endpoint(suser, self.profile.source.host,
                                           self.profile.source.path)
        dest = RSyncClient._format_endpoint(duser, self.profile.destination.host,
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
        joined = ' '.join(command)
        print('RSync CLI options:', joined)
        popen = subprocess.call(command, stderr=subprocess.STDOUT)
        return popen

    def _abort_sync(self):
        pass