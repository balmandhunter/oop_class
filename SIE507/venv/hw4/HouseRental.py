from House import House
from Rental import Rental

class HouseRental(House, Rental):
    '''This class method calls the user prompts from the parent classes, House and Rental'''
    @classmethod
    def prompt_init(cls):
        args = House.prompt_init()
        args.update(Rental.prompt_init())
        return args

    '''This instance method calls the displat methods from the parent classes, house and rental'''
    def display(self):
        House.display(self)
        Rental.display(self)
