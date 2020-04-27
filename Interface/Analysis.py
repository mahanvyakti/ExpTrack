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
from Interface import ExpvsTime
#from Interface 

def launch(username):
    Analysis = Tk()
    Analysis.geometry("1200x600+50+30")
    Analysis.title("Expenso :  Your Analysis ")
    # Analysis.maxsize(1200,1200) # specify the max size the window can expand to
    Analysis.config(bg="skyblue")
    
    def back():
        Analysis.withdraw()

    def redirectToExpvsTime():
        #Analysis.withdraw()
        ExpvsTime.launch(username)



    left_frame = Frame(Analysis, width=20, height=600, bg='skyblue')
    left_frame.grid(row=0, column=0,padx=10)
    #bottom_frame = Frame(Analysis, width=20, height=600, bg='grey')
    #bottom_frame.grid(row=1, column=0)

    right_frame = Frame(Analysis, width = 750, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=1, padx= 40, pady=70)
    

    container1 = Frame(right_frame,  width = 600, height=600, bg='lightgrey')
    container1.grid(row=10, column=2, padx =10, pady =5)
    container2 = Frame(right_frame, width = 230, height=450, bg ='lightgrey')
    container2.grid(row=10, column=3, padx =10, pady =15)

    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0,padx=5)

    Back = Button(toolbar, text="Back", width = 5, height =2, command=back, font=('Times New Roman', 10))
    Back.grid(row=1, column=0, padx=5, pady=5)
    newgraph = Button(toolbar, text="More Analysis",font=('Times New Roman', 16),command = redirectToExpvsTime)
    newgraph.grid(row=0, column=0, padx=5,pady=5)
    Heading1 = Label(container1, text= "Categories wise Distribution", font=('Times New Roman', 16, "bold"))
    Heading1.grid(row=0, column=2, padx=25, pady=25)
    Heading2 = Label(container2, text= "Mode wise Distribution",font=('Times New Roman', 16, "bold"))
    Heading2.grid(row=0, column=2, padx=25, pady=25)

    # Graphs 
    #-------------------------------------------------------------------#
    def show_graphs(expense_list, categories, mode_list, mode, month_expense):  
        
        #category wise pie chart

        fig, ax = plt.subplots(figsize=(4.12, 3), subplot_kw=dict(aspect="equal"))

        wedges, texts = ax.pie(expense_list, wedgeprops=dict(width=0.5), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.5)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(categories[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)

        canvas = FigureCanvasTkAgg(fig, container1)
        canvas.get_tk_widget().grid(row =4, column =2, padx=15, pady=20)


        #mode wise pie chart
    
        fig, ax = plt.subplots(figsize=(4.12, 3), subplot_kw=dict(aspect="equal"))

        wedges, texts = ax.pie(mode_list, wedgeprops=dict(width=0.5), startangle=-40)

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(mode[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)

        canvas = FigureCanvasTkAgg(fig, container2)
        canvas.get_tk_widget().grid(row =4, column =2, padx=15, pady=20)


    #-------------------------------------------------------------------#

    def typevsExp():
        
        query = "SELECT amount,category,mode,date FROM expense WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            rows = cur.fetchall()
            print(rows)
            category_list = []
            for row in rows:
                category_list.append(row[1])
            print(category_list)        
            categories = [] 
            for i in category_list: 
                if i not in categories: 
                    categories.append(i)
            for item in categories:
                if item =='Null':
                    categories.remove(item)
            # print(categories)
            
            
            expense_list =[0] * len(categories)
            i=0
            for item in categories:
                for row in rows:
                    if item == row[1]:
                        expense_list[i] += row[0] 
                i+=1

            mode=['Cash', 'Card', 'Cheque', 'UPI']
            mode_list =[0] * len(mode)
            i=0
            for item in mode:
                for row in rows:
                    if item == row[2]:
                        mode_list[i] += row[0] 
                i+=1
        
            print(mode_list)
            # print(expense_list)

            month_expense = [0]*12
            for row in rows:
                #month = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                month = row[3].month
                month_expense[month-1] += row[0] 

            show_graphs(expense_list, categories,mode_list,mode, month_expense)

        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    typevsExp()


    Analysis.mainloop()

# launch("momo")

