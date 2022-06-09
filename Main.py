import os

import Ticket
from Ticket import Create_Ticket

import Test
from Test import Helper_Func


def Welcome():  # Sign in options

    print("Welcome...")
    welcome = input("Do you have an account? y/n: ")
    if welcome == "n":
        while True:
            username = input("Enter a username :")
            print()
            password = input("Enter a password :")
            print()
            password1 = input("Confirm password :")
            if password == password1:
                file = open(username + ".txt", "w")
                file.write(username + ":" + password)
                file.close()
                welcome = "y"
                break
            print("Passwords do NOT match!")

    if welcome == "y":
        while True:
            login1 = input("Login: ")
            print()
            login2 = input("Password: ")
            file = open(login1 + ".txt", "r")
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")

    if welcome == "change":
        while True:
            login1 = input("Login: ")
            print()
            login2 = input("New Password: \n")
            file = open(login1 + ".txt", "r")  # Need help changing a password
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")


# insert welcome ****************************************************

Order_LIST = []
CREATE_FLAG = 1
OPTION_FLAG = 1



while OPTION_FLAG != 0: # Option 0 sends the user back
    option = Helper_Func.Menu()

    if option == 1:
        while (CREATE_FLAG == 1):
            print("Please input Staff Name and press enter")
            ID = input()
            print("Please input the description and press enter")
            print("[If you require a unique order token, input UOT and press enter]")
            Order_Desc = input()
            print("Please input your Name (optional) and press enter")
            Name = input()

            if Name == "":
                Name = "Not specified"

            Order =  Create_Ticket(ID, Name, Order_Desc)

            if "UOT" in Order.Problem:
                Order = Helper_Func.UniqueToken(Order)
                Helper_Func.DisplayOrder(Order)
                Order_LIST.append(Order)
            else:
                Order_LIST.append(Order)

            print("Do you want to create another request? (Y/N)")
            user_in = input()
            if user_in == "N" or user_in == "n":
                CREATE_FLAG = 0

    elif option == 2:
        for obj in Order_LIST:
            print("*******************")
            print("Order No: ", obj.OrderNo)
            print("ID: ", obj.ID)
            print("Name: ", obj.Name)
            print("Description of the request: ", obj.Problem)
            print("Ticket Status: ", obj.Order_STATUS)

            if obj.Response != "N/A":
                print("Response: ", obj.Response)
            print("*******************")

    elif option == 3:
        print("Please enter the ticket number to respond: ")
        USER_IN_Order_NO = int(input())

        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                print("Please enter the response for the ticket No: ", obj.OrderNo)
                RESPONSE_INPUT = input()
                obj.Response = RESPONSE_INPUT
                obj.Order_STATUS = "Closed"

    elif option == 4:
        print("Please enter the ticket number to reopen: ")
        USER_IN_Order_NO = int(input())

        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                if obj.Order_STATUS == "Closed":
                    obj.Order_STATUS = "Reopened"
                    print("Please enter the description for the ticket No: ", obj.OrderNo)
                    print("[If you require a unique ticket token, input UOT and press enter]")
                    Order_Desc = input()
                    obj.Problem = Order_Desc
                    if "UOT" in obj.Problem:
                        TK = Helper_Func.UniqueToken(obj)
                        Helper_Func.DisplayOrder(TK)

    elif option == 5:
        print("Displaying ticket details")
        C, F, R =  Create_Ticket.Stats(Order_LIST)

        print("++++++++++++++++++++++++++++")
        print("Created: ", C)
        print("Finished: ", F)
        print("Remaining: ", R)
        print("++++++++++++++++++++++++++++")

    else:
        OPTION_FLAG = 0
        print("Exiting, thank you have a great day...")
        os._exit(0)
