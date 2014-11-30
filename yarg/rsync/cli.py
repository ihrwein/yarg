class CLIOptions:

    def __init__(self, profile):
        self._command = 'rsync'
        self.profile = profile

    def get_command_and_options(self):
        rsync_options = [self._command, ]

        if 'rsh' not in self.profile.rsync_options:
            self.profile.rsync_options['rsh'] = 'ssh'

        if 'rsh' in self.profile.rsync_options and self.profile.rsync_options['rsh'].startswith('ssh'):
            sshcommand = self.profile.rsync_options['rsh']
            port = self.profile.sshoptions.port
            identity_file = self.profile.sshoptions.identity_file

            if '' != identity_file and identity_file is not None:
                sshcommand += ' -i {0}'.format(identity_file)

            if '' != port and port is not None:
                sshcommand += ' -p {0}'.format(port)

            self.profile.rsync_options['rsh'] = sshcommand

        for key, value in self.profile.rsync_options.items():

            if value is True:
                rsync_options.append("--{0}".format(key))
            elif value not in (None, False):
                rsync_options.append("--{0}={1}".format(key, value))

        suser = self.profile.sshoptions.user if self.profile.source.is_remote else None
        duser = self.profile.sshoptions.user if self.profile.destination.is_remote else None

        if not self.profile.source.is_remote:
            rsync_options.extend(self.profile.source.path)
        elif len(self.profile.source.path) == 1 and self.profile.source.is_remote:
            src = CLIOptions._format_endpoint(suser, self.profile.sshoptions.host,
                                              self.profile.source.path[0])
            rsync_options.append(src)
        else:
            raise ValueError('If a source location is a remote, it can contain only one path')

        if self.profile.destination.is_remote:
            dest = CLIOptions._format_endpoint(duser, self.profile.sshoptions.host,
                                               self.profile.destination.path[0])
            rsync_options.append(dest)

        return rsync_options

    @staticmethod
    def _format_endpoint(user, host, path):
        src = ''

        if host:
            if user and user != '':
                src = "{0}@".format(user)
            src += host + ':'
        return src + path
