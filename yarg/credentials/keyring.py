from yarg.credentials import RemoteCredentials


class Keyring(RemoteCredentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        user = config['username']
        return Keyring(name, user, config)
