class Location:

    def __init__(self,
                 path,
                 is_remote=False):
        self.path = path
        self.is_remote = is_remote

    def dump_as_config(self):
        l = {'remote': self.is_remote}

        if self.path:
            l['path'] = self.path

        return l
