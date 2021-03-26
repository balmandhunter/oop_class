class Property():
    def __init__(self, square_feet=0, num_bedrooms=0, num_bathrooms=0, **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bathrooms = num_bathrooms

    '''This instance method displays information about the property'''
    def display(self):
        print('Square Feet: ' + str(self.square_feet) + '\n' +
              'Bedrooms: ' + str(self.num_bedrooms) + '\n'
              'Bathrooms: ' + str(self.num_bathrooms))

    '''This static method asks the user for input and returns the answers in a dictionary. This is implemented
    as a static method because it doesn't need access to the class or to self. Good article with notes on class
    vs static vs instance methods: https://realpython.com/instance-class-and-static-methods-demystified/'''
    @staticmethod
    def prompt_init():
        # return {'square_feet': input("Please input the number of square feet:"),
        #         'num_bedrooms': input("Please input the number of bedrooms:"),
        #         'num_bathrooms': input("Please input the number of bathrooms:")}
        return {'square_feet': 2000,
                'num_bedrooms': 3,
                'num_bathrooms': 2}
