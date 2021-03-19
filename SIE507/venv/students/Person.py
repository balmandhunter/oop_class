class Person():
    def __init__(self, firstname="", lastname="", age="", **kwargs):
        super().__init__(**kwargs)
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print_name(self):
        print(self.firstname + ' ' + self.lastname)