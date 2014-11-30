import unittest

from yarg.config import ConfigSaver
from yarg.config import ConfigLoader


class TestConfigSaver(unittest.TestCase):

    def test_save_loaded_config(self):
        cl = ConfigLoader('yarg.conf')
        profiles = cl.get_profiles()
        saver = ConfigSaver('_yarg.conf', profiles, cl.get_default_rsync_options())
        saver.save()


