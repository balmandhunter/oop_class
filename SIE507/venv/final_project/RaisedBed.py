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

        # create an empty list for square objects
        self.square_obj_list = [[0] * self.width for i in range(self.length)]

        # loop through the rows and seats, and create a seat object for every seat, and save it in an array
        for row in range(0, self.length):
            for col in range(0, self.width):
                self.square_obj_list[row][col] = Square(row, col)


    '''Function to book a seat'''
    def fill_square(self, plant_row, plant_col, plant_name):
        # get square object
        square = self.square_obj_list[int(plant_row)-1][int(plant_col) - 1]
        square.occupy_square(plant_name)

    '''Create an array that can be saves to a csv from the square object list'''
    def create_plan_from_square_list(self):
        plant_location_list = [['row', 'column', 'occupied', 'plant']]
        print(self.square_obj_list)
        # iterate through the square object list and append the name of the plant in each location to a list
        for row_idx in range(0, self.length):
            for col_idx in range(0, self.width):
                plant_location_list.append([row_idx, col_idx, self.square_obj_list[row_idx][col_idx].occupied, self.square_obj_list[row_idx][col_idx].plant])
