from View import View, ZonePlanSelectionView, SizeView, BedPlanView
from PlantList import PlantList
from RaisedBed import RaisedBed
from Exceptions import GardenExceptions
from tkinter import messagebox

import tkinter as tk

class Controller:

    def __init__(self, plant_list_filename, **kwargs):
        self.root = tk.Tk()
        self.gardenexceptions = GardenExceptions()
        self.gardenexceptions.call_back(self)
        # self.make_selection_view('view')    # comment to debug
        # self.plant_list_filename = plant_list_filename
        self.plant_list = PlantList('data/all_plants.csv')

        ##### debugging code ######
        self.zone = 3
        self.view = ZonePlanSelectionView(self.root, self, 'view')

        self.set_zone_and_update_view()
        # self.raisedbed.plan_type = 'Load Saved Plan (current year)' uncomment to debug

        self.get_bed_size()


    '''Create the initial GUI View, where gardeners select a Zone.'''
    def make_selection_view(self, dropdown_topic):
        self.view = ZonePlanSelectionView(self.root, self, dropdown_topic)
        # Call the view object to make the initial view
        self.view.make_initial_view()

        # set the command for the button
        if dropdown_topic == 'view':
            button_command = self.set_zone_and_update_view
        elif dropdown_topic == 'plan_type':
            button_command = self.get_and_send_plan_selection

        # Bind the button to the appropriate function
        self.view.buttons['Submit'].configure(command=button_command)
        self.root.mainloop()

    '''Get the selected zone from the dropdown, send it to the plant list and raised bed, and update the view.'''
    def set_zone_and_update_view(self):
        # Get the user-selected zone from the dropdown
        # self.zone = self.view.selected.get()   #comment to debug
        # Initialize a raised bed with the zone
        self.raisedbed = RaisedBed(self.zone)
        # Update the view to the plan selection
        self.make_selection_view('plan_type')  #comment to debug

    '''Get button selection and send it to Raised Bed'''
    def get_and_send_plan_selection(self):
        # Get the user-selected plan type
        plan_type = self.view.selected.get()
        self.raisedbed.plan_type = plan_type
        if plan_type == 'Start a New Plan':
            print('Starting a New Plan')
            self.size_view = SizeView(self.root, self)
            self.size_view.make_size_view()
            # Bind the button to the appropriate function
            self.size_view.buttons['Submit'].configure(command=self.get_bed_size)
        elif plan_type == 'Start a Follow-on Plan from Last Year\'s Plan':
            self.length, self.width = self.raisedbed.load_last_year_plan(self.plant_list)
            self.size_view = SizeView(self.root, self)
            self.get_plan()
        elif plan_type == 'Load Saved Plan (current year)':
            self.length, self.width = self.raisedbed.load_last_year_plan(self.plant_list)
            self.size_view = SizeView(self.root, self)
            self.get_plan()

    '''Ask the user for the size of their garden bed, create the raised bed square objects, 
    and return the empty bed diagram to the user.'''
    def get_bed_size(self):
        # get the length and width from the view
        if self.size_view.length.get() == "" or self.size_view.length.get() == "":
            messagebox.showinfo("Application Error", "Empty Textbox!")
        ######## add error message for non integer ############
        else:
            self.length = self.size_view.length.get()
            self.width = self.size_view.width.get()
        self.raisedbed.initialize_squares(self.length, self.width)
        self.raisedbed.create_plan_from_square_list(self.plant_list)
        self.get_plan()

    '''Return the current garden plan to the user'''
    def get_plan(self):
        self.bedplanview = BedPlanView(self.root, self, self.plant_list.return_plants())
        # show the bed layout to the user
        self.bedplanview.show_bed(self.raisedbed.square_obj_list, self.raisedbed.length, self.raisedbed.width)
        self.bedplanview.buttons['Add Plant'].configure(command=self.get_plant_location)
        self.root.mainloop()

    '''Get the user input for location and plant to add.'''
    def get_plant_location(self):
        plant_row = self.bedplanview.row.get()
        plant_col = self.bedplanview.column.get()
        plant_name = self.bedplanview.selected.get()
        #check that the entries are appropriate
        self.gardenexceptions.check_plant_location_entry(plant_row, plant_col, plant_name)
        self.add_plant_to_garden(plant_row, plant_col, plant_name)

    '''Add user-input plant to the garden'''
    def add_plant_to_garden(self, plant_row, plant_col, plant_name):
        # call the function in the RaisedBed to fill the square
        self.raisedbed.fill_square(plant_row, plant_col, plant_name, self.plant_list)
        # add the plant to the raised bed
        self.raisedbed.create_plan_from_square_list(self.plant_list)
        self.get_plan()

