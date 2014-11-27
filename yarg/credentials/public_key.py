import os

from yarg.credentials import RemoteCredentials


class PublicKeyCredentials(RemoteCredentials):

    def __init__(self, name, user, identity_file, config):
        super().__init__(name, user, config)
        self.identity_file = identity_file

    @staticmethod
    def create_from_config(config):
        name = config['name']
        user = config.get('username', None)
        identity_file = os.path.expanduser(config.get('identity_file', '~/.ssh/id_rsa'))
        return PublicKeyCredentials(name, user, identity_file, config)
