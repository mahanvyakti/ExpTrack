# importing libraries
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox as MessageBox
import mysql.connector as mysql
from datetime import *
"""import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import cx_Oracle   
import socket
import datetime 
import bs4
import operator"""
from Interface import profile, AddIncome, AddExpense, Analysis, ExpvsTime


def launch(username):
    Home = Tk()
    Home.geometry("900x500+200+50")
    Home.title("Expenso :  Home ")
    Home.maxsize(900, 600) # specify the max size the window can expand to
    Home.config(bg="skyblue") # specify background color

    def openAddIncome():
        AddIncome.launch(username)
        
    def openAddExpense():
        AddExpense.launch(username)
        
    def openProfile():
        profile.launch(username)
        #Home.deiconify()
        
    def openAnalysis(username):
        Analysis.launch(username)
        
    def logout():
        MsgBox = MessageBox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
            Home.destroy()
    
    left_frame = Frame(Home, width=50, height=600, bg='grey')
    left_frame.grid(row=0, column=0,padx=10)

    right_frame = Frame(Home,  width = 600, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=1, padx=100, pady=100)


    container = Frame(right_frame,  width = 500, height=600, bg='grey')
    container.grid(row=10, column=2, padx=75, pady=20)
    toolbar = Frame(left_frame, width=50, height=600, bg='grey')
    toolbar.grid(row=0, column=0 )

    bProfile = Button(toolbar, text="Profile", command = openProfile) # ADD COMMAND open_profile()
    bProfile.grid(row=0, column=0, padx=5, pady=5)

    bAnalysis = Button(toolbar, text="Analysis", command =lambda: openAnalysis(username))
    bAnalysis.grid(row=1, column=0, padx=5,pady=5)

    bAddIncome = Button(toolbar, text="Add Income",command = openAddIncome) # ADD COMMAND
    bAddIncome.grid(row=2, column=0, padx=5,pady=5)

    bAddExpense = Button(toolbar, text="Add Expense",command = openAddExpense) # ADD COMMAND
    bAddExpense.grid(row=3, column=0, padx=5,pady=5)

    blogout = Button(toolbar, text="Log Out", command = logout)
    blogout.grid(row=4, column=0, padx=5, pady=5)

    notelabel = Label(right_frame, text="NOTE: Always Enter date in 'yyyy-mm-dd hh:mm:ss' format !", font = ('Times New Roman', 12, "bold"), pady =5 )
    notelabel.grid(row = 30, column = 2, padx =10, pady = 10)

    def update():
        tday = datetime.today()
        firstDay = datetime(tday.year, tday.month, 1)
        Today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

        firstDay = str(firstDay)
        Today = str(Today)

        # query = "SELECT amount FROM expense WHERE username = %s  "
        query = "SELECT amount FROM expense WHERE username = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Today,)
            cur.execute(query,params)
            rows = cur.fetchall()
            total_expense = 0
            for row in rows:
                total_expense += row[0]
                
            Espends.configure(text=str(total_expense))
                
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()
        
        query = "SELECT amount FROM income WHERE username = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Today,)
            cur.execute(query,params)
            rows = cur.fetchall()
            total_income = 0
            for row in rows:
                total_income += row[0]
            
            Eincome.configure(text=str(total_income))
                
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    Display_name = Label(container, text = "Welcome to Expenso !", font=('Times New Roman',15,"bold"))
    Display_name.grid(row=0, column=3, columnspan=6, padx=120, pady=25)

    Display_spends = Label(container, text = "Expenses for the Month: ", font=('Times New Roman', 12))
    Display_spends.grid(row=2, column=3, padx=25, pady=20)

    Espends = Label(container, text = "", font=('Times New Roman', 12))
    Espends.grid(row =2, column = 5 , padx=25, pady=20)

    Display_income = Label(container, text = "Income for the Month: ", font=('Times New Roman', 12))
    Display_income.grid(row=3, column=3, padx=25, pady=15)

    Eincome = Label(container, text = "", font=('Times New Roman',12))
    Eincome.grid(row =3, column = 5 , padx=25, pady=15)

    btnRefresh= Button(container, text="Refresh",command = update, font=('Times New Roman', 12))
    btnRefresh.grid(row=8, column = 5, padx=10, pady=10)

    # Back = Button(container, text ="Back")
    # Back.grid(row=16, column=8)
    update()
    Home.mainloop()

# launch("momo")


