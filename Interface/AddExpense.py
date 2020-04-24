from tkinter import *
def launch(username):
    AddExpense = Tk()
    AddExpense.geometry("900x500+100+25")
    AddExpense.title("Expenso :  Add Expense ")
    AddExpense.maxsize(900, 600) # specify the max size the window can expand to
    AddExpense.config(bg="skyblue") # specify background color

        
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
    Back = Button(right_frame, text="Back")
    Back.grid(row=6, column=0, padx=10, pady=10)

    # Container 1
    #------------------------------------------------------#
    Expense_summary =  Label(container1, text = "Your Expense Summary") 
    Expense_summary.grid(row = 0, column = 6, columnspan = 4, pady =10,padx=10)
    current_expense = Label(container1, text ="Current Expenses: ")
    current_expense.grid(row =2, column = 6, padx =5, pady=10)
    total_budget = Label(container1,text="Total Budget: ")
    total_budget.grid(row =3, column = 6, padx =5, pady=10)
    rem_budget = Label(container1, text = "Remaining Budget: ")
    rem_budget.grid(row=4, column =6, padx=5, pady=10)
    # btn_add_income = Button(container1, text="Edit/Add")
    # btn_add_income.grid(row = 6, column = 6, columnspan = 4)
    ecurr_expense = Entry(container1, text="",width=25)
    ecurr_expense.grid(row = 2, column =8, padx=5, pady=10)
    e_totalbudget = Entry(container1, text="",width=25)
    e_totalbudget.grid(row = 3, column =8, padx =5, pady=10)
    e_rembudget = Entry(container1, text="",width=25)
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
    Type = Label(container2, text="Type")
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
    btn_add_income = Button(container2, text="Add Expense")
    btn_add_income.grid(row = 7, column = 5, columnspan = 4, padx = 5, pady = 15)


    #-------------------------------------------------------#

    AddExpense.mainloop()