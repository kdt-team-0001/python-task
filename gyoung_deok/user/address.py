from study_python.gyoung_deok.user.geo import *
class Address:
    def __init__(self, id, street: str, suite: str, city: str, zipcode: str, geo: dict):
        self.id = id
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo

    def __str__(self):
        return f'{self.__dict__}'
