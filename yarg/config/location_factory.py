from yarg.location import Location


class LocationFactory:

    @staticmethod
    def create_from_config(config):
        path = config['path']
        host = config.get('host', None)
        is_remote = config.get('remote', False)
        return Location(path, host=host, is_remote=is_remote)
