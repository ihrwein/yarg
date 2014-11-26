import datetime
from yarg.profile import Profile
from yarg.config import LocationFactory

class ProfileFactory:

    @staticmethod
    def create_from_config(config):
        name = config['name']
        source = LocationFactory.create_from_config(config['source'])
        destination = LocationFactory.create_from_config(config['destination'])
        rsync_options = config.get('rsync_options', {})
        # TODO use config file
        last_sync = datetime.datetime.fromtimestamp(config.get('last_sync'), None)
        return Profile(name, source=source, destination=destination,
                       last_sync=last_sync, rsync_options=rsync_options)
