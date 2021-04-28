import numpy as np
# from SquareFoot import Square

class RaisedBed:
    def __init__(self, zone):
        self.zone = zone
        self.print_zone()

    def print_zone(self):
        print('Raised Bed Zone: ')
        print(self.zone)