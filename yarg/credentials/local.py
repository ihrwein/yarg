from yarg.credentials import Credentials


class LocalCredentials(Credentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        return LocalCredentials(name)
