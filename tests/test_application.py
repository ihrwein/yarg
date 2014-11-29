import unittest
import os

import yarg.application
from unittest import mock
from yarg import Application
from yarg.syncobserver import SyncObserver



class TestApplication(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.abspath(os.getcwd())
        full_config_path = os.path.join(current_dir, 'yarg.conf')
        self.app = yarg.application.instance(full_config_path)

    def test_load_profiles(self):
        self.assertEqual(len(self.app.get_profiles()), 2)

    def test_load_credentials(self):
        self.assertEqual(len(self.app.get_credentials()), 1)

    def test_sync_profile(self):
        so = SyncObserver()
        so.aborted = mock.Mock()
        so.completed = mock.Mock()
        so.failed = mock.Mock()
        so.status_update = mock.Mock()
        profile1 = list(self.app.get_profiles().keys())[0]
        self.app.sync_profile(profile1, so)
        so.aborted.assert_called_once()
        self.assertFalse(so.aborted.called)
        self.assertFalse(so.failed.called)
