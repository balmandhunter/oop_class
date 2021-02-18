#!/usr/bin/env python
__author__ = "Silvia Nittel"
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
    #print(df.head(10))


def d_get_row_by_name(name):
    #global df2
    df = pd.read_csv(FILENAME, index_col=0)
    df_new = df[df['lastname'] == name]
    return df_new

def d_get_row_by_profession(profession):
    #global df2
    df = pd.read_csv(FILENAME, index_col=0)
    df_new = df[df['profession'] == profession]
    return df_new

def d_append_new_row(firstname, lastname, email):
    # create a DF first with one row to be append
    # then use pd.merge(df_orig, def_new) to merge both DFS
    # then drop duplicates

    df = pd.read_csv(FILENAME, index_col=0)
    #print(df.head(11))

    data = {
        'lastname': [lastname],
        'firstname': [firstname],
        'email': [email]
    }

    C = pd.DataFrame(data)
    #print("added row: \n", C.head(11))

    # need email or I get another new attribute email
    cols = ['lastname', 'firstname', 'email']
    merged = pd.merge(df, C, on=cols, how='outer', indicator=False)

    #print("merged df:\n", merged.head(11))
    df = merged.drop_duplicates(subset=['lastname', 'firstname'], keep='first')
    #print(df.head(10))

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


def c_create_beautiful_display_table(tab, df):
    table = ttk.Treeview(tab, columns=(1, 2, 3), height=10, show="headings")

    table.heading(1, text="Last Name")
    table.heading(2, text="First Name")
    table.heading(3, text="Email")

    table.column(1, width=110)
    table.column(2, width=110)
    table.column(3, width=250)

    table.grid(row=1, column=0, columnspan=3, padx=15, pady=15)
    row, column = df.shape
    for r in range(row):
        table.insert('', 'end', values=(df.iloc[r, 0], df.iloc[r, 1], df.iloc[r, 2]))

    return 1

# def c_load_data_results(tab, selected):
#     global table
#     global df
#     global df2
#     #call data layer to retrieve all data? We called that already for the drop down menu
#     d_read_from_pandas_all()
#     # destroy old frame with table
#     if table:
#        table.destroy()
#
#
#     if selected == 'all':
#         c_create_beautiful_display_table(tab, df)
#     else:
#         df2 = d_get_row_by_name(selected)
#         c_create_beautiful_display_table(tab, df2)
#
#     return has_loaded_successfully


def c_load_data_results_tab1():
    global table
    global df
    global df2
    #call data layer to retrieve all data? We called that already for the drop down menu
    d_read_from_pandas_all()
    # destroy old frame with table
    if table:
       table.destroy()


    if selected == 'all':
        c_create_beautiful_display_table(tab1, df)
    else:
        selected_name = selected.get()
        df2 = d_get_row_by_name(selected_name)
        c_create_beautiful_display_table(tab1, df2)

    return has_loaded_successfully


def c_load_data_results_tab3():
    global table
    global df
    global df2
    #call data layer to retrieve all data? We called that already for the drop down menu
    d_read_from_pandas_all()
    # destroy old frame with table
    if table:
       table.destroy()


    if selectedt3 == 'all':
        c_create_beautiful_display_table(tab3, df)
    else:
        selected_profession = selectedt3.get()
        df2 = d_get_row_by_profession(selected_profession)
        c_create_beautiful_display_table(tab3, df2)

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

    global selected
    global fNameTabTwo
    global famTabTwo
    global emailTabTwo
    form = tk.Tk()
    form.title("Contact List Form")
    form.geometry("600x380")
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

    return form

def v_make_tab1():
    global df
    global selected

    # call data layer function
    c_get_data_for_dropdown()
    values = ['all'] + list(df['lastname'].unique())

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selected = tk.StringVar()
    selected.set("all")
    # create drop down menu
    options = tk.OptionMenu(tab1, selected, *values)
    buttonSearch = tk.Button(tab1, text="Retrieve contact", command=c_load_data_results_tab1)

    # ================================================================
    # =============== Add Widgets to GRID on TAB ONE
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
    values = ['all'] + list(df['profession'].unique())

    # input variable has to be a StringVar, special var for Tkinter to grab user input
    selectedt3 = tk.StringVar()
    selectedt3.set("all")
    # create drop down menu
    options_t3 = tk.OptionMenu(tab3, selectedt3, *values)
    buttonSearch_t3 = tk.Button(tab3, text="Retrieve contact", command=c_load_data_results_tab3)

    # ================================================================
    # =============== Add Widgets to GRID on TAB ONE
    options_t3.grid(row=0, column=0, padx=15, pady=15)
    buttonSearch_t3.grid(row=0, column=1, padx=15, pady=15)
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
