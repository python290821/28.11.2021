import sqlite3
from Customer import Customer

# DAO - Data Access Object
class CustomerDataAccess:

    def __init__(self, file_path):
        self.cursor = sqlite3.connect(file_path).cursor()

    def print_all_customers(self):
        # con = sqlite3.connect('mydb2.db')  # change this
        # cur = con.cursor()
        self.cursor.execute("select * from COMPANY")
        for row in self.cur:
            print(row)

    def insert_customer(self, customer):
        self.cursor.execute(f'INSERT INTO shopping VALUES ({customer.id}, ' +
                    f' "{customer.fname}", "{customer.lname}",' +
                    f' "{customer.mobile}")')

    def get_customer_by_id(self, id):
        self.cursor.execute("select * from customers where "+
                         f" id = {id}")
        customer = None
        for row in self.cur:
            customer = Customer(row[0], row[1], row[2], row[3])

        return customer