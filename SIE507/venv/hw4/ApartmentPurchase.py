from Apartment import Apartment
from Purchase import Purchase

class ApartmentPurchase(Apartment, Purchase):
    '''This static method calls the user prompts from the parent classes, Apartment and Purchase'''
    @staticmethod
    def prompt_init():
        args = Apartment.prompt_init()
        args.update(Purchase.prompt_init())
        return args

    '''This instance method calls the display methods from the parent classes, apartment and purchase'''
    def display(self):
        Apartment.display(self)
        Purchase.display(self)

