class Comment:
    def __init__(self, **kwargs):
        '''
        :param kwargs: title = 포스트 타이틀, name=이름, emmail= 이메일, body = 내용
        '''
        self.title = kwargs.get("title")
        self.name = kwargs.get("name")
        self.email = kwargs.get('email')
        self.body = kwargs.get('body')