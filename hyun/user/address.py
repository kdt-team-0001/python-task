

class Address:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.street = kwargs.get('street')
        self.suite = kwargs.get('suite')
        self.city = kwargs.get('city')
        self.zipcode = kwargs.get('zipcode')
        self.geo = kwargs.get('geo')

