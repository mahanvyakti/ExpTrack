# importing libraries
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
"""import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import cx_Oracle   
import socket
import datetime 
import bs4
import operator"""
from Interface import  profile, Register, AddIncome, AddExpense, Analysis


def launch(username):

    def openAddIncome():
        AddIncome.launch(username)
        pass


    def openAddExpense():
        AddExpense.launch(username)
        pass
    
    
    def openProfile():
        profile.launch(username)
        #Home.deiconify()
        pass


    def openAnalysis():
        Analysis.launch(username)
        pass

    
    Home = Tk()
    Home.geometry("900x500+100+25")
    Home.title("Expenso :  Dashboard ")
    Home.maxsize(900, 600) # specify the max size the window can expand to
    Home.config(bg="skyblue") # specify background color

    left_frame = Frame(Home, width=50, height=600, bg='grey')
    left_frame.grid(row=0, column=0)

    right_frame = Frame(Home,  width = 800, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=1, padx=10, pady=100)


    container = Frame(right_frame,  width = 500, height=600, bg='grey')
    container.grid(row=10, column=2, padx=150, pady=10)
    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0)

    bProfile = Button(toolbar, text="Profile", command = openProfile) # ADD COMMAND open_profile()
    bProfile.grid(row=0, column=0, padx=30, pady=5)

    bAnalysis = Button(toolbar, text="Analysis", command = openAnalysis)
    bAnalysis.grid(row=1, column=0, padx=30,pady=5)

    bAddIncome = Button(toolbar, text="Add Income",command = openAddIncome) # ADD COMMAND
    bAddIncome.grid(row=2, column=0, padx=30,pady=5)

    bAddExpense = Button(toolbar, text="Add Expense",command = openAddExpense) # ADD COMMAND
    bAddExpense.grid(row=3, column=0, padx=30,pady=5)



    Display_name = Label(container, text = "Welcome User!")
    Display_name.grid(row=0, column=3, columnspan=4, padx=10, pady=50)

    Display_spends = Label(container, text = "Expenses for the Month: ")
    Display_spends.grid(row=2, column=3, padx=25, pady=50)

    Espends = Label(container, text = "//insert total expense here//")
    Espends.grid(row =2, column = 5 , padx=25, pady=50)

    # Back = Button(container, text ="Back")
    # Back.grid(row=16, column=8)
    Home.mainloop()
    

#launch("tantanu")


