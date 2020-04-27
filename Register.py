from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import Home
from datetime import *

def launch():
    register = Tk()
    register.geometry('400x700+550+25')
    register.title("Expenso : Register ")
    lRegTitle = Label(register, text="Welcome to Expenso !", font=('Times New Roman', 16),bg="orange red")
    lRegTitle.grid()
    register.grid_rowconfigure(1, weight=0)
    #register.grid_columnconfigure(1, weight=1)
    lRegSubTitle = Label(register, text="Please enter your details here", font=('Times New Roman', 5))
    #start.withdraw()
    
    

    lName = Label(register, text="Enter your name :", font=('Times New Roman', 16))
    lEmail = Label(register, text="Enter your email :", font=('Times New Roman', 16))   
    lAge = Label(register, text="Enter your age :", font=('Times New Roman', 16))
    lAddress = Label(register, text="Enter your address :", font=('Times New Roman', 16))
    lGender = Label(register, text="Gender:", font=('Times New Roman', 16))
    lUsername = Label(register, text="Enter Username:", font=('Times New Roman', 16))
    lPassword = Label(register, text="Enter Password:", font=('Times New Roman', 16))
    

    eName = Entry(register, text="")
    eEmail = Entry(register, text="",width=50)
    eAddress = Entry(register, text="", width=50)
    eAge = Entry(register, text="",width=5)
    eUsername = Entry(register, text="",width=5)
    ePassword = Entry(register, show="*",width=5)
    gender = ""

    eName = Entry(register, text="",width=25)
    eEmail = Entry(register, text="",width=50)
    eAddress = Entry(register, text="", width=50)
    eAge = Entry(register, text="",width=5)
    eUsername = Entry(register, text="",width=25)
    ePassword = Entry(register, text="",width=25)
    


    lRegTitle.grid(padx = '50',pady='5')
    lRegSubTitle.grid( padx = '20',pady='2')

    lUsername.grid( padx = '30',pady='5')
    eUsername.grid( padx = '30',pady='5')
    lPassword.grid( padx = '30',pady='5')
    ePassword.grid( padx = '30',pady='5')
    
    lName.grid( padx = '30',pady='5')
    eName.grid( padx = '30',pady='5')
    lEmail.grid( padx = '30',pady='5')
    eEmail.grid( padx = '30',pady='5')
    lAge.grid( padx = '30',pady='5')
    eAge.grid( padx = '30',pady='5')
    lAddress.grid( padx = '30',pady='5')
    eAddress.grid( padx = '30',pady='5')
    lGender.grid( padx = '30',pady='5')

    OPTIONS = [
    "Male",
    "Female",
    "Other"
    ] #etc
    variable = StringVar(register)
    variable.set("") # default value
    w = OptionMenu(register, variable, *OPTIONS)
    w.grid(padx = '25',pady=5)
    
    




    """
    s = IntVar()
    rbMale = Radiobutton(register, text="Male", font=('Times New Roman', 16), variable=s, value=1)
    rbFemale = Radiobutton(register, text="Female", font=('Times New Roman', 16), variable=s, value=2)
    rbOther = Radiobutton(register, text="Other", font=('Times New Roman', 16), variable=s, value=3)

    
    rbFemale.grid(padx = '25',pady=5)
    rbOther.grid(padx = '25',pady=5)"""

    def validator(gender):
        
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
        
        MessageBox.showerror("Error", errorMessage)
        return valid
        
    def insert(gender):
        #nonlocal gender
        name = eName.get()
        email = eEmail.get()
        address = eAddress.get()
        age = eAge.get()
        username = eUsername.get()
        password = ePassword.get()
        gen = gender

        query = "INSERT INTO user (username,password,name,age,email,address,gender) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,password,name,age,email,address,gen,)
            cur.execute(query,params)
            cur.execute("commit")

            eName.delete(0,'end')
            eEmail.delete(0,'end')
            eAddress.delete(0,'end')
            eAge.delete(0,'end')
            eUsername.delete(0,'end')
            ePassword.delete(0,'end')
            
            MessageBox.showinfo("Success","Inserted Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        finally:
            cur.close()

        tday = datetime.today()
        firstDay = datetime(tday.year, tday.month, 1)

        query = "INSERT INTO income (amount,source,date,username) VALUES (%s, %s, %s, %s)"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (0,"Null",firstDay, username,)#YYYY-MM-DD HH:MI:SS
            cur.execute(query,params)
            cur.execute("commit")
        except mysql.Error as err:  
            print(err)
        else:
            cur.close()
            con.close()

        
        query = "INSERT INTO budget (savings,budget,date,username1) VALUES (%s, %s, %s, %s)"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (0,0,firstDay,username,)#YYYY-MM-DD HH:MI:SS
            cur.execute(query,params)
            cur.execute("commit")
        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()

        query = "INSERT INTO expense (category,mode,amount,date,username) VALUES (%s, %s, %s, %s, %s)"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = ("Null","Null",0,firstDay,username)#YYYY-MM-DD HH:MI:SS
            cur.execute(query,params)
            cur.execute("commit")
            
        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()

    def Reg():
        gender = variable.get()
        valid = validator(gender)
        if valid:
            insert(gender)
            register.withdraw()
            username = eUsername.get()
            Home.launch(username)  

    btnRegister = Button(register, text="Register",font=('Times New Roman', 16, 'bold'), command = Reg)
    btnRegister.grid()
    #btnBack = Button(register, text="Back",font=('Times New Roman', 16, 'bold'),command = back)
    #btnBack.grid()
    register.mainloop()

    return register

#launch()
