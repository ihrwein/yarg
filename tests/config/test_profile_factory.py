import unittest

from yarg.config import ProfileFactory
from yarg.profile import Profile

class TestProfileFactory(unittest.TestCase):

    def test_create_Profile_instance_from_configuration(self):
        config = {
            'name': 'local',
            'source': {
               'path': '/tmp/source/'
            },
            'destination': {
              'path': '/tmp/target/'
            },
            'last_sync': '2014-11-17 12:12:56.000',
            'rsync_options': {
              'partial': True,
              'force': True,
              'chmod': '600',
              'rsh': 'ssh'
            }
        }
        p = ProfileFactory.create_from_config(config)
        self.assertIsNotNone(p)
        self.assertEqual('local', p.name)
        self.assertIsNotNone(p.source)
        self.assertIsNotNone(p.destination)
