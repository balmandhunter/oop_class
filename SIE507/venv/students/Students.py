from Person import Person

class Student(Person):
    def __init__(self, id="", program="", **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.program = program

    def print_program(self):
        print(self.program)
