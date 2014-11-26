from yarg.credentials import Keyring
from yarg.credentials import PublicKeyCredentials
from yarg.credentials import UsernamePasswordCredentials
from yarg.credentials import LocalCredentials


_FACTORY_METHODS = {
    'username_password': UsernamePasswordCredentials.create_from_config,
    'public_key': PublicKeyCredentials.create_from_config,
    'keyring': Keyring.create_from_config,
    'local': LocalCredentials.create_from_config
}


class CredentialsFactory:

    @staticmethod
    def create_from_config(config):
        type = config['type']
        factory_method = _FACTORY_METHODS.get(type)
        return factory_method(config)

