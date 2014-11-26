from yarg.credentials import Credentials


class PublicKeyCredentials(Credentials):

    @staticmethod
    def create_from_config(config):
        return PublicKeyCredentials()
