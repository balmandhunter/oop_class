class Purchase:
    def __init__(self, price=0, taxes=0, **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    '''This instance method prints the price of the property'''
    def display(self):
        print('Transaction Type: Purchase')
        print('Price: ' + str(self.price))

    '''This static method prompts the user for information about the purchase and returns it, so that 
    it can be passed as arguments to a new object'''
    @staticmethod
    def prompt_init():
        price = input("What is the listing price?:")
        while price.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            price = input("What is the listing price?:")

        taxes =  input("What are the property taxes?:")
        while taxes.isdigit() is False:
            print('Invalid Input. Please enter an integer.')
            taxes =  input("What are the property taxes?:")

        info_dict =  {'price': price,
                      'taxes': taxes}

        return info_dict