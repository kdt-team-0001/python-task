class Company:
    def __init__(self, **kwargs):
        '''

        :param kwargs: id, name, catch_phrase, bs
        '''
        self.id = kwargs.get('id')
        self.name = kwargs.get("name")
        self.catch_phrase = kwargs.get("catch_phrase")
        self.bs = kwargs.get("bs")