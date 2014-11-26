from yarg.credentials.credentials import Credentials
from yarg.credentials.keyring import Keyring
from yarg.credentials.public_key import PublicKeyCredentials
from yarg.credentials.username_password import UsernamePasswordCredentials
from yarg.credentials.local import LocalCredentials


# with this 'hack' we can import the subclasses with:
# from yarg.credentials import GnomeKeyring
