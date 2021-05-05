from tkinter import messagebox

class GardenExceptions():
    def __init__(self):
        pass

    '''Make a callback to the controller so the class can access it'''
    def call_back(self, controller):
        self.controller = controller

    '''Check user entry for adding a new plant'''
    def check_plant_location_entry(self, plant_row, plant_col, plant_name):
        # make sure the entries are integers
        self.check_row_col_entry(plant_row, plant_col)
        # make sure the entry is within the size range of the raised bed
        while int(plant_row) not in range(1, int(self.controller.length) + 1):
            retry = messagebox.askretrycancel(title=None, message="Row out of range!")
            self.controller.get_plan()
        while int(plant_col) not in range(1, int(self.controller.width) + 1):
            retry = messagebox.askretrycancel(title=None, message="Column out of range!")
            self.controller.get_plan()
        # Make sure the user selected a plant
        while plant_name == "Select a Plant":
            retry = messagebox.askretrycancel(title=None, message="No plant selected!")
            self.controller.get_plan()

    '''Check user entry for adding a number of rows and columns'''
    def check_row_col_entry(self, plant_row, plant_col):
        # make sure the length and width entries are integers
        while plant_row.isdigit() is False or plant_col.isdigit() is False:
            retry = messagebox.askretrycancel(title=None, message="Please enter an integer!")
            self.controller.get_plan()