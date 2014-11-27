from yarg.credentials import RemoteCredentials


class PublicKeyCredentials(RemoteCredentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        user = config['username']
        return PublicKeyCredentials(name, user, config)
