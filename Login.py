from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import Home, Register


def launch():
    Login = Tk()
    Login.geometry("900x500+100+25")
    Login.title("Expenso :  Login ")
    Login.maxsize(900, 600) # specify the max size the window can expand to
    Login.config(bg="skyblue") # specify background color

    def RedirecttoHome(username):
        Login.withdraw()
        Home.launch(username)


    def RedirecttoRegister():
        Login.withdraw()
        Register.launch()


    def login(getuser, getpass):
        user_name  = getuser.get()
        passw = getpass.get()
        
        query = "SELECT username,password FROM user"
        try:
            con = mysql.connect(host="localhost",user="root",password="",database="exptrack")
            cur = con.cursor()
            cur.execute(query)
            rows = cur.fetchall()
            success=False
            #length = len(rows
            for user in rows:
                if user[0]==user_name and user[1] == passw:
                    RedirecttoHome(user_name)
                    success=True
                    break
            
            if not success:
                getuser.delete(0,'end')
                getpass.delete(0,'end')
                MessageBox.showerror("Error!","Incorrect Username or Password, please check")

        
        except mysql.Error as err:
                print(err)
                MessageBox.showerror("Error","Something went wrong!")
        else:
            cur.close()
            con.close()   
    
    
    frame = Frame(Login,  width = 800, height=425, bg='lightgrey')
    frame.grid(row=0, column=4, padx=300, pady=100)

    Display = Label(frame, text = "Login to Expenso!")
    Display.grid(row=0, column = 4, padx=20, pady=20, columnspan=6)
    Username = Label(frame, text ="Username")
    Username.grid(row=2, column = 4, padx=20, pady=20, columnspan=3)
    Password = Label(frame,text="Password")
    Password.grid(row=4, column = 4, padx=20, pady=20, columnspan=3)
    getuser = Entry(frame, text="")
    getuser.grid(row=2, column=7, padx=20, pady=20)
    getpass = Entry(frame, show="*")
    getpass.grid(row=4, column=7, padx=20, pady=20)


    
    btnlogin = Button(frame, text="Login", command=lambda: login(getuser, getpass))
    btnlogin.grid(row=6, column = 4, padx=20, pady=20, columnspan=6)

    btnRegister = Button(frame, text = "Register", command=lambda: RedirecttoRegister())
    btnRegister.grid(row=12, column=12, padx=10,pady=10)
    RegLabel = Label(frame, text="New to Expenso?")
    RegLabel.grid(row=12, column =10, padx=10, pady=10)
    
    Login.mainloop()

launch()