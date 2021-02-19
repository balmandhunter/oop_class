#!/usr/bin/env python
__authors__ = "Silvia Nittel, Berkeley Almand-Hunter"
__copyright__ = "SIE508, Copyright 2021, Orono, ME, USA"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "silvia.nittel@maine.edu"
__status__ = "beta"

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

df = 0
frame_data = None
table = None
#blank_textboxes_tab_two = True
has_loaded_successfully = False

FILENAME = 'contactlist.csv'


# ================================
# DATA LAYER
# ===============================


def d_read_from_pandas_all():
    global df
    df = pd.read_csv(FILENAME, index_col=0)


def d_get_row(selected, col_name):
    #global df2
    df = pd.read_csv(FILENAME, index_col=0)
    df_new = df[df[col_name] == selected]
    return df_new

def d_update_row(firstname,
                          lastname,
                          email,
                          profession,
                          city,
                          state):
    # read the data file into a df
    df = pd.read_csv(FILENAME, index_col=0)
    # get the index of the person with edited details
    idx = df[(df['firstname'] == firstname) & (df['lastname'] == lastname)].index.tolist()
    #save the birthday and gender from the original file
    birthday = df.iloc[idx]['birthday'].values.tolist()[0]
    gender = df.iloc[idx]['gender'].values.tolist()[0]
    # remove the old details from the df
    df.drop(index=idx, inplace=True)

    data = {
        'lastname':[lastname],
        'firstname':[firstname],
        'email': [email],
        'gender': [gender],
        'birthday': [birthday],
        'profession': [profession],
        'city': [city],
        'state': [state]
    }

    C = pd.DataFrame(data)
    # append the new data to the df
    df_new = df.append(C)
    # save the updated data to a file
    df_new.to_csv(FILENAME)
    return 1

def d_append_new_row(firstname, lastname, email):
    # create a DF first with one row to be append
    # then use pd.merge(df_orig, def_new) to merge both DFS
    # then drop duplicates

    df = pd.read_csv(FILENAME, index_col=0)

    data = {
        'lastname': [lastname],
        'firstname': [firstname],
        'email': [email]
    }

    C = pd.DataFrame(data)

    # need email or I get another new attribute email
    cols = ['lastname', 'firstname', 'email']
    merged = pd.merge(df, C, on=cols, how='outer', indicator=False)

    df = merged.drop_duplicates(subset=['lastname', 'firstname'], keep='first')

    df.to_csv(FILENAME)
    return 1

# ================================
# CONTROL LAYER-- handling events
# ===============================

# ============= TAB 1 CONTROL FUNCTIONS ===============

def c_get_data_for_dropdown():
    global df
    d_read_from_pandas_all()
    return

def v_create_choice_dropdown(tab):
    values = ['city', 'profession']
    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selected = tk.StringVar()
    selected.set("Select Search Method")
    # create drop down menu
    options = tk.OptionMenu(tab, selected, *values)
    buttonSearch = tk.Button(tab,
                             text="Search",
                             command=lambda: c_create_dropdown(selected.get(),
                                                               tab3,
                                                               1))

    return options, buttonSearch

def c_create_dropdown(cname, tab, grid_row):
    col_name=cname
    values = ['all'] + list(df[col_name].unique())

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selected = tk.StringVar()
    selected.set("Search by " + cname)
    # create drop down menu
    options = tk.OptionMenu(tab, selected, *values)
    buttonSearch = tk.Button(tab,
                                text="Retrieve contact",
                                command=lambda: c_load_data_results(tab,
                                                                    selected.get(),
                                                                    col_name,
                                                                    grid_row))


    return options, buttonSearch

def c_create_display_table(tab):
    table = tk.Frame(tab)
    table.grid(row=1, column=0)

    # fill frame with table
    row, column = df.shape
    for r in range(row):
        for c in range(column):
            e1 = tk.Entry(table)
            e1.insert(1, df.iloc[r, c])
            e1.grid(row=r, column=c, padx=2, pady=2)
            e1.config(state='disabled')

def c_create_beautiful_display_table(tab, df, grid_row):
    table = ttk.Treeview(tab, columns=(1, 2, 3), height=10, show="headings")

    table.heading(1, text="Last Name")
    table.heading(2, text="First Name")
    table.heading(3, text="Email")

    table.column(1, width=110)
    table.column(2, width=110)
    table.column(3, width=250)

    table.grid(row=grid_row, column=0, columnspan=3, padx=15, pady=15)
    row, column = df.shape
    for r in range(row):
        table.insert('', 'end', values=(df.iloc[r, 0], df.iloc[r, 1], df.iloc[r, 2]))

    return 1

def c_load_data_results(tab, selected, col_name, grid_row):
    global table
    global df2
    #call data layer to retrieve all data? We called that already for the drop down menu
    d_read_from_pandas_all()
    # destroy old frame with table
    if table:
       table.destroy()

    if selected == 'all':
        c_create_beautiful_display_table(tab, df, grid_row)
    else:
        df2 = d_get_row(selected, col_name)
        c_create_beautiful_display_table(tab, df2, grid_row)

    return has_loaded_successfully

