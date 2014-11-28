import subprocess


class RSyncClient:

    def __init__(self, profile):
        self.profile = profile

        self._command = ['rsync', ]
        self._options = self._create_cli_options_from_profile()

    def _create_cli_options_from_profile(self):
        rsync_options = []

        if 'rsh' in self.profile.rsync_options and self.profile.rsync_options['rsh'].startswith('ssh'):
            sshcommand = self.profile.rsync_options['rsh']
            port = self.profile.sshoptions.port
            identity_file = self.profile.sshoptions.identity_file

            sshcommand = '{0} -i {1} -p {2}'.format(sshcommand, identity_file, port)
            self.profile.rsync_options['rsh'] = sshcommand

        for key, value in self.profile.rsync_options.items():

            if value is True:
                rsync_options.append("--{0}".format(key))
            elif value not in (None, False):
                rsync_options.append("--{0}={1}".format(key, value))

        suser = self.profile.sshoptions.user if self.profile.source.is_remote else None
        duser = self.profile.sshoptions.user if self.profile.destination.is_remote else None

        if len(self.profile.source.path) > 1:
            rsync_options.extend(self.profile.source.path)
        else:
            src = RSyncClient._format_endpoint(suser, self.profile.source.host,
                                               self.profile.source.path[0])
            rsync_options.append(src)

        dest = RSyncClient._format_endpoint(duser, self.profile.destination.host,
                                            self.profile.destination.path[0])

        rsync_options.append(dest)
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