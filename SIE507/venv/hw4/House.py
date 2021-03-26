from Property import Property

class House(Property):
    def __init__(self, num_stories=0, garage=False, fenced_yard=False, **kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    '''This instance method prints information about the house'''
    def display(self):
        # print property information from the parent class
        Property.display(self)
        # print house information
        print('Number of Stories: ' + str(self.num_stories) + '\n' +
              'Garage: ' + str(self.garage) + '\n'
              'Fenced Yard: ' + str(self.fenced_yard))

    '''This static method prompts the user for information about the house and returns it, so that 
    it can be passed as arguments to a new house object'''
    @staticmethod
    def prompt_init():
        # call the static method of the property class to prompt the user for arguments of the property class
        args = Property.prompt_init()
        # prompt the user to enter the arguments for a house
        args.update({'num_stories': input("How many stories does the house have?:"),
                     'garage': input("Does the house have a garage (True or False)?:"),
                     'fenced_yard': input("Does the house have a fenced-in yard (True or False)?:")})
        # return the property and house arguments
        return args