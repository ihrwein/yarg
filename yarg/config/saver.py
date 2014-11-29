import yaml


class ConfigSaver:
    def __init__(self,
                 path,
                 profiles,
                 credentials):
        self._path = path
        self._profiles = profiles
        self._credentials = credentials

    def save(self):
        credentials = self._dump_credentials()
        profiles = self._dump_profiles()
        root = {'credentials': credentials, 'profiles': profiles}
        print(yaml.dump(root, default_flow_style=False))

    def _dump_credentials(self):
        credentials = []
        for k, v in self._credentials.items():
            c = {}

            if v:
                if v.name:
                    c['name'] = v.name

                credentials.append(c)
        return credentials

    def _dump_profiles(self):
        profiles = []
        for k, v in self._profiles.items():
            config = v.dump_as_config()
            profiles.append(config)
        return profiles
