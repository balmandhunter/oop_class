from Property import Property

class Apartment(Property):
    def __init__(self, balcony=False, laundry=False, **kwargs):
        super().__init__(**kwargs)
        self.laundry = laundry
        self.balcony = balcony

    '''This instance method prints information about the apartment'''
    def display(self):
        # print property information from the parent class
        Property.display()
        # print apartment information
        print('The apartment has a balcony: ' + str(self.balcony) + '\n' +
              'The apartment has laundry facilities: ' + str(self.laundry))

    @staticmethod
    def prompt_init():
        # call the static method of the property class to prompt the user for arguments of the property class
        args = Property.prompt_init()
        # prompt the user to enter the arguments for an apartment
        args.update({'balcony': input('Does the apartment have a balcony?: '),
                     'laundry': input('Does the apartment have a washer and dryer?: ')})
        # return the property and apartment arguments
        return args