from Apartment import Apartment
from Rental import Rental

class ApartmentRental(Apartment, Rental):
    '''This static method calls the user prompts from the parent classes, Apartment and Rental'''
    @staticmethod
    def prompt_init():
        args = Apartment.prompt_init()
        args.update(Rental.prompt_init())
        return args

    '''This instance method calls the display methods from the parent classes, Apartment and Rental'''
    def display(self):
        Apartment.display(self)
        Rental.display(self)