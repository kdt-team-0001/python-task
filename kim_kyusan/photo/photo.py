class Photo:
    def __init__(self, **kwargs):
        '''
        :param kwargs: album_id = 앨범아이디, title = 타이틀, url: 주소 , thumbnail_url= 썸네일 주소
        '''
        self.album_id = kwargs.get('album_id')
        self.title = kwargs.get('title')
        self.url = kwargs.get("url")
        self.thumbnail_url = kwargs.get('thumbnail_url')


