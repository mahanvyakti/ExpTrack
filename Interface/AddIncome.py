from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk
from tkinter import Canvas
# from profile import launchProfile
# Add bar on the left for 
# buttons for analaysis, profile, add income, add expense
def launch(username):    
    AddIncome = Tk()
    AddIncome.geometry("900x500+100+25")
    AddIncome.title("Expenso :  Add Income ")
    AddIncome.maxsize(900, 600) # specify the max size the window can expand to
    AddIncome.config(bg="skyblue") # specify background color

    def back():
        AddIncome.withdraw()

    def get_income(eamount, edate, esource):
        eamount.delete(0,'end')
        edate.delete(0,'end')
        esource.delete(0,'end')
        query = "SELECT amount,date,source  FROM income WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            rows = cur.fetchall()

            for row in rows:
                eamount.insert(0, row[0])
                edate.insert(0, row[1])
                # if row[2]=="" or row[2]=="Null" or row[2]==None:
                esource.insert(0, row[2])
                # else:
                #     esource.insert(0, row[2])
                
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    def get_budget(eSaving,eBudget,edate1):
        # eSaving.delete(0,'end')
        # eBudget.delete(0,'end')
        # edate1.delete(0,'end')
        query = "SELECT savings,budget,date FROM budget WHERE username1 = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            rows = cur.fetchall()

            for row in rows:
                eSaving.insert(0, row[0])
                eBudget.insert(0, row[1])
                if row[2] != None:
                    edate1.insert(0, row[2])
                else:
                    edate1.insert(0, "Null")

        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    

    def add_income(eamount, edate, esource):
        amount = eamount.get()
        date = edate.get()
        source = esource.get()
        query = "UPDATE  income SET amount = %s,date = %s,source = %s WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (amount,date,source,username,)
            cur.execute(query,params)
            cur.execute("commit")

            eamount.delete(0,'end')
            edate.delete(0,'end')
            esource.delete(0,'end')
            
            MessageBox.showinfo("Success","Inserted Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        else:
            cur.close()
            con.close()

    def add_budget(eSaving, eBudget, edate):
        savings = eSaving.get()
        budget = eBudget.get()
        date1 = edate.get()
        query = "UPDATE  budget SET savings = %s,budget =%s,date = %s WHERE username1 = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (savings,budget,date1,username,)
            cur.execute(query,params)
            cur.execute("commit")

            eSaving.delete(0,'end')
            eBudget.delete(0,'end')
            edate.delete(0,'end')
            
            MessageBox.showinfo("Success","Inserted Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        else:
            cur.close()
            con.close()

    # Create left and right frames
    left_frame = Frame(AddIncome, width=50, height=600, bg='grey')
    left_frame.grid(row=0, column=0)

    right_frame = Frame(AddIncome,  width = 800, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=2, padx=10, pady=40)

    container1 = Frame(right_frame,  width = 400, height=100, bg='grey')
    container1.grid(row=2, column=2, padx=40, pady=25)
    container2 = Frame(right_frame, width = 400, height=100, bg ='grey')
    container2.grid(row=2, column=3, padx=40, pady=25)

    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0)

    Back = Button(right_frame, text="Back", command=back)
    Back.grid(row=6, column=0, padx=10, pady=10)

    # Container 1
    #------------------------------------------------------#
    Add_income =  Label(container1, text = "Add your Monthly income") 
    Add_income.grid(row = 0, column = 6, columnspan = 4, pady =10,padx=10)
    amount = Label(container1, text ="Amount")
    amount.grid(row =2, column = 6, padx =5, pady=10)
    date = Label(container1,text="Date")
    date.grid(row =3, column = 6, padx =5, pady=10)
    source = Label(container1, text = "Source")
    source.grid(row=4, column =6, padx=5, pady=10)
    
    
    eamount = Entry(container1, text="",width=25)
    edate = Entry(container1, text="",width=25)
    esource = Entry(container1, text="",width=25)
    btn_add_income = Button(container1, text="Edit/Add", command =lambda: add_income(eamount, edate, esource))
    
    btn_add_income.grid(row = 6, column = 6, columnspan = 4)
    eamount.grid(row = 2, column =8, padx=5, pady=10)
    edate.grid(row = 3, column =8, padx =5, pady=10)
    esource.grid(row =4, column = 8, padx=5, pady=10)
    #-------------------------------------------------------#

    # Container 2
    #-------------------------------------------------------#
    Add_savings =  Label(container2, text = "Add Monthly Savings and Budget")
    Add_savings.grid(row = 0, column = 6, columnspan = 4, pady =10)

    
    eSaving = Entry(container2, text="", width=25)
    eBudget = Entry(container2, text="", width=25)
    
    savings = Label(container2, text="Savings")
    budget = Label(container2, text="Budget")
    date1 = Label(container2, text="Date")
    edate1 = Entry(container2, text="", width = 25)
    btn_add_income = Button(container2, text="Edit/Add", command =lambda: add_budget(eSaving, eBudget, edate))

    btn_add_income.grid(row = 6, column = 6, columnspan = 4)
    eSaving.grid(row = 2, column =8, padx=5, pady=10)
    savings.grid(row =2, column = 6, padx =5, pady=10)
    eBudget.grid(row = 3, column =8, padx =5, pady=10)
    budget.grid(row =3, column = 6, padx =5, pady=10)
    date1.grid(row=4, column=6, padx=5, pady=10)
    edate1.grid(row=4, column=8, padx=5, pady=10)   
    #-------------------------------------------------------#

    get_income(eamount, edate, esource)
    get_budget(eSaving,eBudget,edate1)
    AddIncome.mainloop()

# launch("dodo")