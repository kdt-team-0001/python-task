class Todo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.completed = kwargs.get('completed')
        self.user = kwargs.get('user')