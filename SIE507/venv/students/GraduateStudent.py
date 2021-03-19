from Students import Student

class GraduateStudent(Student):
    def __init__(self, is_thesis=0, **kwargs):
        super().__init__(**kwargs)
        self.is_thesis = is_thesis

    def print_thesis_option(self):
        if self.is_thesis == 1:
            print('Student will write thesis')
        else:
            print('Student is working on a non-thesis masters')