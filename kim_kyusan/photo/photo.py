class Photo:
    def __init__(self, album_title, title, url, thumbnail_url):
        '''
        :param kwargs: album_id = 앨범아이디, title = 타이틀, url: 주소 , thumbnail_url= 썸네일 주소
        '''
        self.album_title = album_title
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url


