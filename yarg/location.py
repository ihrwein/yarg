class Location:

    def __init__(self,
                 path,
                 host=None,
                 port=None,
                 credentials=None):
        self.host = host
        self.port = port
        self.path = path
        self.credentials = credentials
