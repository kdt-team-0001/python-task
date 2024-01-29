class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.username = kwargs.get("user_name")
        self.email = kwargs.get("email")
        self.address = kwargs.get('address').__dict__
        self.phone = kwargs.get("phone")
        self.website = kwargs.get("website")
        self.company = kwargs.get('company').__dict__

