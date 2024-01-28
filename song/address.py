class Address:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.suite = kwargs.get('suite')
        self.street = kwargs.get('street')
        self.city = kwargs.get('city')
        self.zipcode = kwargs.get('zipcode')
        self.geo = kwargs.get('geo')