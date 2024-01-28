class Album:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.user = kwargs.get('user')