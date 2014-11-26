from yarg.credentials import Credentials


class UsernamePasswordCredentials(Credentials):

    @staticmethod
    def create_from_config(config):
        return UsernamePasswordCredentials()
