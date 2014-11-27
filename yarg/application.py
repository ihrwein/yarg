from yarg.config import ConfigLoader
from yarg.rsync import SyncManager


class Application:

    def __init__(self, config_path=None):
        self._config_loader = ConfigLoader(config_path)
        self._profiles = self._config_loader.get_profiles()
        self._credentials = self._config_loader.get_credentials()
        self._sync_manager = SyncManager()

    def add_new_profile(self, profile):
        if profile not in self._profiles:
            self._profiles.append(profile)

    def remove_profile(self, profile):
        if profile in self._profiles:
            self._profiles.remove(profile)

    def sync_profile(self, name, sync_observer):
        profile = self._profiles[name]
        return self._sync_manager.sync_profile(profile, sync_observer)

    def save_configuration(self, ):
        pass

    def get_profiles(self):
        return self._profiles

    def get_credentials(self):
        return self._credentials