# Bank transfer
from database import *
import datetime

class Bank:
    def __init__(self,username,account_number):
        self.__username = username
        self.__account_number = account_number
        
    def Create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction"
                f"(timedate VARCHAR(30),"
                f"account_number INTEGER,"
                f"remark VARCHAR(30),"
                f"amount INTEGER)")
        
    def balance_enquiry(self):
        temp = db_query(f"SELECT balance from customers where username='{self.__username}';")
        print(f"{self.__username} Your Balance is {temp[0][0]}")
        
    def deposit(self,amount):
        temp = db_query(f"SELECT balance from customers where username='{self.__username}';")
        test = temp[0][0] + amount
        db_query(f"update customers SET balance = {test} where username = '{self.__username}';")
        self.balance_enquiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                f"'{datetime.datetime.now()}',"
                f"'{self.__account_number}',"
                f"'Amount Deposit',"
                f"'{amount}'"
                f")")
        print(f"{self.__username} Amount is Succcesfully Deposited in your Account {self.__account_number}")
        
    def withdraw(self,amount):
        temp = db_query(f"SELECT balance from customers where username='{self.__username}';")
        if temp[0][0]>=amount:
            test = temp[0][0] -amount
            db_query(f"UPDATE customers SET balance = {test} where username = '{self.__username}';")
            self.balance_enquiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'Amount Withdraw',"
                    f"'{amount}'"
                    f")")
            print(f"{self.__username} Amount is Succcesfully Withdraw From your Account {self.__account_number}")
        else:
            print(f"Insufficient Balance in you Account {temp[0][0]}")
       
        
    def fundtransfer(self,recevier,amount):

        temp = db_query(f"SELECT balance from customers where username='{self.__username}';")
        if temp[0][0] >= amount:
            temp2 = db_query(f"SELECT balance from customers where account_number = '{recevier}';")
            test = temp[0][0] - amount
            test2 = temp2[0][0] + amount
            db_query(f"UPDATE customers SET balance = {test2} where account_number = '{recevier}';")
            db_query(f"UPDATE customers SET balance = {test} where username = '{self.__username}';")
            recevier_username = db_query(f"SELECT username FROM customers where account_number = '{recevier}';")
            self.balance_enquiry()
            db_query(f"INSERT INTO {recevier_username[0][0]}_transaction VALUES ("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'Fund Transfer From-> {self.__account_number}',"
                    f"'{amount}'"
                    f")")
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'Fund Transfer-> {recevier}',"
                    f"'{amount}'"
                    f")")
            print(f"{self.__username} Amount is Succcesfully Transfer From Your Account")
        else:
            print("Insufficient Balance in your Account")