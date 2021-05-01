import numpy as np
import csv
from Square import Square
from Plant import Plant, Annual, Perennial
from PlantList import PlantList

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

    '''Function to book a square'''
    def fill_square(self, plant_row, plant_col, plant_name, plant_list):
        # get square object
        square = self.square_obj_list[int(plant_row)-1][int(plant_col) - 1]
        # self.plant_list = PlantList()
        # create a plant object for the correct plant and zone
        if plant_list.get_perennial_status(plant_name) == 1:
            plant = Perennial(True, plant_name, self.zone)
        elif plant_list.get_perennial_status(plant_name) == 0:
            plant = Annual(plant_name, self.zone)
        else:
            print('Need to write exception')
            #######add exception ############
        # occupy the square
        square.occupy_square(plant_name, plant)

    '''Create an array that can be saves to a csv from the square object list'''
    def create_plan_from_square_list(self):
        self.plant_location_list = [['row', 'column', 'occupied', 'plant']]
        # iterate through the square object list and append the name of the plant in each location to a list
        for row_idx in range(0, self.length):
            for col_idx in range(0, self.width):
                self.plant_location_list.append([row_idx,
                                                 col_idx,
                                                 self.square_obj_list[row_idx][col_idx].occupied,
                                                 self.square_obj_list[row_idx][col_idx].plant])
        self.save_plan_to_csv()

    def save_plan_to_csv(self):
        # file = open('data/raised_bed.csv', 'w')       # Open/create a text file in write only mode
        # for line in self.plant_location_list:         # Iterate through each row in array
        #     for char in line:                         # Iterate through each character in the loop variable line
        #         file.write(str(char))                 # Write the character to the text file
        #         file.write(',')
        #     file.write('\n')                          # Go to the next line in the text file after writing a line
        # file.close()

        with open('data/raised_bed.csv', 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(self.plant_location_list)