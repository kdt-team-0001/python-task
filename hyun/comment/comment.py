class Comment:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.body = kwargs.get('body')
        self.post = kwargs.get('post')