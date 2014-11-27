from yarg.credentials import RemoteCredentials


class UsernamePasswordCredentials(RemoteCredentials):

    @staticmethod
    def create_from_config(config):
        name = config['name']
        user = config['username']
        return UsernamePasswordCredentials(name, user, config)
