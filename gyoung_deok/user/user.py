from study_python.gyoung_deok.user.address import *
from study_python.gyoung_deok.user.company import *

class User:
    def __init__(self, id: int, name: str, username: str, email: str, phone: str, website: str, address: dict, company: dict):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website
        self.address = address
        self.company = company

    def __str__(self):
        return f'{self.__dict__}'
