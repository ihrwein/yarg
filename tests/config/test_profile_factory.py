import unittest

from datetime import datetime

from yarg.config import ProfileFactory


class TestProfileFactory(unittest.TestCase):

    def test_create_profile_instance_from_configuration(self):
        config = {
            'name': 'local',
            'source': {
               'path': '/tmp/source/'
            },
            'destination': {
              'path': '/tmp/target/'
            },
            'last_sync': 1417030174.658952,
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
        self.assertIsNotNone(p.rsync_options)
        self.assertEqual('/tmp/source/', p.source.path)
        self.assertEqual('/tmp/target/', p.destination.path)
        self.assertEqual(True, p.rsync_options['partial'])
        self.assertEqual('ssh', p.rsync_options['rsh'])
        self.assertEqual('ssh', p.rsync_options['rsh'])
        self.assertTrue(p.last_sync < datetime.now())
