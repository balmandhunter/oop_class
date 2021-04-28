import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
from tkinter import *

# from tkinter import filedialog
import pandas as pd

class View:
    def __init__(self, root, controller, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.controller = controller

    def initialize_GUI(self):
        # setup and name the window
        self.root.title("Maine Garden Planner")
        self.root.geometry("300x300")
        # Create a frame widget
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

class ZonePlanSelectionView(View):
    def __init__(self, root, controller, dropdown_topic,  **kwargs):
        super().__init__(root, controller, **kwargs)
        self.root = root
        # initialize the view
        self.buttons = {}
        self.controller = controller
        self.dropdown_topic = dropdown_topic
        super().initialize_GUI()

    def make_initial_view(self):
        if self.dropdown_topic == 'view':
            # create the zone dropdown
            options = ['3','4','5','6']
            title = 'Select Your Gardening Zone'
        elif self.dropdown_topic == 'plan_type':
            options = ['Load Last Year\'s Plan', 'Start a New Plan']
            title = 'Select a Plan Type'
        self.c_create_dropdown(title, options, 1, 0)

        # display the profession dropdown
        self.zone_dropdown.grid(row=0, column=0, padx=15, pady=15)

        # make an exit button to end the program
        exit_button = ttk.Button(self.mainframe, text="EXIT", command=self.root.destroy)
        exit_button.grid(row=8, column=0, padx=5)

    def c_create_dropdown(self, title, values, buttonrow, buttoncol):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        self.selected = tk.StringVar()
        # set default in dropdown
        self.selected.set(title)

        # create drop down menu
        self.zone_dropdown = tk.OptionMenu(self.mainframe, self.selected, *values)

        # make the button
        self.create_button(self.mainframe, 'Submit', buttonrow, buttoncol)

    def create_button(self, frame, name, row, column):
        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
        self.buttons[name] = ttk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)
