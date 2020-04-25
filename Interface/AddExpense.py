from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk
from tkinter import Canvas
import datetime

def launch(username):
    AddExpense = Tk()
    AddExpense.geometry("900x500+100+25")
    AddExpense.title("Expenso :  Add Expense ")
    AddExpense.maxsize(900, 600) # specify the max size the window can expand to
    AddExpense.config(bg="skyblue") # specify background color

    def back():
        AddExpense.withdraw()

    def get_expense(ecurr_expense,e_totalbudget):
        tday = datetime.datetime.today()
        firstDay = datetime.datetime(tday.year, tday.month, 1)
        
        Today = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # query = "SELECT amount FROM expense WHERE username = %s  "
        query = "SELECT amount FROM expense WHERE username = %s AND date \
        BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME)"
        
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Today,)
            cur.execute(query,params)
            row1 = cur.fetchall()     
            print(row1)      #Empty !!!! 
            ecurr_expense.config(text=str(row1[0][0]))

        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()

        query = "SELECT budget FROM budget WHERE username1 = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            row2 = cur.fetchall()

            e_totalbudget.config(text=str(row2[0][0]))

            remaining = int(row2[0][0]) - int(row1[0][0])
            
            if remaining < 0:
                message = "Out of budget ! You have spent Rs.", str(-remaining)," than your budget !"
                e_rembudget.config(text=message)
            else:
                e_rembudget.config(text=str(remaining))
                
            #e_rembudget.config(text=str(remaining))

        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()


    def check_expense(eamount, category, variable, date):
        amount = eamount.get()
        category = etype.get()
        mode = variable.get()
        date = edate.get()

        query = "SELECT budget FROM budget WHERE username1 = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            row2 = cur.fetchall()

            totalbudget = row2[0][0]

        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()

        query = "SELECT amount FROM expense WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            row = cur.fetchall()

            total_expense = 0
            for value in row:
                total_expense += value[0]
                print(total_expense)

            if total_expense>totalbudget:
                MessageBox.showerror("Error", "Budget for the Month has been used up!")    
            else:
                add_expense(eamount, category, variable, date)

        except mysql.Error as err:
            print(err)
        else:
            cur.close()
            con.close()

    def add_expense(eamount, category, variable, date):
        amount = eamount.get()
        category = etype.get()
        mode = variable.get()
        date = edate.get()

        query = "SELECT amount FROM expense WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,)
            cur.execute(query,params)
            exp = cur.fetchall()

        except mysql.Error as err:
            print("Couldn't fetch expense", err)
        else:
            cur.close()
            con.close()
            
        new_amount = int(exp[0][0]) + int(amount)
        
        query = "UPDATE  expense SET amount = %s,category =%s,date = %s,mode = %s WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (new_amount,category,date,mode,username,)
            cur.execute(query,params)
            cur.execute("commit")
            
            eamount.delete(0,'end')
            etype.delete(0,'end')
            edate.delete(0,'end')
            
            MessageBox.showinfo("Success","Inserted Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        else:
            cur.close()
            con.close()


    # Create left and right frames
    left_frame = Frame(AddExpense, width=50, height=600, bg='grey')
    left_frame.grid(row=0, column=0)

    right_frame = Frame(AddExpense,  width = 800, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=2, padx=10, pady=20)

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
    Expense_summary =  Label(container1, text = "Your Expense Summary") 
    Expense_summary.grid(row = 0, column = 6, columnspan = 4, pady =10,padx=10)
    ecurr_expense = Label(container1, text ="Current Expenses: ")
    ecurr_expense.grid(row =2, column = 6, padx =5, pady=10)
    e_totalbudget = Label(container1,text="Total Budget: ")
    e_totalbudget.grid(row =3, column = 6, padx =5, pady=10)
    e_rembudget = Label(container1, text = "Remaining Budget: ")
    e_rembudget.grid(row=4, column =6, padx=5, pady=10)
    # btn_add_income = Button(container1, text="Edit/Add")
    # btn_add_income.grid(row = 6, column = 6, columnspan = 4)
    ecurr_expense = Label(container1,width=25)
    ecurr_expense.grid(row = 2, column =8, padx=5, pady=10)
    e_totalbudget = Label(container1,width=25)
    e_totalbudget.grid(row = 3, column =8, padx =5, pady=10)
    e_rembudget = Label(container1,width=25)
    e_rembudget.grid(row =4, column = 8, padx=5, pady=10)
    #-------------------------------------------------------#

    # Container 2
    #-------------------------------------------------------#
    Add_newexpense =  Label(container2, text = "Add New Expense")
    Add_newexpense.grid(row = 0, column = 6, columnspan = 4, pady =10)

    eamount = Entry(container2, text="", width=25)
    eamount.grid(row = 2, column =8, padx=5, pady=10)
    edate = Entry(container2, text="", width=25)
    edate.grid(row = 3, column =8, padx =5, pady=10)
    etype = Entry(container2, text="", width=25)
    etype.grid(row = 4, column =8, padx =5, pady=10)
    Amount = Label(container2, text="Amount: ")
    Amount.grid(row =2, column = 6, padx =5, pady=10)
    Date = Label(container2, text="Date")
    Date.grid(row =3, column = 6, padx =5, pady=10)
    Type = Label(container2, text="Category")
    Type.grid(row =4, column = 6, padx =5, pady=10)

    Mode = Label(container2, text="Mode of Expense")
    Mode.grid(row =5, column = 6, padx =5, pady=10)
    OPTIONS = [
    "Cash",
    "Card",
    "Cheque",
    "UPI"
    ] #etc
    variable = StringVar(container2)
    variable.set(OPTIONS[0]) # default value
    w = OptionMenu(container2, variable, *OPTIONS)
    w.grid(row=5, column =8, padx=6,pady=10)
    btn_add_expense = Button(container2, text="Add Expense", command=lambda: check_expense(eamount, etype, variable, edate))
    btn_add_expense.grid(row = 7, column = 5, columnspan = 4, padx = 5, pady = 15)

    get_expense(ecurr_expense,e_totalbudget)
    #-------------------------------------------------------#

    AddExpense.mainloop()

# launch("popo")