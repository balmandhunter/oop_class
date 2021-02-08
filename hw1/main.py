import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
import textwrap


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # --- functions ---

    df2 = None
    table = None
    current_index = None


    # a function we call to display pandas data
    def showdata():
        # create Treeview with a column for each movie atrribute
        cols = list(df2.columns)
        treeview = ttk.Treeview(mainframe, columns=cols, show='headings', height=len(df2))
        treeview.grid(column=0, row=1, padx=5, sticky=(E, W))

        for i in cols:
            treeview.column(i, anchor="w")
            treeview.heading(i, text=i, anchor='w')

        for index, row in df2.iterrows():
            treeview.insert("", 0, text=index, values=list(row))

        treeview.column("Rank", width=50, stretch=NO)
        treeview.column("Year", width=50, stretch=NO)
        treeview.column("Rating", width=50, stretch=NO)
        treeview.column("Votes", width=50, stretch=NO)
        treeview.column("Title", width=100, stretch=NO)
        treeview.column("Genre", width=100, stretch=NO)
        treeview.column("Director", width=100, stretch=NO)
        treeview.column("Description", width=100, stretch=NO)
        treeview.column("Actors", width=100, stretch=NO)
        treeview.column("Runtime (Minutes)", width=110, stretch=NO)
        treeview.column("Revenue (Millions)", width=110, stretch=NO)
        treeview.column("Metascore", width=100, stretch=NO)







    def on_select(val):
        global df2
        global current_index

        val = selected.get()
        if val == 'all':
            df2 = df
            next_button.grid_forget()
            showdata()
        else:
            df2 = df[df['Title'] == val]
            # find index
            current_index = 0
            for ind in df.index:
                if df['Title'][ind] == val:
                    current_index = ind

            # put next button on the canvas
            next_button.grid(row=0, column=0)
            showdata()


    def next_data():
        global current_index
        global df2

        if current_index < len(df) - 1:
            current_index = current_index + 1
        df2 = df.iloc[[current_index]]
        showdata()


    # --- main ---
    frame_data = None

    # import the data
    df = pd.read_csv('data/IMDB-Movie-Data.csv', index_col=None)

    # setup and name the window
    root = tk.Tk()
    root.title("Simple Pandas App")

    # create a frame widget
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selected = tk.StringVar()

    # create drop down menu
    # we have a function we execute on button click -- on_select from drop down menu
    options = ttk.Combobox(mainframe, textvariable=selected)
    # add a virtual event to call the "on_select" function when a new movie is selected
    options.bind('<<ComboboxSelected>>', on_select)
    # add movie names to dropdown
    options['values'] = ['all'] + list(df['Title'].unique())
    options.grid(column=1, row=1, padx=5, pady=15, sticky=W)

    # Make a label for the dropdown menu
    selected_entry = ttk.Label(mainframe, width=15, text='Select a Movie: ')
    selected_entry.grid(column=0, row=1, padx=5, sticky=(E, W))

    # frame for table and button "Next Data"
    frame_data = tk.Frame(mainframe)
    frame_data.grid(row=2, column=0, padx=5, pady=5)

    # button "Next Data" - inside "frame_data" - without showing it
    next_button = tk.Button(frame_data, text="Next Data", command=next_data)

    # table with data - inside "frame_data" - without showing it
    table = tk.Frame(frame_data)
    table.grid(row=0, column=0)

    exit_button = tk.Button(mainframe, text="EXIT", command=root.destroy)
    exit_button.grid(row=3, column=0, padx=5, pady=5, sticky=W)

    root.mainloop()