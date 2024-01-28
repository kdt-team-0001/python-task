class Todo:
    def __init__(self, **kwargs):
        '''

        :param kwargs: user_id = 사용자 이메일로 찾은 아이디, title = 타이틀, completed : boolen 타입의 true, false
        '''
        self.user_id = kwargs.get("user_id")
        self.title = kwargs.get("title")
        self.completed = kwargs.get("completed")
