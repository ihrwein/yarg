import os


class SSHOptions:

    def __init__(self,
                 user=None,
                 port=22,
                 identity_file='~/.ssh/id_rsa',
                 host=None):
        self.user = user
        self.port = port
        self.identity_file = os.path.expanduser(identity_file)
        self.host = host

    def dump_as_config(self):
        config = {'port': self.port,
                  'identity_file': self.identity_file}

        if self.user:
            config['user'] = self.user

        if self.host is not None:
            config['host'] = self.host

        return config



    @staticmethod
    def create_from_config(config):
        port = config.get('port', '22')
        identity_file = config.get('identity_file', '~/.ssh/id_rsa')
        user = config.get('user', None)
        host = config.get('host', None)
        return SSHOptions(user, port=port, identity_file=identity_file, host=host)
