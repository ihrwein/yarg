from datetime import timezone

from yarg.sshoptions import SSHOptions
from yarg.location import Location


class Profile:
    def __init__(self,
                 name,
                 source=None,
                 destination=None,
                 last_sync=None,
                 rsync_options=None,
                 credentials=None,
                 sshoptions=SSHOptions()):
        if rsync_options is None:
            rsync_options = {}
        self.name = name
        if source is None:
            source = Location()
        self.source = source
        if destination is None:
            destination = Location()
        if source.is_remote and destination.is_remote:
            raise ValueError('Source and destination cannot be both remotes at the same time')
        self.destination = destination
        self.last_sync = last_sync
        if rsync_options is None:
            rsync_options = {}
        self.rsync_options = rsync_options
        self.credentials = credentials
        self.sshoptions = sshoptions

    def dump_as_config(self):
        config = {'name': self.name,
                  'last_sync': self.last_sync.replace(tzinfo=timezone.utc).timestamp(),
                  'rsync_options': self.rsync_options}

        if self.source:
            config['source'] = self.source.dump_as_config()

        if self.destination:
            config['destination'] = self.destination.dump_as_config()

        if self.credentials:
            config['credentials'] = self.credentials

        if self.sshoptions:
            config['ssh'] = self.sshoptions.dump_as_config()

        return config
