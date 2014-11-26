from yarg.credentials import Credentials


class Keyring(Credentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        return Keyring(name, config)
