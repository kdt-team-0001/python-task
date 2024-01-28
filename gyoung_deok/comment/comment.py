from study_python.gyoung_deok.post.post import Post


class Comment:
    def __init__(self, id: int, name: str, email: str, body: str, post: Post):
        self.id = id
        self.name = name
        self.email = email
        self.body = body
        self.post = post.__dict__

    def __str__(self):
        return f'{self.__dict__}'
