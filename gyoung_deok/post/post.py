class Post:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.body = kwargs["body"]
        self.user = kwargs["user"].__dict__

    def __str__(self):
        return f'{self.__dict__}'
