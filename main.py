
from register import *
from bank import *

status = False
print("Welcome To Happy Customer Banking System")

while True:
    try:
        register = int(input("1. SignUp\n"
                            "2. SignIn\n"
                            "Enter your choice: "))
        if register == 1 or register == 2:
            if register == 1:
                signup()
            if register == 2:
                user = Signin()
                status = True
                break
                
        else:
            print("Please Enter Valid Input From Option")
            
    except ValueError:
        print("Invalid Input Try Again with 1 or 2 option")
        
        
account_number = db_query(f"SELECT  account_number from customers where username = '{user}';")
print(account_number[0][0])

while status:
    print(f"Welcome {user} Choose your Banking Service\n")
    try:
        facility = int(input("1. Balance Enquiry\n"
                            "2. Cash Deposit\n"
                            "3. Cash Withdraw\n"
                            "4. Fund Transfer\n"
                            "5. Exit\n"
                            "Enter your choice: "))
        if facility >=1 and facility <=5:
            if facility == 1:
                bobj = Bank(user,account_number[0][0])
                bobj.balance_enquiry()
                
            elif facility == 2:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit: "))
                        bobj = Bank(user,account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                    
            elif facility == 3:
                while True:
                    try:
                        amount_withdraw = int(input("Enter Amount to Withdraw: "))
                        bobj = Bank(user,account_number[0][0])
                        bobj.withdraw(amount_withdraw)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
                    
            elif facility == 4:
                while True:
                    try:
                        receiver = int(input("Enter Reciver Account Number: "))
                        if receiver == account_number[0][0]:
                            print("please enter correct account number")
                            continue
                        else:
                            amount = int(input("Enter Amount which you want to Transfer"))
                            bobj = Bank(user,account_number[0][0])
                            bobj.fundtransfer(receiver,amount)
                            mydb.commit()
                            break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
            
            elif facility == 5:
                print("Thanks For Using Our Services")
                status = False
        else:
            print("Please Enter Valid Input From Option")
            continue
            
    except ValueError:
        print("Invalid Input Try Again with 1 or 2 option")
        continue