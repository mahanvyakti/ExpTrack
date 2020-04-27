from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk
from tkinter import Canvas
# from AddIncome import openAddIncome
# Add bar on the left for 
# buttons for analaysis, profile, add income, add expense
def launch(username):
    profile = Tk()
    profile.geometry("910x630+200+50")
    profile.title("Expenso :  Your Profile ")
    profile.maxsize(900, 700) # specify the max size the window can expand to
    profile.config(bg="skyblue") # specify background color

    def back():
        profile.withdraw()

    
    def get_profile():
        eName.delete(0,'end')
        eAddress.delete(0,'end')
        eUsername.config(text="")
        eAge.delete(0,'end')
        eEmail.delete(0,'end')
        eGender.delete(0,'end')
        ePassword.delete(0,'end')
        
        query = "SELECT username,password,name,age,email,address,gender FROM user WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            rows = cur.fetchall()
            print(rows)
            
            for row in rows:
                print("For loop 1")
                eUsername.config(text=username)
                eName.insert(0, row[2])
                eAddress.insert(0, row[5])
                eAge.insert(0, row[3])
                eEmail.insert(0, row[4])
                eGender.insert(0, row[6])
                ePassword.insert(0, row[1])

            

        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        else:
            cur.close()
    
    
    # Create left and right frames
    left_frame = Frame(profile, width=50, height=600, bg='skyblue')
    left_frame.grid(row=0, column=0)

    right_frame = Frame(profile,  width = 800, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=1, padx=10, pady=50)

    container = Frame(right_frame,  width = 400, height=600, bg='grey')
    container.grid(row=10, column=2, padx=200, pady=50)
    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0,pady=50)

    btnBack = Button(toolbar, text="Back", command=back)
    btnBack.grid(row=1, column=0, padx=15, pady=10)

    # bProfile = Button(toolbar, text="Profile" ,command = get_profile)
    # bProfile.grid(row=0, column=0, padx=30, pady=5)

    # bAnalysis = Button(toolbar, text="Analysis")
    # bAnalysis.grid(row=1, column=0, padx=30,pady=5)

    # bAddIncome = Button(toolbar, text="Add Income", command=open_AddIncome)
    # bAddIncome.grid(row=2, column=0, padx=30,pady=5)

    # bAddExpense = Button(toolbar, text="Add Expense")
    # bAddExpense.grid(row=3, column=0, padx=30,pady=5)

    lusername =  Label(container, text = "Username: ", font=('Times New Roman', 12)) 
    name = Label(container, text = "Name: ", font=('Times New Roman', 12)) 
    address = Label(container, text = "Address: ",font=('Times New Roman', 12))
    age =  Label(container, text = "Age: ", font=('Times New Roman', 12)) 
    email = Label(container, text = "Email: ", font=('Times New Roman', 12))
    gender = Label(container, text = "Gender: ", font=('Times New Roman', 12))
    password = Label(container, text = "Password: ", font=('Times New Roman', 12))

    eUsername = Label(container, text="",width=21, font=('Times New Roman',10))
    eName = Entry(container, text="",width=25)
    eAddress = Entry(container, text="", width=25)
    eAge = Entry(container, text="",width=25)
    eEmail = Entry(container, text="",width=25)
    eGender = Entry(container, text="",width=25)
    ePassword = Entry(container, text="",width=25)

    eUsername.grid( row=9 , column=10, pady=5)
    eName.grid(row=10, column=10, pady=5)
    eAddress.grid(row=11, column=10, pady=5)
    eAge.grid(row=12, column=10, pady=5)
    eEmail.grid(row=13, column=10, pady=5)
    eGender.grid(row=14, column=10, pady=5)
    ePassword.grid(row=15, column=10, pady=5)

    lusername.grid(row= 9 , column = 8,padx=10, pady=20)
    name.grid(row= 10 , column = 8, padx=10, pady=10)
    address.grid(row= 11 , column = 8, padx=10, pady=10)
    age.grid(row= 12 , column = 8, padx=10, pady=10)
    email.grid(row= 13 , column = 8,padx=10, pady=10)
    gender.grid(row= 14 , column = 8,padx=10, pady=10)
    password.grid(row= 15 , column = 8,padx=10, pady=10)



    def update_profile():
        name = eName.get()
        email = eEmail.get()
        address = eAddress.get()
        age = eAge.get()
        password = ePassword.get()
        gen = eGender.get()
        query = "UPDATE user SET  password = %s,name = %s,age = %s,email = %s,address = %s  WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (password,name,str(age),email,address,username,)
            cur.execute(query,params)
            cur.execute("commit")
            
            eName.delete(0,'end')
            eEmail.delete(0,'end')
            eAddress.delete(0,'end')
            eAge.delete(0,'end')
            ePassword.delete(0,'end')
            
            MessageBox.showinfo("Success","Updated Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not update !")
        finally:
            cur.close()      

    btnUpdate = Button(container, text="Update Profile",font=('Times New Roman', 16, 'bold'), command = update_profile)
    btnUpdate.grid(row=100, column=10,padx = 50, pady = 30)
    get_profile()
    profile.mainloop()
    

# launch("momo")