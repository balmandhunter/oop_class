from House import House
from Purchase import Purchase

class HousePurchase(House, Purchase):
    '''This static method calls the user prompts from the parent classes, House and Purchase'''
    @staticmethod
    def prompt_init():
        args = House.prompt_init()
        args.update(Purchase.prompt_init())
        return args

    '''This instance method calls the display methods from the parent classes, House and Purchase'''
    def display(self):
        House.display(self)
        Purchase.display(self)