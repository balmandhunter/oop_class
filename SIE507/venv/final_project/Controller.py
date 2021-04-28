from View import View, ZonePlanSelectionView
from PlantList import PlantList
from RaisedBed import RaisedBed
from abc import ABC, abstractmethod
from tkinter import messagebox

import tkinter as tk

class Controller:

    def __init__(self, plant_list_filename, **kwargs):
        super().__init__(**kwargs)
        self.root = tk.Tk()
        self.make_selection_view('view')
        # self.plant_list_filename = plant_list_filename

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
        zone = self.view.selected.get()
        # Initialize a PlantList object with the zone
        self.plantlist = PlantList('data/all_plants.csv', zone)
        # Initialize a raised bed with the zone
        self.raisedbed = RaisedBed(zone)
        # Update the view to the plan selection
        self.make_selection_view('plan_type')

    '''Get button selection and send it to Raised Bed'''
    def get_and_send_plan_selection(self):
        # Get the user-selected plan type
        plan_type = self.view.selected.get()
        self.raisedbed.plan_type = plan_type
        if plan_type == 'Start a New Plan':
            print('Starting a New Plan')
            self.view.make_size_view()
            # Bind the button to the appropriate function
            self.view.buttons['Submit'].configure(command=self.get_bed_size)
            # self.root.mainloop()
        else:
            print('not coded yet')

    def get_bed_size(self):
        if self.view.length.get() == "" or self.view.length.get() == "":
            messagebox.showinfo("Application Error", "Empty Textbox!")
        ### add error message for non integer
        else:
            length = self.view.length.get()
            width = self.view.width.get()
        self.raisedbed.initialize_squares(length, width)