from Students import Student

class OnlineStudent(Student):
    def __init__(self, home_address="", **kwargs):
        super().__init__(**kwargs)
        self.home_address = home_address

    def print_address(self):
        print(self.home_address)

    def print_program(self):
        print(self.program)

    def print_name(self):
        print(self.firstname, self.lastname)

    def print_age(self):
        print(self.age)

    def print_thesis_option(self):
        if self.is_thesis == 1:
            print('Student will write thesis')
        else:
            print('Student is working on a non-thesis masters')