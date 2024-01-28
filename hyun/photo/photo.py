class Photo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.url = kwargs.get('url')
        self.thumbnailurl = kwargs.get('thumbnailurl')
        self.album = kwargs.get('album')