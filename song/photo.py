class Photo:
    def __init__(self, **kwargs):
        self.album_id = kwargs.get('album_id')
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.url = kwargs.get('url')
        self.thumbnail_url = kwargs.get('thumbnail_url')
