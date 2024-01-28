from study_python.gyoung_deok.user.user import User


class Album:
    def __init__(self, id: int, title: str, user: User):
        self.id = id
        self.title = title
        self.user = user.__dict__

    def __str__(self):
        return f'{self.__dict__}'
