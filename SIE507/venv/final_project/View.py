import tkinter as tk
from tkinter import ttk
from tkinter import *
import pandas as pd


class View:
    def __init__(self):
        self.root1 = tk.Tk()
        self.root1.withdraw()
        self.root = tk.Toplevel(self.root1)
        self.initialize_GUI()

    '''Make a call back to the controller to send button commands'''
    def call_back(self, controller):
        self.controller = controller

    '''Initialize the GUI'''
    def initialize_GUI(self):
        # setup and name the window
        self.root.title("Maine Garden Planner")
        self.mainframe = ttk.Frame(self.root)
        self.mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

    '''Destroy all of the widgets before making a new window'''
    def clear_canvas(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    '''Create a button and add it to the button dictionary'''
    def create_button(self, frame, name, row, column, buttons, alignment=None):
        # Style the buttons
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
        buttons[name] = ttk.Button(frame)
        buttons[name]["text"] = name
        buttons[name].grid(row=row, column=column, padx=15, pady=10, sticky=alignment)


class ZonePlanSelectionView():
    def __init__(self, dropdown_topic, view):
        self.dropdown_topic = dropdown_topic
        self.view = view

    '''Create the initial view in the GUI'''
    def make_initial_view(self):
        if self.dropdown_topic == 'view':
            # create the zone dropdown
            options = ['3','4','5']
            title = 'Select Your Gardening Zone'
        elif self.dropdown_topic == 'plan_type':
            self.view.clear_canvas()
            options = ['Start a Follow-on Plan from Last Year\'s Plan',
                       'Load Saved Plan (current year)',
                       'Start a New Plan']
            title = 'Select a Plan Type'
        self.create_dropdown(title, options, 1, 0, self.dropdown_topic)

        # display the zone dropdown
        self.zone_dropdown.grid(row=0, column=0, padx=15, pady=15, ipadx=10)


        # make an quit button to end the program
        quit_button = ttk.Button(self.view.mainframe, text="Quit", command=self.view.root.destroy)
        quit_button.grid(row=2, column=0, padx=15, pady=5, sticky='W')



    '''Create the dropdown menu'''
    def create_dropdown(self, title, values, buttonrow, buttoncol, dropdown_topic):
        # input variable has to be a StringVar, special var for Tkinter to grab user input
        self.selected = tk.StringVar()
        # set default in dropdown
        self.selected.set(title)
        # create drop down menu
        self.zone_dropdown = tk.OptionMenu(self.view.mainframe, self.selected, *values)
        # set the command for the button
        if dropdown_topic == 'view':
            button_command = self.view.controller.set_zone_and_update_view
        elif dropdown_topic == 'plan_type':
            button_command = self.view.controller.get_and_send_plan_selection
        # make the button
        ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")
        submit_button = ttk.Button(self.view.mainframe, text="Submit", command=button_command)
        submit_button.grid(row=buttonrow, column=buttoncol, padx=15, pady=10, sticky='W')


        # Bind the button to the  function
        # self.buttons['Submit'].configure(command=button_command)

class SizeView():
    def __init__(self, view):
        self.view = view

    '''Create the view where users input the size of their garden bed'''
    def make_size_view(self):
        self.view.clear_canvas()
        self.length = tk.StringVar()
        self.width = tk.StringVar()

        # Label the entry boxes
        self.length_label = tk.Label(self.view.mainframe, text="Garden Bed Length (ft): ").grid(row=0, column=0,
                                                                                                padx=15, pady=15,
                                                                                                sticky='W')
        self.width_label = tk.Label(self.view.mainframe, text="Garden Bed Width (ft): ").grid(row=1, column=0,
                                                                                              padx=15, pady=15,
                                                                                              sticky='W')

        # Create the entry boxes
        self.length_entry = tk.Entry(self.view.mainframe, textvariable=self.length).grid(row=0, column=1,
                                                                                         padx=15, pady=15,
                                                                                         sticky='W')
        self.width_entry = tk.Entry(self.view.mainframe, textvariable=self.width).grid(row=1, column=1,
                                                                                       padx=15, pady=15,
                                                                                       sticky='W')

        # Create the submit button
        submit_button = ttk.Button(self.view.mainframe,
                                   text="Submit",
                                   command=self.view.controller.get_bed_size)
        submit_button.grid(row=2, column=0, padx=15, pady=10, sticky='W')

class BedPlanView():
    def __init__(self, list_of_plants, view):
        self.buttons = {}
        self.list_of_plants = list_of_plants
        self.view = view

    '''Return the garden plan'''
    def show_bed(self, square_obj_list, length, width, df_plant):
        self.view.clear_canvas()

        tk.Label(self.view.mainframe, text="Garden Plan (plant and count per square foot): ").grid(row=4,
                                                                                                   column=0,
                                                                                                   padx=15,
                                                                                                   pady=15,
                                                                                                   sticky='W')
        columns = width
        self.table = ttk.Treeview(self.view.mainframe, columns=list(range(1,columns+2)),
                             height=length+1, show="headings", selectmode='browse')

        # set the column headings and width
        self.table.heading(1, text='')
        self.table.column(1, width=100)
        for column in range(2,columns+2):
            self.table.heading(column, text=str(column-1))
            self.table.column(column, width=100)

        # put the table on the canvas
        self.table.grid(row=5, column=0, columnspan=2, padx=15, pady=15, sticky='W')

        # iterate through the square object list and get the plant names, then add them
        # to the table (the count becomes an index column)
        count = 0
        for row in square_obj_list:
            count +=1
            value_list = [count]
            for square in row:
                name = square.return_plant_name()
                if name != '(empty)':
                    count = df_plant.count_per_square[df_plant.name == name].values[0]
                    value_list.append(name + ' (' + str(count) + ')')
                else:
                    value_list.append(name)
            self.table.insert('', 'end', values=value_list)

        self.show_plant_options()

    '''Return the planting dates table'''
    def show_planting_dates(self, df_planting):
        # make a title for the table
        tk.Label(self.view.mainframe, text="Plant List: ").grid(row=6, column=0, padx=15,
                                                                pady=15, ipadx=10, sticky='W')

        # set up the empty table
        self.table = ttk.Treeview(self.view.mainframe, columns=list(range(0,6)),
                                  height=len(df_planting)+1, show="headings", selectmode='browse')
        # set the column headings and width
        self.table.heading(0, text='Plant Name')
        self.table.column(0, width = 100)
        self.table.heading(1, text='Total Count')
        self.table.column(1, width = 100)
        self.table.heading(2, text='Month to Start Indoors')
        self.table.column(2, width = 150)
        self.table.heading(3, text='Month to Transplant')
        self.table.column(3, width = 150)
        self.table.heading(4, text='Month to Direct Seed')
        self.table.column(4, width = 150)
        self.table.heading(5, text='Month to Harvest')
        self.table.column(5, width = 150)
        # put the table on the canvas
        self.table.grid(row=7, column=0, columnspan=10, padx=15, pady=15, sticky='W')
        # iterate through the df and get the data for each plant, then add them
        # to the table (the count becomes an index column)
        for idx, row in df_planting.iterrows():
            row_list = []
            for entry in row:
                row_list.append(entry)
            self.table.insert('', 'end', values=row_list)

    '''Create en entry form for users to add a plant in a given location.'''
    def show_plant_options(self):
        tk.Label(self.view.mainframe, text="To add a plant, entering the desired location "
                                      "and select a plant from the dropdown menu: ").grid(row=0,
                                                                                           columnspan=2,
                                                                                           column=0,
                                                                                           padx=15,
                                                                                           pady=15,
                                                                                           sticky='W')

        # create an entry form for row and column
        self.row = tk.StringVar()
        self.column = tk.StringVar()

        # Label the entry boxes
        self.row_label = tk.Label(self.view.mainframe, text="Row: ").grid(row=1, column=0,
                                                                          padx=15, pady=10,
                                                                          sticky='W')
        self.columnlabel = tk.Label(self.view.mainframe, text="Column: ").grid(row=2, column=0,
                                                                               padx=15, pady=10,
                                                                               sticky='W')

        # Create the entry boxes
        self.row_entry = tk.Entry(self.view.mainframe, textvariable=self.row).grid(row=1, column=1,
                                                                                   padx=15, pady=10,
                                                                                   sticky='W')
        self.column_entry = tk.Entry(self.view.mainframe, textvariable=self.column).grid(row=2, column=1,
                                                                                         padx=15, pady=10,
                                                                                         sticky='W')

        self.create_plant_dropdown()

    '''Create a dropdown for plant selection'''
    def create_plant_dropdown(self):
        # Create the dropdown
        self.selected = tk.StringVar()
        # set default in dropdown
        self.selected.set("Select a Plant")
        # create dropdown menu
        self.plant_dropdown = tk.OptionMenu(self.view.mainframe, self.selected, *self.list_of_plants)
        # display the profession dropdown
        self.plant_dropdown.grid(row=3, column=0, padx=15, pady=10, ipadx=10, sticky='W')
        # make the 'add plant' button
        submit_button = ttk.Button(self.view.mainframe, text="Add Plant", command=self.view.controller.get_plant_location)
        submit_button.grid(row=3, column=1, padx=15, pady=10, sticky='W')
        # make the 'save and quit' button
        quit_button = ttk.Button(self.view.mainframe, text="Save and Quit", command=self.view.root.destroy)
        quit_button.grid(row=8, column=0, padx=15, pady=5, sticky='W')