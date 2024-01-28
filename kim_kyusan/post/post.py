class Post:
    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.body = kwargs.get('body')