import numpy as np
# from SquareFoot import Square

class RaisedBed:
    def __init__(self, zone):
        self.zone = zone
        self.plan_type = None

    def print_zone(self):
        print('Raised Bed Zone: ')
        print(self.zone)

    def print_plantype(self):
        print(self.plan_type)

    def initialize_squares(self, length, width):
        self.length = length
        self.width = width
        print(self.length)