import pandas as pd
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

    def print_plantype(self):
        print(self.plan_type)

    '''Function to create a list of empty squares, based on the user input length and width'''
    def initialize_squares(self, length, width):
        self.length = int(length)
        self.width = int(width)
        # create an empty list for square objects
        self.square_obj_list = [[0] * self.width for i in range(self.length)]

        # loop through the rows and seats, and create a square object for every square foot, and save it in an array
        for row in range(0, self.length):
            for col in range(0, self.width):
                self.square_obj_list[row][col] = Square(row, col)

    '''Function to book a square'''
    def fill_square(self, plant_row, plant_col, plant_name, plant_list):
        # get square object
        square = self.square_obj_list[int(plant_row)-1][int(plant_col) - 1]
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

    '''Create an array that can be saved to a csv from the square object list'''
    def create_plan_from_square_list(self, plant_list):
        self.plant_location_list = [['row', 'column', 'occupied', 'plant', 'count']]
        # iterate through the square object list and append the name of the plant in each location to a list
        for row_idx in range(0, self.length):
            for col_idx in range(0, self.width):
                plant_name = self.square_obj_list[row_idx][col_idx].plant_name
                if self.square_obj_list[row_idx][col_idx].occupied == True:
                    count = plant_list.get_count_per_square(plant_name)
                else:
                    count = 0
                self.plant_location_list.append([row_idx,
                                                 col_idx,
                                                 self.square_obj_list[row_idx][col_idx].occupied,
                                                 plant_name,
                                                 count])
        self.save_plan_to_csv()

    '''Save the current plan to a csv file'''
    def save_plan_to_csv(self):
        with open('data/current_plan.csv', 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(self.plant_location_list)

    '''Load a saved plan'''
    def load_saved_plan_current_year(self, plant_list):
        df = pd.read_csv('data/current_plan.csv', index_col=None)
        self.make_square_obj_list_from_plan(df, plant_list, 'current')
        return self.length, self.width

    '''Create a list of square objects from a saved, current year plan'''
    def make_square_obj_list_from_plan(self, df, plant_list, plan_year):
        # find the number of rows and columns in the bed
        self.length = df.row.max() + 1
        self.width = df.column.max() + 1
        # create an empty list of square objects
        self.initialize_squares(self.length, self.width)
        # create a plant object and add it to the appropriate square
        for idx, plant in df.iterrows():
            # only add plants for squares that are occupied in the loaded plan
            if plant.plant != '(empty)':
                # only add perennials to the plan is loading last year's plan
                if plan_year == 'current' or plant_list.get_perennial_status(plant.plant) == 1:
                    self.fill_square(plant.row + 1,
                                     plant.column + 1,
                                     plant.plant,
                                     plant_list)

    '''Load a saved plan for this year'''
    def load_last_year_plan(self, plant_list):
        df = pd.read_csv('data/last_year_plan.csv', index_col=None)
        self.make_square_obj_list_from_plan(df, plant_list, 'last_year')
        return self.length, self.width

    '''Make planting dates output'''
    def make_planting_dates_file(self, plant_list):
        # convert the plant location list to a numpy array
        np_plant_location_list = np.asarray(self.plant_location_list)
        # convert the np array to a df
        df_plant_locations = pd.DataFrame(np_plant_location_list[1:],
                                          columns = list(np_plant_location_list[0]),
                                          index=None)
        # drop unoccupied spaces
        df_plant_locations = df_plant_locations[df_plant_locations.occupied == 'True']
        # drop row and column columns
        df_plant_locations.drop(columns=['row', 'column', 'occupied'], inplace=True)
        # sum the plants to get total per square
        df_plant_locations = df_plant_locations.astype({'count': 'int32'})
        df_plant_locations = df_plant_locations.groupby(['plant']).sum().reset_index()
        df_plant_locations.rename(columns={'plant': 'name', 'count': 'total_count'}, inplace=True)
        # filter the plant list to the current zone
        df_plant_list_zone = plant_list.df_plant[plant_list.df_plant.zone == int(self.zone)]
        # merge the two dataframes
        self.df_planting = df_plant_locations.merge(df_plant_list_zone, on='name', how='left')
        self.make_planting_df_human_readable()

    '''Convert the planting df to a human friendly format'''
    def make_planting_df_human_readable(self):
        start_indoors_month = []
        transplant_month = []
        direct_seed_month = []
        harvest_month = []
        month_dict = {0: 'Not Recommended',
                      1: 'January',
                      2: 'February',
                      3: 'March',
                      4: 'April',
                      5: 'May',
                      6: 'June',
                      7: 'July',
                      8: 'August',
                      9: 'September',
                      10: 'October',
                      11: 'November',
                      12: 'December'}
        for idx, row in self.df_planting.iterrows():
            start_indoors_month.append(month_dict[row.start_indoors_month])
            transplant_month.append(month_dict[row.transplant_month])
            direct_seed_month.append(month_dict[row.direct_seed_month])
            harvest_month.append(month_dict[row.harvest_month])
        self.df_planting['start_indoors_month'] = start_indoors_month
        self.df_planting['transplant_month'] = transplant_month
        self.df_planting['direct_seed_month'] = direct_seed_month
        self.df_planting['harvest_month'] = harvest_month
        # Drop the columns we don't want to show
        self.df_planting.drop(columns=['zone', 'is_perennial', 'count_per_square'], inplace=True)
        # save the planting df to a csv file
        self.df_planting.to_csv('data/planting_dates.csv', index=False)
