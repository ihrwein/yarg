import yaml


class ConfigSaver:
    def __init__(self,
                 path,
                 profiles,
                 default_rsync_options):
        self._path = path
        self._profiles = profiles
        self._default_rsync_options = default_rsync_options

    def save(self):
        profiles = self._dump_profiles()
        default_rsync_options = self._dump_default_rsync_options()
        root = {'default_rsync_options': default_rsync_options,
                'profiles': profiles}
        with open(self._path, 'wt') as f:
            yaml.dump(root, f, default_flow_style=False)

    def _dump_default_rsync_options(self):
        return self._default_rsync_options

    def _dump_profiles(self):
        profiles = []
        for k, v in self._profiles.items():
            config = v.dump_as_config()
            profiles.append(config)
        return profiles
