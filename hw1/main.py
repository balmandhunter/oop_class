

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    from tkinter import ttk
    from tkinter import *
    import tkinter as tk
    import textwrap

    # --- functions ---

    df2 = None
    current_index = None

    def import_data():
        global df
        df = pd.read_csv("data/IMDB-Movie-Data.csv", index_col=None)
        df.rename(columns={"Runtime (Minutes)": "Runtime (min)",
                           "Revenue (Millions)": "Revenue (mil.)"}, inplace=True)

        return df

    # write a function to wrap text
    def wrap(string, length=25):
        return '\n'.join(textwrap.wrap(string, length))

    # populate the table
    def populate_table(results_table, cols):
        # setup columns and headings
        for col in cols:
            if col in ["Rank", "Year", "Rating"]:
                results_table.column(col, width=40, anchor="w")
            elif col == "Votes":
                results_table.column(col, width=50, anchor="w")
            elif col in ["Runtime (min)", "Revenue (mil.)", "Metascore"]:
                results_table.column(col, width=80, anchor="w")
            else:
                results_table.column(col, anchor="w")
            results_table.heading(col, text=col, anchor="w")

        # populate the table
        for index, row in df2.iterrows():
            results_table.insert("", 0, text=index, values=[wrap(str(x)) for x in list(row)])

    # display pandas data
    def showdata():
        # create results_table with a column for each movie attribute
        cols = list(df2.columns)
        results_table = ttk.Treeview(frame_data, columns=cols, show="headings", height=13)
        results_table.grid(column=0, row=0, padx=0, sticky=W)
        populate_table(results_table, cols)

    def on_select(val):
        global df2
        global current_index

        val = selected.get()
        if val == "all":
            df2 = df
            next_button.grid_forget()
            showdata()
        else:
            df2 = df[df["Title"] == val]
            # find index
            current_index = 0
            for ind in df.index:
                if df["Title"][ind] == val:
                    current_index = ind

            showdata()
            # put next button on the canvas
            next_button.grid(row=2, column=0, sticky=W)

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
    df = import_data()

    # setup and name the window
    root = tk.Tk()
    root.title("Movie Selection App")

    # create a frame widget
    mainframe = ttk.Frame(root, padding="10 15 12 12", width=385, height=450)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    # Style the buttons
    ttk.Style().configure("TButton", padding=6, relief="flat", background="#ccc")

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selected = tk.StringVar()

    # create drop down menu
    # we have a function we execute on button click -- on_select from drop down menu
    dropdown_menu = ttk.Combobox(mainframe, textvariable=selected)
    # add a virtual event to call the "on_select" function when a new movie is selected
    dropdown_menu.bind("<<ComboboxSelected>>", on_select)
    dropdown_menu.set("Select a Movie")
    # add movie names to dropdown
    dropdown_menu["values"] = ["all"] + list(df["Title"].unique())
    dropdown_menu.grid(row=0, column=0, padx=5, pady=15, sticky=W)

    # frame for table and button "Next Data"
    frame_data = tk.Frame(mainframe)
    frame_data.grid(row=1, column=0, padx=5)

    # button "Next Data" - inside "frame_data" - without showing it
    next_button = ttk.Button(frame_data, text="Next Data", command=next_data)

    # make an exit button to end the program
    exit_button = ttk.Button(mainframe, text="EXIT", command=root.destroy)
    exit_button.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    root.mainloop()
