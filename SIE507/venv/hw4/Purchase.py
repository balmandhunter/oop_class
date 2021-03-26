class Purchase:
    def __init__(self, price=0, taxes=0, **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    '''This instance method prints purchase information'''
    def display(self):
        print('price: ' + str(self.price) + '\n' + 'taxes: ' + str(self.taxes))

    '''This static method prompts the user for information about the purchase and returns it, so that 
    it can be passed as arguments to a new object'''
    @staticmethod
    def prompt_init(self):
        return {'price': input("What is the listing price?: "),
                'taxes': input("What are the property taxes?: ")}