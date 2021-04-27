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
        self.root.geometry("825x500")
        # Create a frame widget
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))



class ZoneView(View):
    def __init__(self, root, controller, **kwargs):
        super().__init__(root, controller, **kwargs)
        self.root = root
        # initialize the view
        self.buttons = {}
        self.controller = controller
        super().initialize_GUI()

    def make_initial_view(self):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        # selected = tk.StringVar()

        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

        # create drop down menu
        # create the zone dropdown
        zone_options = ['3','4','5','6']
        zone_dropdown = self.c_create_dropdown("Select Your Gardening Zone", zone_options, 1, 0)

        # display the profession dropdown
        zone_dropdown.grid(row=0, column=0, padx=15, pady=15)

        # make an exit button to end the program
        exit_button = ttk.Button(self.mainframe, text="EXIT", command=self.root.destroy)
        exit_button.grid(row=8, column=0, padx=5)

        self.root.mainloop()


    def c_create_dropdown(self, title, values, buttonrow, buttoncol):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        selected = tk.StringVar()
        # set default in dropdown
        selected.set(title)

        # create drop down menu
        options = tk.OptionMenu(self.mainframe, selected, *values)
        # make the button
        self.create_button(self.mainframe, 'Submit', buttonrow, buttoncol)

        return options

    def create_button(self, frame, name, row, column):
        self.buttons[name] = tk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)

    def on_select(val):
        pass
        # global df2
        # global current_index
        #
        # val = selected.get()
        # if val == "all":
        #     df2 = df
        #     next_button.grid_forget()
        #     showdata()
        # else:
        #     df2 = df[df["Title"] == val]
        #     # find index
        #     current_index = 0
        #     for ind in df.index:
        #         if df["Title"][ind] == val:
        #             current_index = ind
        #
        #     showdata()
        #     # put next button on the canvas
        #     next_button.grid(row=2, column=0, sticky=W)