from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd 

def launch(username):
    Analysis = Tk()
    Analysis.geometry("900x500+100+25")
    Analysis.title("Expenso :  Your Analysis ")
    Analysis.maxsize(900, 600) # specify the max size the window can expand to
    Analysis.config(bg="skyblue")

    def back():
        Analysis.withdraw()
    
    left_frame = Frame(Analysis, width=50, height=600, bg='grey')
    left_frame.grid(row=0, column=0)

    right_frame = Frame(Analysis, width = 750, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=1, padx=10, pady=50)

    container1 = Frame(right_frame,  width = 230, height=450, bg='lightgrey')
    container1.grid(row=10, column=2, padx =15, pady =15)
    container2 = Frame(right_frame, width = 230, height=450, bg ='lightgrey')
    container2.grid(row=10, column=3, padx =15, pady =15)
    container3 = Frame(right_frame, width = 230, height = 450, bg = 'lightgrey')
    container3.grid(row=10, column = 4, padx =15, pady =15)

    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0)

    Back = Button(toolbar, text="Back", width = 5, height =2, command=back)
    Back.grid(row=0, column=0, padx=15, pady=5, columnspan=2)

    Heading1 = Label(container1, text= "Categories wise Distribution")
    Heading1.grid(row=0, column=2, padx=25, pady=25)
    Heading2 = Label(container2, text= "Mode wise Distribution")
    Heading2.grid(row=0, column=2, padx=25, pady=25)
    Heading3 = Label(container3, text = "Spending vs Time")
    Heading3.grid(row=0, column=2, padx=35, pady=25)

    # Graphs 
    #-------------------------------------------------------------------#
    f= Figure(figsize=(2,2), dpi=100)
    a = f.add_subplot(111)
    piesizes = [100, 25, 6]
    mycolours = ['red', 'green', 'blue']
    a.pie(piesizes, colors = mycolours)
    a.axis('equal')
    canvas = FigureCanvasTkAgg(f, container1)
    canvas.get_tk_widget().grid(row =4, column =2, padx=15, pady=20)

    f= Figure(figsize=(2,2), dpi=100)
    a = f.add_subplot(111)
    piesizes = [100, 25, 6]
    mycolours = ['red', 'green', 'blue']
    a.pie(piesizes, colors = mycolours)
    a.axis('equal')
    canvas = FigureCanvasTkAgg(f, container2)
    canvas.get_tk_widget().grid(row =4, column =2,padx=15,pady=20)

    f= Figure(figsize=(2,2), dpi=100)
    a = f.add_subplot(111)
    a.plot([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9])
    canvas = FigureCanvasTkAgg(f, container3)
    canvas.get_tk_widget().grid(row =4, column =2,padx=15,pady=20)

    #-------------------------------------------------------------------#
    Analysis.mainloop()