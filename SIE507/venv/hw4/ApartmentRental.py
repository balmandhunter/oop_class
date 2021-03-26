from Apartment import Apartment
from Rental import Rental

class ApartmentRental(Apartment, Rental):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)