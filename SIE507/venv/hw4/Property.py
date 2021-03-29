class Property():
    def __init__(self, square_feet=0, num_bedrooms=0, num_bathrooms=0, address='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms
        self.address = address

    '''This instance method returns the sq. footage of the property'''
    def get_square_feet(self):
        return self.square_feet

    '''This instance method returns the address of the property'''
    def get_address(self):
        return self.address

    '''This instance method returns the number of bathrooms'''
    def get_num_bathrooms(self):
        return self.num_bathrooms

    '''This instance method returns the number of bedrooms'''
    def get_num_bedrooms(self):
        return self.num_bedrooms

    '''This instance method displays information about the property'''
    def display(self):
        print('------------------------' + '\n' +
              'Address: ' + str(self.address) + '\n'
              'Square Feet: ' + str(self.square_feet) + '\n' +
              'Bedrooms: ' + str(self.num_bedrooms) + '\n' +
              'Bathrooms: ' + str(self.num_bathrooms))


    '''This class method asks the user for information about the property, validates it, and returns
    it in a dictionary'''
    @classmethod
    def prompt_init(cls):
        square_feet = input("Please input the number of square feet:")
        while square_feet.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            square_feet = input("Please input the number of square feet:")

        address = input("Please input the property address:")
        while len(address) <= 0:
            print('Invalid Input')
            address = input("Please input the property address:")

        num_bedrooms = input("Please input the number of bedrooms:")
        while num_bedrooms.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            num_bedrooms = input("Please input the number of bedrooms:")

        num_bathrooms = input("Please input the number of bathrooms:")
        while num_bathrooms.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            num_bathrooms = input("Please input the number of bathrooms:")

        info_dict = {'square_feet': square_feet,
                     'address': address,
                     'num_bedrooms': num_bedrooms,
                     'num_bathrooms': num_bathrooms}

        return info_dict

