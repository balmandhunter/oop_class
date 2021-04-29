from View import View, ZonePlanSelectionView, SizeView, BedPlanView
from PlantList import PlantList
from RaisedBed import RaisedBed
from abc import ABC, abstractmethod
from tkinter import messagebox

import tkinter as tk

class Controller:

    def __init__(self, plant_list_filename, **kwargs):
        super().__init__(**kwargs)
        self.root = tk.Tk()
        # self.make_selection_view('view')    uncomment when finished debugging
        # self.plant_list_filename = plant_list_filename
        ##### debugging code ######
        self.zone = 3
        self.set_zone_and_update_view()
        self.raisedbed.plan_type = 'Start a New Plan'

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
  #      self.zone = self.view.selected.get()   uncomment when finished debugging
        # Initialize a PlantList object with the zone
        self.plantlist = PlantList('data/all_plants.csv', self.zone)
        # Initialize a raised bed with the zone
        self.raisedbed = RaisedBed(self.zone)
        # Update the view to the plan selection
        #self.make_selection_view('plan_type') uncomment when finished debugging

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
            # self.root.mainloop()
        else:
            print('not coded yet')

    '''Ask the user for the size of their garden bed, create the raised bed square objects, 
    and return the empty bed diagram to the user.'''
    def get_bed_size(self):
        self.length = 5
        self.width = 2
        #     self.width =
        # # get the length and width from the view
        # if self.size_view.length.get() == "" or self.size_view.length.get() == "":
        #     messagebox.showinfo("Application Error", "Empty Textbox!")
        # ######## add error message for non integer ############
        # else:
        #     self.length = self.size_view.length.get()
        #     self.width = self.size_view.width.get()
        self.raisedbed.initialize_squares(self.length, self.width)
        self.get_plan()

    '''Return the current garden plan to the user'''
    def get_plan(self):
        self.bedplanview = BedPlanView(self.root, self, self.plantlist.return_plants())
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
        self.check_plant_location_entry(plant_row, plant_col, plant_name)

        print(plant_row, plant_col, plant_name)

    def check_plant_location_entry(self, plant_row, plant_col, plant_name):

        # make sure the length and width entries are integers
        while plant_row.isdigit() is False or plant_col.isdigit() is False:
            # messagebox.showinfo("Application Error", "Please enter an integer!")
            retry = messagebox.askretrycancel(title=None, message="Please enter an integer!")
            self.get_plan()
        # make sure the entry is within the size range of the raised bed
        while int(plant_row) not in range(1, int(self.length) + 1):
            retry = messagebox.askretrycancel(title=None, message="Row out of range!")
            self.get_plan()
        while int(plant_col) not in range(1, int(self.width) + 1):
            retry = messagebox.askretrycancel(title=None, message="Column out of range!")
            self.get_plan()
        # Make sure the user selected a plant
        while plant_name == "Select a Plant":
            retry = messagebox.askretrycancel(title=None, message="No plant selected!")
            self.get_plan()
