from View import View, ZonePlanSelectionView, SizeView, BedPlanView
from PlantList import PlantList
from RaisedBed import RaisedBed
from Exceptions import GardenExceptions
from tkinter import messagebox
import tkinter as tk

class Controller:
    def __init__(self):
        # initialize the plant list object
        self.plant_list = PlantList('data/all_plants.csv')
        # initialize and make a call back to the exceptions class
        self.gardenexceptions = GardenExceptions()
        self.gardenexceptions.call_back(self)
        # initialize the view
        self.view = View()
        self.view.call_back(self)
        self.start_app()

    '''Method to start the app with the zone selection view'''
    def start_app(self):
        self.make_selection_view('view')
        self.view.root.mainloop()

    '''Create the initial GUI View, where gardeners select a Zone.'''
    def make_selection_view(self, dropdown_topic):
        self.zoneplanview = ZonePlanSelectionView(dropdown_topic, self.view)
        # Call the view object to make the initial view
        self.zoneplanview.make_initial_view()

    '''Get the selected zone from the dropdown, send it to the plant list and raised bed, and update the view.'''
    def set_zone_and_update_view(self):
        # Get the user-selected zone from the dropdown
        self.zone = self.zoneplanview.selected.get()
        # Initialize a raised bed with the zone
        self.raisedbed = RaisedBed(self.zone)
        # Update the view to the plan selection
        self.make_selection_view('plan_type')

    '''Get button selection and send it to Raised Bed'''
    def get_and_send_plan_selection(self):
        # self.view.root.destroy()
        # Get the user-selected plan type
        self.raisedbed.plan_type = self.zoneplanview.selected.get()
        # create and show the appropriate plan
        if self.raisedbed.plan_type == 'Start a New Plan':
            self.size_view = SizeView(self.view)
            self.size_view.make_size_view()
        elif self.raisedbed.plan_type == 'Start a Follow-on Plan from Last Year\'s Plan':
            self.length, self.width = self.raisedbed.load_last_year_plan(self.plant_list)
            self.create_plan_from_file()
        elif self.raisedbed.plan_type == 'Load Saved Plan (current year)':
            self.length, self.width = self.raisedbed.load_saved_plan_current_year(self.plant_list)
            self.create_plan_from_file()

    '''Method to show create a plan from a file'''
    def create_plan_from_file(self):
        self.size_view = SizeView(self.view)
        self.raisedbed.create_plan_from_square_list(self.plant_list)
        self.raisedbed.make_planting_dates_file(self.plant_list)
        self.get_plan()

    '''Ask the user for the size of their garden bed, create the raised bed square objects, 
    and return the empty bed diagram to the user.'''
    def get_bed_size(self):
        # get the length and width from the view
        self.gardenexceptions.check_row_col_entry(self.size_view.length.get(),
                                                  self.size_view.width.get())
        # get the length and width from the view
        self.length = self.size_view.length.get()
        self.width = self.size_view.width.get()
        self.raisedbed.initialize_squares(self.length, self.width)
        self.raisedbed.create_plan_from_square_list(self.plant_list)
        self.get_plan(plan_type='new')

    '''Return the current garden plan to the user'''
    def get_plan(self, plan_type=None):
        self.bedplanview = BedPlanView(self.plant_list.return_plants(), self.view)
        # show the bed layout to the user
        self.bedplanview.show_bed(self.raisedbed.square_obj_list,
                                  self.raisedbed.length,
                                  self.raisedbed.width,
                                  self.plant_list.df_plant)
        if plan_type != 'new':
            self.bedplanview.show_planting_dates(self.raisedbed.df_planting)

    '''Get the user input for location and plant to add.'''
    def get_plant_location(self):
        plant_row = self.bedplanview.row.get()
        plant_col = self.bedplanview.column.get()
        plant_name_and_count = self.bedplanview.selected.get()
        # remove the plant count from the name
        plant_name = plant_name_and_count.split(' (')[0]

        #check that the entries are appropriate
        self.gardenexceptions.check_plant_location_entry(plant_row, plant_col, plant_name)
        self.add_plant_to_garden(plant_row, plant_col, plant_name)
        self.get_plan()

    '''Add user-input plant to the garden'''
    def add_plant_to_garden(self, plant_row, plant_col, plant_name):
        # call the function in the RaisedBed to fill the square
        self.raisedbed.fill_square(plant_row, plant_col, plant_name, self.plant_list)
        # add the plant to the raised bed
        self.raisedbed.create_plan_from_square_list(self.plant_list)
        self.raisedbed.make_planting_dates_file(self.plant_list)
