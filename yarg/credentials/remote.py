from yarg.credentials import Credentials


class RemoteCredentials(Credentials):

    def __init__(self, name, user, config):
        super().__init__(name, config)
        self.user = user

    @staticmethod
    def create_from_config(config):
        name = config['name']
        user = config['username']
        return RemoteCredentials(name, user, config)
