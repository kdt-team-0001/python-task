class Geo:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.lat = kwargs.get('lat')
        self.lng = kwargs.get('lng')