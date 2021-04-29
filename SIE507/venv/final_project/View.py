import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd


class View:
    def __init__(self, root, controller, **kwargs):
        super().__init__(**kwargs)
        self.root = root
        self.controller = controller

    def initialize_GUI(self):
        # setup and name the window
        self.root.title("Maine Garden Planner")
        self.root.geometry("500x300")
        # Create a frame widget
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    '''Destroy all of the widgets before making a new window'''
    def _clear_canvas(self):
        for widget in self.root.winfo_children():
            pass
            # widget.destroy()

    '''Create a button and add it to the button dictionary'''
    def create_button(self, frame, name, row, column):
        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
        self.buttons[name] = ttk.Button(frame)
        self.buttons[name]["text"] = name
        self.buttons[name].grid(row=row, column=column)

class ZonePlanSelectionView(View):
    def __init__(self, root, controller, dropdown_topic,  **kwargs):
        super().__init__(root, controller, **kwargs)
        self.root = root
        self.buttons = {}
        self.controller = controller
        self.dropdown_topic = dropdown_topic
        super().initialize_GUI()

    '''Create the initial view in the GUI'''
    def make_initial_view(self):
        if self.dropdown_topic == 'view':
            # create the zone dropdown
            options = ['3','4','5','6']
            title = 'Select Your Gardening Zone'
        elif self.dropdown_topic == 'plan_type':
            ###### add this function to clear the canvas -- it's breaking now
            self._clear_canvas()
            options = ['Load Last Year\'s Plan', 'Start a New Plan']
            title = 'Select a Plan Type'
        self.create_dropdown(title, options, 1, 0)

        # display the profession dropdown
        self.zone_dropdown.grid(row=0, column=0, padx=15, pady=15)

        # make an exit button to end the program
        exit_button = ttk.Button(self.mainframe, text="EXIT", command=self.root.destroy)
        exit_button.grid(row=8, column=0, padx=5)

    '''Create the dropdown menu'''
    def create_dropdown(self, title, values, buttonrow, buttoncol):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        self.selected = tk.StringVar()
        # set default in dropdown
        self.selected.set(title)
        # create drop down menu
        self.zone_dropdown = tk.OptionMenu(self.mainframe, self.selected, *values)
        # make the button
        self.create_button(self.mainframe, 'Submit', buttonrow, buttoncol)

class SizeView(View):
    def __init__(self, root, controller,  **kwargs):
        super().__init__(root, controller, **kwargs)
        self.root = root
        self.buttons = {}
        self.controller = controller
        super().initialize_GUI()

    '''Create the view where users input the size of their garden bed'''
    def make_size_view(self):
        ####### self._clear_canvas()
        self.length = tk.StringVar()
        self.width = tk.StringVar()

        # Label the entry boxes
        self.length_label = tk.Label(self.mainframe, text="Garden Bed Length (ft): ").grid(row=0, column=0, padx=15, pady=15)
        self.width_label = tk.Label(self.mainframe, text="Garden Bed Width (ft): ").grid(row=1, column=0, padx=15, pady=15)

        # Create the entry boxes
        self.length_entry = tk.Entry(self.mainframe, textvariable=self.length).grid(row=0, column=1, padx=15, pady=15)
        self.width_entry = tk.Entry(self.mainframe, textvariable=self.width).grid(row=1, column=1, padx=15, pady=15)

        # Create the submit button
        self.create_button(self.mainframe, 'Submit', 3, 3)


class BedPlanView(View):
    def __init__(self, root, controller, plant_list, **kwargs):
        super().__init__(root, controller, **kwargs)
        self.root = root
        self.buttons = {}
        self.controller = controller
        self.plant_list = plant_list
        super().initialize_GUI()

    '''Return the garden plan'''
    def show_bed(self, square_obj_list, length, width):
        columns = width
        self.table = ttk.Treeview(self.mainframe, columns=list(range(1,columns+2)),
                             height=10, show="headings", selectmode='browse')


        # set the column headings and width
        self.table.heading(1, text='')
        self.table.column(1, width=100)
        for column in range(2,columns+2):
            self.table.heading(column, text=str(column-1))
            self.table.column(column, width=100)

        # put the table on the canvas
        self.table.grid(row=5, column=0, columnspan=3, padx=15, pady=15)

        # iterate through the square object list and get the plant names, then add them
        # to the table (the count becomes an index column)
        count = 0
        for row in square_obj_list:
            count +=1
            value_list = [count]
            for square in row:
                value_list.append(square.return_plant())
            self.table.insert('', 'end', values=value_list)

        self.show_plant_options()

    '''Create en entry form for users to add a plant in a given location.'''
    def show_plant_options(self):
        # create an entry form for row and column
        self.row = tk.StringVar()
        self.column = tk.StringVar()

        # Label the entry boxes
        self.row_label = tk.Label(self.mainframe, text="Row: ").grid(row=0, column=0, padx=15, pady=15)
        self.columnlabel = tk.Label(self.mainframe, text="Column: ").grid(row=1, column=0, padx=15, pady=15)

        # Create the entry boxes
        self.row_entry = tk.Entry(self.mainframe, textvariable=self.row).grid(row=0, column=1, padx=15, pady=15)
        self.column_entry = tk.Entry(self.mainframe, textvariable=self.column).grid(row=1, column=1, padx=15, pady=15)

        # Create the dropdown
        self.selected = tk.StringVar()
        # set default in dropdown
        self.selected.set("Select a Plant")
        # create dropdown menu
        self.zone_dropdown = tk.OptionMenu(self.mainframe, self.selected, *self.plant_list)
        # display the profession dropdown
        self.zone_dropdown.grid(row=2, column=0, padx=15, pady=15)
        # make the button
        self.create_button(self.mainframe, 'Add Plant', 3, 1)


