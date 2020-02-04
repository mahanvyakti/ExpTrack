#importing libraries
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import cx_Oracle   
import socket
import datetime
import bs4
import operator

def register():
    start.withdraw()
    register = Tk()
    register.geometry('700x700+450+25')
    register.title("Expenso : Register ")
    lRegTitle = Label(register, text="Welcome to Expenso !", font=('Times New Roman', 16))
    lRegSubTitle = Label(register, text="Please enter your details here", font=('Times New Roman', 13))

    lName = Label(register, text="Enter your name :", font=('Times New Roman', 16))
    lEmail = Label(register, text="Enter your email :", font=('Times New Roman', 16))   
    lAge = Label(register, text="Enter your age :", font=('Times New Roman', 16))
    lAddress = Label(register, text="Enter your address :", font=('Times New Roman', 16))
    lGender = Label(register, text="Gender:", font=('Times New Roman', 16))
    
    eName = Entry(register, text="")
    eEmail = Entry(register, text="")
    eAddress = Entry(register, text="", width=50)
    eAge = Entry(register, text="")
    gender=""

    lRegTitle.grid(sticky='w', padx = '50',pady='10')
    lRegSubTitle.grid(sticky='w', padx = '50',pady='10')
    lName.grid(sticky='w', padx = '30',pady='10')
    eName.grid(sticky='w', padx = '30',pady='10')
    lEmail.grid(sticky='w', padx = '30',pady='10')
    eEmail.grid(sticky='w', padx = '30',pady='10')
    lAge.grid(sticky='w', padx = '30',pady='10')
    eAge.grid(sticky='w', padx = '30',pady='10')
    lAddress.grid(sticky='w', padx = '30',pady='5')
    eAddress.grid(sticky='w', padx = '30',pady='15')
    lGender.grid(sticky='w', padx = '30',pady='30')

    s = IntVar()
    rbMale = Radiobutton(register, text="Male", font=('Times New Roman', 16), variable=s, value=1)
    rbFemale = Radiobutton(register, text="Female", font=('Times New Roman', 16), variable=s, value=2)
    rbOther = Radiobutton(register, text="Other", font=('Times New Roman', 16), variable=s, value=3)
    
    rbMale.grid(sticky='w', padx = '30',pady=7)
    rbFemale.grid(sticky='w', padx = '30',pady=7)
    rbOther.grid(sticky='w', padx = '30',pady=7)
    def Reg():
        nonlocal gender 
        if s.get()==1:
            gender+="Male"
        elif s.get()==2:
            gender+="Female"
        elif s.get()==3:
            gender+="Other"
        register.withdraw()
        start.deiconify()
    btnRegister = Button(register, text="Register",font=('Times New Roman', 16, 'bold'), command = Reg)
    btnRegister.grid()
    register.mainloop()

#Start Page
start = Tk()
start.geometry('700x700+450+25')
start.title("Expenso !")
register()
start.mainloop()