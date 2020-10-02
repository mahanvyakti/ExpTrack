from tkinter import messagebox
from Interface import profile, AddIncome, AddExpense, ExpvsTime
import Login
import db_functions
import mysql.connector as mysql
from dotenv import load_dotenv
import os
#Start Page

load_dotenv()

connection = mysql.connect(
    host= os.getenv('MYSQL_HOST', default='localhost'),
    user= os.getenv('MYSQL_USER', default='root'),
    password= os.getenv('MYSQL_PASSWORD', default=''),
    database= os.getenv('MYSQL_DATABASE', default='exptrack')
)

is_db_initialised = db_functions.check_if_db_initialised(connection)
if not is_db_initialised:
    queries = db_functions.get_initial_queries()
    status = db_functions.execute_queries(queries)
    if status:
        print('DB INITIALISED SUCCESSFULLY')
    else:
        print('ERROR INITIALISING DB')
register = Login.launch()

