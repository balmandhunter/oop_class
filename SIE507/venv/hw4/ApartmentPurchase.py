from Apartment import Apartment
from Purchase import Purchase

class ApartmentPurchase(Apartment, Purchase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)