# ============= TAB 2 CONTROL FUNCTIONS ===============

def c_append_new_record():
    #global blank_textboxes_tab_two
    blank_textbox_count = 0

    if fNameTabTwo.get()  == "":
        blank_textbox_count = blank_textbox_count + 1

    if famTabTwo.get() ==  "":
        blank_textbox_count = blank_textbox_count + 1

    if emailTabTwo.get() == "":
        blank_textbox_count = blank_textbox_count + 1

    if blank_textbox_count > 0:
        blank_textboxes_tab_two = True
        messagebox.showinfo("App Error", "Blank Text boxes")
    elif blank_textbox_count == 0:
        blank_textboxes_tab_two = False

        d_append_new_row(fNameTabTwo.get(), famTabTwo.get(), emailTabTwo.get())

# ============= TAB 4 CONTROL FUNCTIONS ===============

def c_create_display_entry_form(tab,
                                selected,
                                col_name):
    global df2

    #call data layer to retrieve all data? We called that already for the drop down menu
    d_read_from_pandas_all()
    # grab the selected row of the df
    df2 = d_get_row(selected, col_name)
    v_setup_blank_entry_fields()

    # fill the entry form with the selected person's data
    firstEntryTab4.insert(0, df2['firstname'].values[0])
    familyEntryTab4.insert(0, df2['lastname'].values[0])
    emailEntryTab4.insert(0, df2['email'].values[0])
    professionEntryTab4.insert(0, df2['profession'].values[0])
    cityEntryTab4.insert(0, df2['city'].values[0])
    stateEntryTab4.insert(0, df2['state'].values[0])
    #display the filled entry fields
    v_show_tab4_entry_fields()

    return has_loaded_successfully

def c_update_record():
    #global blank_textboxes_tab_two
    blank_textbox_count = 0

    if emailTab4.get()  == "":
        blank_textbox_count = blank_textbox_count + 1

    if professionTab4.get() ==  "":
        blank_textbox_count = blank_textbox_count + 1

    if cityTab4.get() == "":
        blank_textbox_count = blank_textbox_count + 1

    if stateTab4.get() == "":
        blank_textbox_count = blank_textbox_count + 1

    if blank_textbox_count > 0:
        blank_textboxes_tab_two = True
        messagebox.showinfo("App Error", "Blank Text boxes")
    elif blank_textbox_count == 0:
        blank_textboxes_tab_two = False

        d_update_row(fNameTab4.get(),
                     famTab4.get(),
                     emailTab4.get(),
                     professionTab4.get(),
                     cityTab4.get(),
                     stateTab4.get())

# ============= start Appliction-- CONTROL FUNCTIONS ===============

def c_start_app():
    global form

    form = None
    v_initialize_GUI()
    form.mainloop()


# ================================
# VIEW LAYER-- handling events
# ===============================

def v_initialize_GUI():
    global form
    global tab1
    global tab2
    global tab3
    global tab4

    global selected
    global fNameTabTwo
    global famTabTwo
    global emailTabTwo
    form = tk.Tk()
    form.title("Contact List Form")
    form.geometry("600x500")
    tab_parent = ttk.Notebook(form)

    tab1 = ttk.Frame(tab_parent)
    tab2 = ttk.Frame(tab_parent)
    tab3 = ttk.Frame(tab_parent)
    tab4 = ttk.Frame(tab_parent)


    tab_parent.bind("<<NotebookTabChanged>>", v_on_tab_selected)

    tab_parent.add(tab1, text="All contacts")
    tab_parent.add(tab2, text="Add new contact")
    tab_parent.add(tab3, text="Search")
    tab_parent.add(tab4, text="Update contact")

    tab_parent.pack(expand=1, fill='both')
    v_make_tab1()
    v_make_tab2()
    v_make_tab3()
    v_make_tab4()

    return form

def v_setup_blank_entry_fields():
    global fNameTab4
    global famTab4
    global emailTab4
    global professionTab4
    global cityTab4
    global stateTab4
    global firstLabelTab4
    global familyLabelTab4
    global emailLabelTab4
    global professionLabelTab4
    global cityLabelTab4
    global stateLabelTab4
    global firstEntryTab4
    global familyEntryTab4
    global emailEntryTab4
    global professionEntryTab4
    global cityEntryTab4
    global stateEntryTab4
    global buttonCommit

    fNameTab4 = tk.StringVar()
    famTab4 = tk.StringVar()
    emailTab4 = tk.StringVar()
    professionTab4 = tk.StringVar()
    cityTab4 = tk.StringVar()
    stateTab4 = tk.StringVar()

    firstLabelTab4 = tk.Label(tab4, text="First Name: ")
    familyLabelTab4 = tk.Label(tab4, text="Last Name: ")
    emailLabelTab4 = tk.Label(tab4, text="Email*: ")
    professionLabelTab4 = tk.Label(tab4, text="Profession*: ")
    cityLabelTab4 = tk.Label(tab4, text="City*: ")
    stateLabelTab4 = tk.Label(tab4, text="State*: ")

    firstEntryTab4 = tk.Entry(tab4, textvariable=fNameTab4)
    familyEntryTab4 = tk.Entry(tab4, textvariable=famTab4)
    emailEntryTab4 = tk.Entry(tab4, textvariable=emailTab4)
    professionEntryTab4 = tk.Entry(tab4, textvariable=professionTab4)
    cityEntryTab4 = tk.Entry(tab4, textvariable=cityTab4)
    stateEntryTab4 = tk.Entry(tab4, textvariable=stateTab4)

    buttonCommit = tk.Button(tab4,
                             text="Update Contact",
                             command=c_update_record)

