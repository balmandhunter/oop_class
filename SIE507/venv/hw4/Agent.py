from HouseRental import HouseRental
from HousePurchase import HousePurchase
from ApartmentPurchase import ApartmentPurchase
from ApartmentRental import ApartmentRental

class Agent():
    # this only gets run once, when the file is initially read, so it doesn't reinitialize the
    # list every time you create a new object
    agent_list = []

    def __init__(self, property_list=[], agent_name="", **kwargs):
        super().__init__(**kwargs)
        self.property_list = property_list
        self.agent_name = agent_name
        self.agent_list.append(self)
        self.property_type = 'house'
        self.purchase_type = 'rental'

    def print_agent_list(self):
        print(self.agent_list)

    def list_properties(self, show_all=False):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type_dict = {('house', 'rental'): HouseRental,
                              ('house', 'purchase'): HousePurchase,
                              ('apartment', 'purchase'): ApartmentPurchase,
                              ('apartment', 'rental'): ApartmentRental}
        # self.property_type = input("Is the property a house or apartment?").lower()
        # self.purchase_type = input("Is the listing for a rental or purchase?").lower()
        PropertyClass = property_type_dict[(self.property_type, self.purchase_type)]
        kwargs = PropertyClass.prompt_init(self)
        self.property_list.append(PropertyClass(**kwargs))


        # self.property_list.append(property)