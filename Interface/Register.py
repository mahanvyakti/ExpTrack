from tkinter import *
from tkinter import messagebox

import cx_Oracle

def launch(start):
    register = Toplevel()
    register.geometry('400x750+550+25')
    register.title("Expenso : Register ")
    lRegTitle = Label(register, text="Welcome to Expenso !", font=('Times New Roman', 16),bg="orange red")
    lRegTitle.grid()
    register.grid_rowconfigure(1, weight=0)
    #register.grid_columnconfigure(1, weight=1)
    lRegSubTitle = Label(register, text="Please enter your details here", font=('Times New Roman', 13))
    #start.withdraw()

    lName = Label(register, text="Enter your name :", font=('Times New Roman', 16))
    lEmail = Label(register, text="Enter your email :", font=('Times New Roman', 16))   
    lAge = Label(register, text="Enter your age :", font=('Times New Roman', 16))
    lAddress = Label(register, text="Enter your address :", font=('Times New Roman', 16))
    lGender = Label(register, text="Gender:", font=('Times New Roman', 16))

    eName = Entry(register, text="")
    eEmail = Entry(register, text="",width=50)
    eAddress = Entry(register, text="", width=50)
    eAge = Entry(register, text="",width=5)
    gender = ""

    lRegTitle.grid(padx = '50',pady='10')
    lRegSubTitle.grid( padx = '50',pady='10')
    lName.grid( padx = '30',pady='10')
    eName.grid( padx = '30',pady='10')
    lEmail.grid( padx = '30',pady='10')
    eEmail.grid( padx = '30',pady='10')
    lAge.grid( padx = '30',pady='10')
    eAge.grid( padx = '30',pady='10')
    lAddress.grid( padx = '30',pady='5')
    eAddress.grid( padx = '30',pady='15')
    lGender.grid( padx = '30',pady='30')

    s = IntVar()

    rbMale = Radiobutton(register, text="Male", font=('Times New Roman', 16), variable=s, value=1)
    rbFemale = Radiobutton(register, text="Female", font=('Times New Roman', 16), variable=s, value=2)
    rbOther = Radiobutton(register, text="Other", font=('Times New Roman', 16), variable=s, value=3)

    rbMale.grid(padx = '30',pady=7)
    rbFemale.grid(padx = '30',pady=7)
    rbOther.grid(padx = '30',pady=7)

    def validator():
        """
        Validates data based on following requirements/conditions-
        name : 
            1. atleast two characters #
            2. only alphabets   #
        email : 
            1. non-empty #
            2. valid (must contain @ and .) #
        address :
            1. atleast 10 characters #
        age :
            1. non-negative #
            2. > 10 #
        gender :
            1. non-empty 
        """
        name, email, address, age, gen = eName.get(), eEmail.get(), eAddress.get(), eAge.get(), gender
        errorMessage = ""
        valid = False

        if len(name)<2:
            errorMessage+="\nName must contain atleast two characters !"
        elif not (name.replace(" ", "")).isalpha():
            errorMessage+="\nName must contain alphabets only !"

        
        if len(email) ==    0:
            errorMessage+="\nPlease enter your email address !"
        elif "@" not in email or "." not in email:
            errorMessage+="\nPlease enter valid email address !"
        
        if len(address)<10:
            errorMessage+= "\nPlease enter valid address !"
        
        if len(age) == 0:
            errorMessage+="\nPlease enter your age !"
        elif int(age) < 0:
            errorMessage+="\nAge cannot be negative !"
        elif int(age) < 10:
            errorMessage+="\nUser must atleast be 10 years old !"
        
        if gen == "":
            errorMessage+="\nPlease enter your gender !"
        
        if errorMessage == "":
            valid = True
            return valid
        
        messagebox.showerror("Error", errorMessage)
        return valid


    def Reg():
        nonlocal gender
        if s.get()==1:
            gender+="Male"
        elif s.get()==2:
            gender+="Female"
        elif s.get()==3:
            gender+="Other"
        
        valid = validator()
        if valid:
            register.withdraw()
            start.deiconify()
        """else:
            pass"""


    btnRegister = Button(register, text="Register",font=('Times New Roman', 16, 'bold'), command = Reg)
    btnRegister.grid()
    register.mainloop()
    return register

