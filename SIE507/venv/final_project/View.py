import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
from tkinter import *

# from tkinter import filedialog
import pandas as pd

class View:
    def __init__(self):
        self.mainframe = None
        # initialize the view
        self.__initialize_GUI()

    def c_start_app(self):
        form = None
        v_initialize_GUI()
        form.mainloop()

    def __initialize_GUI(self):
        # setup and name the window
        self.root = tk.Tk()
        self.root.title("Maine Garden Planner")
        self.root.geometry("825x500")
        # Create a frame widget
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # call the function that makes the initial view with dropdown
        self.make_initial_view()


    def make_initial_view(self):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        # selected = tk.StringVar()

        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

        # create drop down menu
        # create the zone dropdown
        options_list = ['3','4','5','6']
        options1 = self.c_create_dropdown("Select Your Gardening Zone", options_list)
        # display the profession dropdown
        options1.grid(row=0, column=0, padx=15, pady=15)

        # Make a Dropdown for the plan type
        options_list = ['Load Last Year\'s Plan', 'Start a New Plan']
        options2 = self.c_create_dropdown("Choose a Plan", options_list)
        # display the  dropdown
        options2.grid(row=2, column=0, padx=15, pady=15)

        # frame for table and button "Submit"
        frame_data = tk.Frame(self.mainframe)
        frame_data.grid(row=3, column=0, padx=5, pady=15)

        # button "Submit" - inside "frame_data"
        ##### add command to this button to make it do something!
        next_button = ttk.Button(frame_data, text="Submit", command=None)
        next_button.grid(row=3, column=0, padx=5)

        # make an exit button to end the program
        exit_button = ttk.Button(self.mainframe, text="EXIT", command=self.root.destroy)
        exit_button.grid(row=8, column=0, padx=5)

        self.root.mainloop()

    def c_create_dropdown(self, title, values):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        selected = tk.StringVar()
        # set default in dropdown
        selected.set(title)

        # create drop down menu
        options = tk.OptionMenu(self.mainframe, selected, *values)

        return options

    def submit_initial_entry():
        pass

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