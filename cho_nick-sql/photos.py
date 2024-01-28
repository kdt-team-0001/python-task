class Photos:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.url = kwargs.get('url')
        self.thumbnail_url = kwargs.get('thumbnail_url')
        self.album_id = kwargs.get('album_id')

