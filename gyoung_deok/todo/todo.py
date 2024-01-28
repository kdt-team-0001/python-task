from study_python.gyoung_deok.user.user import User


class Todo:
    def __init__(self, id: int, title: str, completed: bool, user: User):
        self.id = id
        self.title = title
        self.completed = completed
        self.user = user.__dict__

    def __str__(self):
        return f'id{self.__dict__}'
