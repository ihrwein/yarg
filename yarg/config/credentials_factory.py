from yarg.credentials import Keyring
from yarg.credentials import UsernamePasswordCredentials


_FACTORY_METHODS = {
    'username_password': UsernamePasswordCredentials.create_from_config,
    'keyring': Keyring.create_from_config,
}


class CredentialsFactory:

    @staticmethod
    def create_from_config(config):
        type = config['type']

        factory_method = _FACTORY_METHODS.get(type)
        if factory_method:
            factory_method(config)
        else:
            return None

