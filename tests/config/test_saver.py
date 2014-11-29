import unittest

from yarg.config import ConfigSaver
from yarg.config import ConfigLoader


class TestConfigSaver(unittest.TestCase):

    def test_save_loaded_config(self):
        cl = ConfigLoader('yarg.conf')
        profiles = cl.get_profiles()
        credentials = cl.get_credentials()
        saver = ConfigSaver('_yarg.conf', profiles, credentials)
        saver.save()


