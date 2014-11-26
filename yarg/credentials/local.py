from yarg.credentials import Credentials


class LocalCredentials(Credentials):

    def __init__(self, name, params=None):
        super().__init__(name, params=None)

    @staticmethod
    def create_from_config(config):
        name = config['name']
        return LocalCredentials(name)
