from yarg.location import Location


class LocationFactory:

    @staticmethod
    def create_from_config(config):
        path = config['path']
        host = config.get('host', None)
        port = config.get('port', None)
        credentials = config.get('credentials', None)
        return Location(path, host=host, port=port, credentials=credentials)
