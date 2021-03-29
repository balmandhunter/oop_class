from HouseRental import HouseRental
from HousePurchase import HousePurchase
from ApartmentPurchase import ApartmentPurchase
from ApartmentRental import ApartmentRental

class Agent():
    # this only gets run once, when the file is initially read, so it doesn't reinitialize the
    # list every time you create a new object
    agent_list = []

    def __init__(self, agent_name="", property_list=[], **kwargs):
        super().__init__(**kwargs)
        self.property_list = property_list
        self.agent_name = agent_name
        self.agent_list.append(self)

    '''This class method prints the list of agent objects'''
    @classmethod
    def print_agent_list(cls):
        print(cls.agent_list)

    '''This class method returns the list of agents'''
    @classmethod
    def get_agent_list(cls):
        return cls.agent_list

    '''This instance method returns the name of the agent'''
    def get_name(self):
        return self.agent_name

    '''This instance method lists all of an agent's properties'''
    def list_properties(self, show_all=False):
        for property in self.property_list:
            property.display()

    '''This class method ask users to input a property and transaction type. '''
    @classmethod
    def get_user_input(cls):
        # Ask the user to enter the property type
        property_type = input("Is the property a house or apartment?").lower()
        # check the validity of the property type
        while property_type.lower() not in ['house', 'apartment']:
            print('Invalid Input')
            property_type = input("Is the property a house or apartment?").lower()

        # Ask the user to enter the purchase type
        purchase_type = input("Is the listing for a rental or purchase?").lower()
        # check the validity of the purchase type
        while purchase_type.lower() not in ['rental', 'purchase']:
            print('Invalid Input')
            purchase_type = input("Is the listing for a rental or purchase?").lower()

        return property_type, purchase_type

    '''This instance method gets input from the user about what type of property they would like to create,
    then creates the property and adds it to the agent's property list.'''
    def add_property(self):
        # create a dictionary of all of the property types
        property_type_dict = {('house', 'rental'): HouseRental,
                              ('house', 'purchase'): HousePurchase,
                              ('apartment', 'purchase'): ApartmentPurchase,
                              ('apartment', 'rental'): ApartmentRental}
        # ask the user to input property type and purchase type
        print('Add a property for ' + str(self.agent_name) + '.')
        property_type, purchase_type = Agent.get_user_input()
        # Call the user input as a key to the dictionary to grab the appropriate class
        DeclaredPropertyClass = property_type_dict[(property_type, purchase_type)]
        # Prompt the user to enter information specific to the selected class
        args = DeclaredPropertyClass.prompt_init()
        # Creat an object of the appropriate class using the arguments entered by the user,
        # and append it to the agent's list of properties
        self.property_list.append(DeclaredPropertyClass(**args))
