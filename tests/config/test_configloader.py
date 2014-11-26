import unittest
import os
import os.path

from yarg.config import ConfigLoader


RAW_CONFIG = {
    'credentials': [],
    'profiles': []
}


class TestConfigLoader(unittest.TestCase):

    def test_load_config_from_default_places(self):
        cl = ConfigLoader()
        config = cl.get_raw_config()
        self.assertTrue(os.path.isfile('.yarg.conf'))
        different_items = set(RAW_CONFIG) ^ set(config)
        self.assertEqual(0, len(different_items))
