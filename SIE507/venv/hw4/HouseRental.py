from House import House
from Rental import Rental

class HouseRental(House, Rental):
    '''This static method '''
    @staticmethod
    def prompt_init(self):
        args = House.prompt_init()
        args.update(Rental.prompt_init())
        return args

    def display(self):
        House.display(self)
        Rental.display(self)
