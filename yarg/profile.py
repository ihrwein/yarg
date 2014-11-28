class Profile:

    def __init__(self,
                name,
                source=None,
                destination=None,
                last_sync=None,
                rsync_options=None,
                credentials=None,
                sshoptions=None):
        if rsync_options is None:
            rsync_options = {}

        self.name = name

        if source.is_remote and destination.is_remote:
            raise ValueError('Source and destination cannot be both remotes at the same time')

        self.source = source
        self.destination = destination
        self.last_sync = last_sync
        if rsync_options is None:
            rsync_options = {}
        self.rsync_options = rsync_options
        self.credentials = credentials
        self.sshoptions = sshoptions
