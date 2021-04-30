class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.occupied = False
        self.plant = '(empty)'

    def occupy_square(self, plant):
        self.occupied = True
        self.plant = plant

    def empty_square(self):
        self.occupied = False
        self.plant = None

    def return_plant(self):
        return self.plant
