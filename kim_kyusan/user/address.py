class Address:
    def __init__(self,**kwargs):
        '''

        :param kwargs: id, street, suite, city, zipcode
        '''
        self.id = kwargs.get("id")
        self.street = kwargs.get("street")
        self.suite= kwargs.get("suite")
        self.city = kwargs.get("city")
        self.zipcode = kwargs.get("zipcode")
        self.lat = kwargs.get("lat")
        self.lng = kwargs.get("lng")
        # self.geo = kwargs.get("Geo").__dict__
