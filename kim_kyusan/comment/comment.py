class Comment:
    def __init__(self, *kwargs):
        '''
        :param kwargs: post_id = 포스트 아이디, name=이름, emmail= 이메일, body = 내용
        '''
        self.post_id = kwargs.get("post_id")
        self.name = kwargs.get("name")
        self.email = kwargs.get('email')
        self.body = kwargs.get('body')