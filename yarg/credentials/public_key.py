from yarg.credentials import Credentials


class PublicKeyCredentials(Credentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        return PublicKeyCredentials(name, config)
