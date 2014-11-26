class Profile:

    def __init__(self,
                name,
                source=None,
                destination=None,
                last_sync=None,
                rsync_options=None):
        self.name = name
        self.source = source
        self.destination = destination
        self.last_sync = last_sync
        self.rsync_options = rsync_options
