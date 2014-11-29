import os


class SSHOptions:

    def __init__(self,
                 user=None,
                 port=22,
                 identity_file='~/.ssh/id_rsa',
                 host=None,
                 **kwars):
        self.user = user
        self.port = port
        self.identity_file = os.path.expanduser(identity_file)
        self.host = host
        self.kwargs = kwars

    @staticmethod
    def create_from_config(config):
        port = config.get('port', '22')
        identity_file = config.get('identity_file', '~/.ssh/id_rsa')
        user = config.get('user', None)
        host = config.get('host', None)
        return SSHOptions(user, port=port, identity_file=identity_file, host=host)
