import datetime
from yarg.profile import Profile
from yarg.config import LocationFactory
from yarg.sshoptions import SSHOptions


class ProfileFactory:

    @staticmethod
    def create_from_config(config):
        name = config['name']
        source = LocationFactory.create_from_config(config['source'])
        destination = LocationFactory.create_from_config(config['destination'])
        rsync_options = config.get('rsync_options', {})

        if 'last_sync' not in config:
            last_sync = None
        else:
            last_sync = datetime.datetime.fromtimestamp(config.get('last_sync'))

        sshoptions = SSHOptions.create_from_config(config.get('ssh', {}))
        return Profile(name, source=source, destination=destination,
                       last_sync=last_sync, rsync_options=rsync_options,
                       sshoptions=sshoptions)
