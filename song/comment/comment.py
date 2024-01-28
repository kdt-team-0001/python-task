class Comment:
    def __init__(self, **kwargs):
        self.post_id = kwargs.get('post_id')
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.body = kwargs.get('body')
