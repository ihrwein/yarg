import unittest
import os

from yarg import Application


class TestApplication(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.abspath(os.getcwd())
        full_config_path = os.path.join(current_dir, 'yarg.conf')
        self.app = Application(full_config_path)

    def test_load_profiles(self):
        self.assertEqual(len(self.app.get_profiles()), 2)

    def test_load_credentials(self):
        self.assertEqual(len(self.app.get_credentials()), 1)
