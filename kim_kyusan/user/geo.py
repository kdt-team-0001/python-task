class Geo:
    def __init__(self,**kwargs):
        '''
        :param kwargs: id = 아이디, lat : 위도 , lng :경도
        '''
        self.id = kwargs.get('id')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get("lng")

