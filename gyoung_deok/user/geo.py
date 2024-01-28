class Geo:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.lat = kwargs["lat"]
        self.lng = kwargs["lng"]

    def __str__(self):
        return f"{self.__dict__}"
