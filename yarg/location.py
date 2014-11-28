class Location:

    def __init__(self,
                 path,
                 host=None,
                 is_remote=False):
        self.host = host
        self.path = path
        self.is_remote = is_remote
