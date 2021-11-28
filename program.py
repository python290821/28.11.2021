import sqlite3
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess

dao = CustomerDataAccess('mydb.db')
dao.print_all_customers();