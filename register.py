# user Registration Signin And Signup

from customer import *
from bank import Bank
import random

def signup():
    username = input("Create username: ")
    temp = db_query(f"SELECT username from customers where username = '{username}';")
    if temp:
        print("username is already exist")
        signup()
    else:
        print('Username is available please proceed')
        password = input("Enter your password: ")
        name = input("Enter you name: ")
        age = int(input("Enter you age: "))
        city = input("Enter your city: ")
        while True:
            account_number = random.randint(10000000,99999999)
            temp = db_query(f"SELECT account_number FROM customers where account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number: ",account_number)
                break
    cust_obj = customer(username, password, name, age, city, account_number)
    cust_obj.createuser()
    bank_obj = Bank(username,account_number)
    bank_obj.Create_transaction_table()
    
def Signin():
    username = input("Enter username: ")
    temp = db_query(f"SELECT username from customers where username='{username}';")
    
    if temp:
        while True:
            password = input("Enter your password: ")
            temp = db_query(f"SELECT password from customers where username = '{username}';")
            if temp[0][0] == password:
                print("Sign in Succesfully\n")
                return username
            else:
                print("Wrong password try again")
                continue
                
    else:
        print("Enter correct username")
        Signin()