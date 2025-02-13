class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.occupied = False
        self.plant_name = '(empty)'
        self.plant_object = None

    '''Add a plant to the square'''
    def occupy_square(self, plant, plant_object):
        self.occupied = True
        self.plant = plant
        self.plant_object = plant_object
        self.plant_name = plant_object.plant_name

    '''Remove a plant from the square'''
    def empty_square(self):
        self.occupied = False
        self.plant = None

    '''Return the name of the plant'''
    def return_plant_name(self):
        return self.plant_name
