from Property import Property

class House(Property):
    def __init__(self, num_stories=0, garage=False, fenced_yard=False, **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    '''This instance method prints information about the house'''
    def display(self):
        print('---------------')
        # print property address from the property class
        print('Address: ' + Property.get_address(self))
        print('Property Type: House')

    '''This class method prompts the user for information about the house and returns it, so that
    it can be passed as arguments to a new house object'''
    @classmethod
    def prompt_init(cls):
        # call the prompt_init() method of the property class to prompt the user for arguments of the property class
        house_info = Property.prompt_init()

        # prompt the user for inputs specific to houses and verify them
        num_stories = input('How many stories does the house have?:')
        while num_stories.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            num_stories = input('How many stories does the house have?:')

        garage = input('Does the house have a garage (yes or no)?:')
        while garage.lower() not in ['yes', 'no']:
            print('Invalid Input.')
            garage = input('Does the house have a garage (yes or no)?:')

        fenced_yard = input('Does the house have a fenced-in yard (yes or no)?:')
        while fenced_yard.lower() not in ['yes', 'no']:
            print('Invalid Input.')
            fenced_yard = input('Does the house have a fenced-in yard (yes or no)?:')

        house_info.update({'num_stories': num_stories,
                     'garage': num_stories,
                     'fenced_yard': fenced_yard})

        # return the property and house arguments
        return house_info