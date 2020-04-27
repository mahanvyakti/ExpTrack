from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter.ttk
from tkinter import Canvas
from datetime import *

# from profile import launchProfile
# Add bar on the left for 
# buttons for analaysis, profile, add income, add expense
def launch(username):    
    AddIncome = Tk()
    AddIncome.geometry("900x500+200+50")
    AddIncome.title("Expenso :  Add Income ")
    AddIncome.maxsize(900, 600) # specify the max size the window can expand to
    AddIncome.config(bg="skyblue") # specify background color
    

    def back():
        AddIncome.withdraw()

    def get_income(eamount, edate, esource):
        eamount.delete(0,'end')
        edate.delete(0,'end')
        esource.delete(0,'end')

        tday = datetime.today()
        firstDay = datetime(tday.year, tday.month, 1)
        Today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        firstDay = str(firstDay)
        Today = str(Today)

        
        query = "SELECT  amount,date,source  FROM income WHERE username = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        
        #query = "SELECT amount,date,source  FROM income WHERE username = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Today,)
            cur.execute(query,params)
            rows = cur.fetchall()
            print(rows)
            eamount.insert(0, rows[-1][0])
            edate.insert(0, rows[-1][1])
            # if row[2]=="" or row[2]=="Null" or row[2]==None:
            esource.insert(0, rows[-1][2])
            # else:
            #     esource.insert(0, row[2])
                
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

    def get_budget(eSaving,eBudget,edate1):
        #eSaving.delete(0,'end')
        #eBudget.delete(0,'end')
        #edate1.delete(0,'end')
        

        tday = datetime.today()
        firstDay = datetime(tday.year, tday.month, 1)
        Today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        firstDay = str(firstDay)
        Today = str(Today)

        
        query = "SELECT savings,budget,date FROM budget WHERE username1 = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Today,)
            cur.execute(query,params)
            rows = cur.fetchall()

            print("Get budget rows:\n", rows)    
            eSaving.insert(0, rows[-1][0])
            eBudget.insert(0, rows[-1][1])
            if rows[-1][2] != None:
                edate1.insert(0, rows[-1][2])
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

        
        query = "UPDATE income SET amount=%s, date=%s, source=%s WHERE username=%s"
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
    
    def check_income(eamount, edate, esource):
        amount = eamount.get()
        Date = edate.get()
        source = esource.get()

        Date= datetime.strptime(Date, '%Y-%m-%d %H:%M:%S')
        firstDay = datetime(Date.year, Date.month, 1)
        firstDay = str(firstDay)
        Date = str(Date)

        firstEntry = False

        query = "SELECT amount FROM income  WHERE username = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Date,)
            cur.execute(query,params)
            rows = cur.fetchall()
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()


        if  int(amount)< 0:
            MessageBox.showerror("Error !", "Income cannot be negative !")
            eamount.delete(0,'end')
            return

        if rows[0][0] == 0:
            firstEntry = True
        
        if firstEntry:
            add_income(eamount, edate, esource)



    def add_budget(eSaving, eBudget, edate1):
        savings = eSaving.get()
        budget = eBudget.get()
        date1 = edate1.get()


        query = "UPDATE budget SET savings = %s,budget = %s,date = %s WHERE username1 = %s"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (savings,budget,date1,username,)
            cur.execute(query,params)
            cur.execute("commit")

            eSaving.delete(0,'end')
            eBudget.delete(0,'end')
            edate1.delete(0,'end')
            
            MessageBox.showinfo("Success","Inserted Successfully")
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Could not insert !")
        else:
            cur.close()
            con.close()
    
    def check_budget(eSavings, eBudget, edate1):
        savings = eSaving.get()
        budget = eBudget.get()
        Date1 = edate1.get()

        Date= datetime.strptime(Date1, '%Y-%m-%d %H:%M:%S')
        firstDay = datetime(Date.year, Date.month, 1)
        firstDay = str(firstDay)
        Date = str(Date)

        monthlyIncome = 0
        firstEntry = False
        
        query = "SELECT  amount FROM income WHERE username = %s AND (date BETWEEN CAST(%s AS DATETIME) AND CAST(%s AS DATETIME))"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            params = (username,firstDay, Date,)
            cur.execute(query,params)
            rows = cur.fetchall()
            
            for income in rows:
                if income[0]==0:
                    firstEntry = True
                monthlyIncome += income[0]
                
        except mysql.Error as err:
            print(err)
            MessageBox.showerror("Error","Something went wrong !")
        else:
            cur.close()
            con.close()

        if  int(savings)< 0:
            MessageBox.showerror("Error !", "Savings cannot be negative !")
            eSaving.delete(0,'end')
            
            return
        if  int(budget) < 0:
            MessageBox.showerror("Error !", "Budget cannot be negative !")   
            eBudget.delete(0,'end')
            return
        
        if monthlyIncome < int(savings): 
            MessageBox.showerror("Error !", "Savings must be less than monthly income !")
            eSavings.delete(0,'end')
        

        if monthlyIncome < int(budget): 
            MessageBox.showerror("Error !", "Budget must be less than monthly income !")
            eBudget.delete(0,'end')
            
            return
        if monthlyIncome < int(savings) + int(budget):  
            MessageBox.showerror("Error !","Sum of budget and savings must be less than monthly income !" )
            eSaving.delete(0,'end')
            eBudget.delete(0,'end')
            return

        if rows[0][0] == 0:
            firstEntry = True
        
        if firstEntry:
            add_budget(eSavings, eBudget, edate1)




    # Create left and right frames
    left_frame = Frame(AddIncome, width=50, height=600, bg='skyblue')
    left_frame.grid(row=0, column=0, padx=10)

    right_frame = Frame(AddIncome,  width = 800, height=600, bg='lightgrey')
    right_frame.grid(row=0, column=2, padx=60, pady=110)

    container1 = Frame(right_frame,  width = 400, height=100, bg='grey')
    container1.grid(row=2, column=2, padx=40, pady=25)
    container2 = Frame(right_frame, width = 400, height=100, bg ='grey')
    container2.grid(row=2, column=3, padx=40, pady=25)

    toolbar = Frame(left_frame, width=50, height=600, bg='skyblue')
    toolbar.grid(row=0, column=0, padx=10)

    Back = Button(toolbar, text="Back", command=back, font=('Times New Roman', 10))
    Back.grid(row=0, column=0, padx=10, pady=10)

    # Container 1
    #------------------------------------------------------#
    Add_income =  Label(container1, text = "Add your Monthly income") 
    Add_income.grid(row = 0, column = 6, columnspan = 4, pady =10,padx=10)
    amount = Label(container1, text ="Amount",font=('Times New Roman', 10))
    amount.grid(row =2, column = 6, padx =5, pady=10)
    date = Label(container1,text="Date",font=('Times New Roman', 10))
    date.grid(row =3, column = 6, padx =5, pady=10)
    source = Label(container1, text = "Source",font=('Times New Roman', 10))
    source.grid(row=4, column =6, padx=5, pady=10)
    
    
    eamount = Entry(container1, text="",width=25)
    edate = Entry(container1, text="",width=25)
    esource = Entry(container1, text="",width=25)
    btn_add_income = Button(container1, text="Add", command =lambda: check_income(eamount, edate, esource))
    
    btn_add_income.grid(row = 6, column = 6, columnspan = 4, pady=10)
    eamount.grid(row = 2, column =8, padx=5, pady=10)
    edate.grid(row = 3, column =8, padx =5, pady=10)
    esource.grid(row =4, column = 8, padx=5, pady=10)
    #-------------------------------------------------------#

    # Container 2
    #-------------------------------------------------------#
    Add_savings =  Label(container2, text = "Add Monthly Savings and Budget",font=('Times New Roman', 10))
    Add_savings.grid(row = 0, column = 6, columnspan = 4, pady =10)

    
    eSaving = Entry(container2, text="", width=25)
    eBudget = Entry(container2, text="", width=25)
    
    savings = Label(container2, text="Savings",font=('Times New Roman', 10))
    budget = Label(container2, text="Budget",font=('Times New Roman', 10))
    date1 = Label(container2, text="Date",font=('Times New Roman', 10))
    edate1 = Entry(container2, text="", width = 25)
    btn_add_income = Button(container2, text="Add", command =lambda: check_budget(eSaving, eBudget, edate1))

    btn_add_income.grid(row = 6, column = 6, columnspan = 4, pady=10)
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

# launch("momo")