from View import View, ZonePlanSelectionView
from PlantList import PlantList
from RaisedBed import RaisedBed
from abc import ABC, abstractmethod
import tkinter as tk

class Controller:

    def __init__(self, plant_list_filename, **kwargs):
        super().__init__(**kwargs)
        self.root = tk.Tk()
        self.make_zone_selection_view()
        # self.plant_list_filename = plant_list_filename

    '''Create the initial GUI View, where gardeners select a Zone.'''
    def make_zone_selection_view(self):
        self.zoneview = ZonePlanSelectionView(self.root, self, 'view')
        # Call the zoneview object to make the initial zoneview
        self.zoneview.make_initial_view()
        # Bind the button to the set_zone_and_update_view function
        self.zoneview.buttons['Submit'].configure(command=self.set_zone_and_update_view)
        self.root.mainloop()

    '''Get the selected zone from the dropdown, send it to the raised bed and plant list,
    and update the view.'''
    def set_zone_and_update_view(self):
        # Get the user-selected from the dropdown
        self.zone = self.zoneview.selected.get()
        # Initialize a PlantList object with the zone
        self.plantlist = PlantList('data/all_plants.csv', self.zone)
        # Initialize a raised bed with the zone
        self.raisedbed = RaisedBed(self.zone)
