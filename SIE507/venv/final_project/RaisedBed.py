import numpy as np
from Square import Square

class RaisedBed:
    def __init__(self, zone):
        self.zone = zone
        self.plan_type = None

    def print_zone(self):
        print('Raised Bed Zone: ')
        print(self.zone)

    def print_plantype(self):
        print(self.plan_type)

    '''Function to create a list of empty squares, based on the user input length and width'''
    def initialize_squares(self, length, width):
        self.length = int(length)
        self.width = int(width)
        print(self.length)

        # create an empty list for seat objects
        self.square_obj_list = [[0] * self.width for i in range(self.width)]

        # loop through the rows and seats, and create a seat object for every seat, and save it in an array
        for row in range(0, self.length):
            for col in range(0, self.width):
                self.square_obj_list[row][col] = Square(row, col)
        print(self.square_obj_list)
