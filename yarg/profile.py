class Profile:

    def __init__(self,
                name,
                source=None,
                destination=None,
                last_sync=None,
                rsync_options=None):
        if rsync_options is None:
            rsync_options = {}

        self.name = name
        self.source = source
        self.destination = destination
        self.last_sync = last_sync
        if rsync_options is None:
            rsync_options = {}
        self.rsync_options = rsync_options