def v_show_tab4_entry_fields():
    firstLabelTab4.grid(row=1, column=0, padx=15, pady=15)
    firstEntryTab4.grid(row=1, column=1, padx=15, pady=15)

    familyLabelTab4.grid(row=2, column=0, padx=15, pady=15)
    familyEntryTab4.grid(row=2, column=1, padx=15, pady=15)

    emailLabelTab4.grid(row=3, column=0, padx=15, pady=15)
    emailEntryTab4.grid(row=3, column=1, padx=15, pady=15)

    professionLabelTab4.grid(row=4, column=0, padx=15, pady=15)
    professionEntryTab4.grid(row=4, column=1, padx=15, pady=15)

    cityLabelTab4.grid(row=5, column=0, padx=15, pady=15)
    cityEntryTab4.grid(row=5, column=1, padx=15, pady=15)

    stateLabelTab4.grid(row=6, column=0, padx=15, pady=15)
    stateEntryTab4.grid(row=6, column=1, padx=15, pady=15)
    buttonCommit.grid(row=7, column=0, padx=15, pady=15)


def v_make_tab1():
    global df
    global selected

    # call data layer function
    c_get_data_for_dropdown()
    # create the dropdown
    options, buttonSearch = c_create_dropdown('lastname', tab1, 1)

    # show widgets
    options.grid(row=0, column=0, padx=15, pady=15)
    buttonSearch.grid(row=0, column=1, padx=15, pady=15)
    return 1

def v_make_tab2():
    # we need to share them with the controller to retrieve the values
    global fNameTabTwo
    global famTabTwo
    global emailTabTwo
    # =============== Widgets for TAB TWO
    fNameTabTwo = tk.StringVar()
    famTabTwo = tk.StringVar()
    emailTabTwo = tk.StringVar()

    firstLabelTabTwo = tk.Label(tab2, text="First Name: ")
    familyLabelTabTwo = tk.Label(tab2, text="Last Name: ")
    emailLabelTabTwo = tk.Label(tab2, text="Email: ")

    firstEntryTabTwo = tk.Entry(tab2, textvariable=fNameTabTwo)
    familyEntryTabTwo = tk.Entry(tab2, textvariable=famTabTwo)
    emailEntryTabTwo = tk.Entry(tab2, textvariable=emailTabTwo)
    buttonCommit = tk.Button(tab2, text="Add Contact to List", command=c_append_new_record)

    # === ADD WIDGETS TO GRID ON TAB TWO
    firstLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
    firstEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)

    familyLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
    familyEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)

    emailLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
    emailEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)
    buttonCommit.grid(row=4, column=0, padx=15, pady=15)

    return 1

def v_make_tab3():
    global df
    global selectedt3

    # call data layer function
    c_get_data_for_dropdown()

    options, buttonSearch = v_create_choice_dropdown(tab3)
    options.grid(row=0, column=0, padx=15, pady=15)
    buttonSearch.grid(row=0, column=1, padx=15, pady=15)


    return 1


def v_make_tab4():
    global df
    global selectedt4

    # call data layer function
    c_get_data_for_dropdown()
    col_name='lastname'
    values = list(df[col_name].unique())

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selectedt4 = tk.StringVar()
    selectedt4.set("Select a Name")
    # # create drop down menu
    options_t4 = tk.OptionMenu(tab4, selectedt4, *values)
    buttonSearch_t4 = tk.Button(tab4,
                                text="Retrieve contact",
                                command=lambda: c_create_display_entry_form(tab4,
                                                                            selectedt4.get(),
                                                                            col_name))


    # ================================================================
    # =============== Add Widgets to GRID on TAB ONE
    options_t4.grid(row=0, column=0, padx=15, pady=15)
    buttonSearch_t4.grid(row=0, column=1, padx=15, pady=15)
    return 1


# === defining an event  ===============

def v_on_tab_selected(event):

    global blank_textboxes_tab_two

    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "All Records":
        c_load_data_results()

    if tab_text == "Add New Record":
        blank_textboxes_tab_two = True

# ==== form code ============

c_start_app()
