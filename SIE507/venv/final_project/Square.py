class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.occupied = False
        self.plant = '(empty)'
        self.plant_object = None

    def occupy_square(self, plant, plant_object):
        self.occupied = True
        self.plant = plant
        self.plant_object = plant_object

    def empty_square(self):
        self.occupied = False
        self.plant = None

    def return_plant(self):
        return self.plant
