class Post:
    def __init__(self, id: int, title: str, body: str, user: dict):
        self.id = id
        self.title = title
        self.body = body
        self.user = user

    def __str__(self):
        return f'{self.__dict__}'
