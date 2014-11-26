from yarg.credentials import Credentials


class Keyring(Credentials):

    @staticmethod
    def create_from_config(config):
        return Keyring()
