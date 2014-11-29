import yaml

from datetime import timezone


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

    def _dump_location(self, location):
        l = {}

        if location.path:
            l['path'] = location.path

        if location.is_remote is not None:
            l['remote'] = location.is_remote

        if location.host is not None:
            l['host'] = location.host

        return l

    def _dump_profiles(self):
        profiles = []
        for k, v in self._profiles.items():
            p = {'name': v.name,
                 'source': self._dump_location(v.source),
                 'destination': self._dump_location(v.destination),
                 'last_sync': v.last_sync.replace(tzinfo=timezone.utc).timestamp(),
                 'rsync_options': v.rsync_options}

            if v.credentials:
                p['credentials'] = v.credentials

            if v.sshoptions:
                o = {'port': v.sshoptions.port,
                     'identity_file': v.sshoptions.identity_file}

                if v.sshoptions.user:
                    o['user'] = v.sshoptions.user

                p['ssh'] = o
            profiles.append(p)
        return profiles
