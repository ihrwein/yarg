import unittest
import os

from yarg import Application


class TestApplication(unittest.TestCase):

    def test_load_profiles(self):
        current_dir = os.path.abspath(os.getcwd())
        full_config_path = os.path.join(current_dir, 'yarg.conf')
        a = Application(full_config_path)
        self.assertEqual(len(a.get_profiles()), 2)
