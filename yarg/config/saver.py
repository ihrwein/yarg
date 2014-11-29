import yaml


class ConfigSaver:
    def __init__(self,
                 path,
                 profiles,
                 credentials,
                 default_rsync_options):
        self._path = path
        self._profiles = profiles
        self._credentials = credentials
        self._default_rsync_options = default_rsync_options

    def save(self):
        credentials = self._dump_credentials()
        profiles = self._dump_profiles()
        default_rsync_options = self._dump_default_rsync_options()
        root = {'credentials': credentials,
                'default_rsync_options': default_rsync_options,
                'profiles': profiles}
        with open(self._path, 'wt') as f:
            yaml.dump(root, f, default_flow_style=False)

    def _dump_default_rsync_options(self):
        return self._default_rsync_options

    def _dump_credentials(self):
        credentials = []
        for k, v in self._credentials.items():
            c = {}

            if v:
                if v.name:
                    c['name'] = v.name

                if v.config.get('type', None):
                    c['type'] = v.config.get('type')

                credentials.append(c)
        return credentials

    def _dump_profiles(self):
        profiles = []
        for k, v in self._profiles.items():
            config = v.dump_as_config()
            profiles.append(config)
        return profiles
