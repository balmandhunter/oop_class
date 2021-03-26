class Rental:
    def __init__(self, furnished=False, utilities=0, rent=0, **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    '''This instance method prints rental information'''
    def display(self):
        print('Furnished: ' + str(self.furnished) + '\n' +
              'Utilities Included: ' + str(self.utilities) + '\n'
              'Rent ($): ' + str(self.rent))

    '''This static method prompts the user for information about the rental and returns it, so that 
    it can be passed as arguments to a new object'''
    @staticmethod
    def prompt_init():
        # return {'furnished': input("Is the property furnished?:"),
        #          'utilities': input("Does the rent include utilities?:"),
        #          'rent': input("What is the amount of the rent?:")}
        return {'furnished': True,
                 'utilities': False,
                 'rent': 1200}