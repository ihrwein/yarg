from yarg.credentials import Credentials


class UsernamePasswordCredentials(Credentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        return UsernamePasswordCredentials(name, config)
