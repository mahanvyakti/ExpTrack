from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd 
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from datetime import *


def launch(username):
    Root = Tk()
    Root.geometry("750x600+270+25")
    Root.title("Expenso :  Expense versus Time")
    # Analysis.maxsize(1200,1200) # specify the max size the window can expand to
    Root.config(bg="skyblue")

    def back():
        Root.withdraw()


    rightframe = Frame(Root, width = 750, height=600, bg='lightgrey')
    rightframe.grid(row=0, column=4, padx= 20, pady=20)
    leftframe = Frame(Root, width = 750, height=600, bg='skyblue')
    leftframe.grid(row=0, column=0, padx= 20, pady=20)
    btnBack = Button(leftframe, text = "Back", command = back)
    btnBack.grid(row=5, column =1, padx=10, pady=10, columnspan=2)
    
    

    def show_graph(month_expense):
        f = Figure(figsize=(5,5), dpi=100)
        ax = f.add_subplot(111)
        data = month_expense
        ind = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # the x locations for the groups
        width = .5
        #ax.tick_params(labelrotation=90)
        ax.set_title("Expense vs Time")
        rects1 = ax.bar(ind, data, width)
        canvas = FigureCanvasTkAgg(f, rightframe)
        canvas.get_tk_widget().grid(row=4, column=2,padx=10,pady=10)
    

    def query():
        query = "SELECT amount,date FROM expense WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            rows = cur.fetchall()
            # print(rows)

            month_expense = [0]*12
            for row in rows:
                #month = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                month = row[1].month
                month_expense[month-1] += row[0]

            show_graph(month_expense)

        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    query()

    Root.mainloop()

# launch("momo")    