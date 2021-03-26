from House import House
from Purchase import Purchase

class HousePurchase(House, Purchase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)