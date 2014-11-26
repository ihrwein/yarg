class Application:

    def __init__(self):
        self._profiles = []

    def add_new_profile(self, profile):
        if profile not in self._profiles:
            self._profiles.append(profile)

    def remove_profile(self, profile):
        if profile in self._profiles:
            self._profiles.remove(profile)

    def sync_profile(self, name, sync_observer):
        pass

    def save_configuration(self, ):
        pass

    def get_profiles(self):
        return self._profiles