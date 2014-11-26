import os
import os.path
import yaml

from yarg.config.profile_factory import ProfileFactory
from yarg.config import CredentialsFactory


class ConfigLoader:

    def __init__(self,
                 path=None):
        paths = self._get_config_file_paths(path)
        self._config = self._load_first_available_config(paths)
        self._profiles = self._parse_profiles()
        self._credentials = self._parse_credentials()
        self._path = ''

    def _parse_config(self, key, factory_method):
        items = {}
        for i in self._config.get(key, {}):
            c = factory_method(i)
            items[i['name']] = c

        return items

    def _parse_credentials(self):
        return self._parse_config('credentials', CredentialsFactory.create_from_config)

    def _parse_profiles(self):
        return self._parse_config('profiles', ProfileFactory.create_from_config)

    def _get_config_file_paths(self, first_path=None):
        conffile_name = '.yarg.conf'
        home_dir = os.getenv('HOME')

        cwd_conf = os.path.join(os.path.abspath(os.path.curdir),
                                conffile_name)
        home_conf = os.path.join(home_dir, conffile_name)
        confdir_conf = os.path.join(home_dir, '.config', 'yarg', conffile_name)

        paths = [cwd_conf, home_conf, confdir_conf]

        if first_path is not None:
            paths.insert(0, first_path)

        return paths

    def _load_first_available_config(self, paths):
        existing_paths = list(filter(lambda p: os.path.isfile(p), paths))

        config = {}

        for i in existing_paths:
            try:
                with open(i, 'r') as f:
                    config = yaml.load(f)
                    break
            except IOError as err:
                print(err)

        return config

    def get_raw_config(self):
        return self._config

    def get_profiles(self):
        return self._profiles

    def get_credentials(self):
        return self._credentials
