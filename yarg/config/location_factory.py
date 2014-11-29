from yarg.location import Location


class LocationFactory:

    @staticmethod
    def create_from_config(config):
        path = config['path']
        is_remote = config.get('remote', False)
        return Location(path, is_remote=is_remote)
