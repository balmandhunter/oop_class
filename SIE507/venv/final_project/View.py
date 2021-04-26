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
        self.root.title("Garden Planner")
        self.root.geometry("825x500")
        # Create a frame widget
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # call the function that makes the initial view with dropdown
        self.make_initial_view()


    def make_initial_view(self):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        selected = tk.StringVar()

        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

        # create drop down menu
        # we have a function we execute on button click -- on_select from drop down menu
        dropdown_menu = ttk.Combobox(self.mainframe, textvariable=selected)
        dropdown_menu.set("New or Saved Plan")
        # add a virtual event to call the "on_select" function when an option is selected
        dropdown_menu.bind("<<ComboboxSelected>>", self.on_select)

        # add options to dropdown
        dropdown_menu["values"] =["Load Last Year's Plan", "Start a New Plan"]
        dropdown_menu.grid(row=0, column=0, padx=5, pady=15)

        self.root.mainloop()


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