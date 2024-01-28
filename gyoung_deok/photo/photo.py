from study_python.gyoung_deok.album.album import Album


class Photo:
    def __init__(self, id: int, title: str, url: str, thumbnail_url: str, album: Album):
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.album = album.__dict__

    def __str__(self):
        return f"{self.__dict__}"
