class Rental:
    def __init__(self, furnished=False, utilities=0, rent=0, **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    '''This instance method prints the rent'''
    def display(self):
        print('Transaction Type: Rental')
        print('Rent ($): ' + str(self.rent))

    '''This class method gets and validates user input for rental information.'''
    @classmethod
    def prompt_init(self):
        furnished = input("Is the property furnished (yes or no)?:")
        while furnished.lower() not in ['yes', 'no']:
            print('Invalid Input')
            furnished = input("Is the property furnished (yes or no)?:")

        utilities = input("Does the rent include utilities (yes or no)?:")
        while utilities.lower() not in ['yes', 'no']:
            print('Invalid Input')
            utilities = input("Does the rent include utilities (yes or no)?:")

        rent = input("What is the amount of the rent?:")
        while rent.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            rent = input("What is the amount of the rent?:")

        info_dict = {'furnished': furnished,
                      'utilities': utilities,
                      'rent': rent}

        return info_dict