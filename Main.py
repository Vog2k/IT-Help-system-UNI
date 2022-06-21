import os

import Ticket
from Ticket import Create_Ticket

import Menu
from Menu import Helper_Func


def Welcome():  # Sign in options

    print("Welcome...")
    welcome = input("Do you have an account? y/n: ")
    if welcome == "n":
        while True:
            username = input("Enter a username :")
            print()
            password = input("Enter a password :")
            '''This section is the sign in process which will ask the user if they have an account.'''
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
            '''If the user does have an account then this part of the code will run and the user will be asked
            to log in and sign in with their password'''
            data = file.readline()
            file.close()
            if data == login1 + ":" + login2:
                print("Welcome", " " + login1)
                break
            print("Incorrect username or password.")

    if welcome == "c":
        while True:
            username = input("Enter your username :")
            print()
            password = input("Enter a new password :")
            '''This section will tell the user to enter their username and a new passwords'''
            print()
            password1 = input("Confirm password :")
            if password == password1:
                file = open(username + ".txt", "w")
                file.write(username + ":" + password)
                file.close()
                welcome = "c"
                break
            print("Passwords do NOT match!")


Welcome()

Order_LIST = []
CREATE_FLAG = 1
OPTION_FLAG = 1

while OPTION_FLAG != 0:  # Option 0 sends the user back
    option = Helper_Func.Menu()

    if option == 1:
        while (CREATE_FLAG == 1):
            print("Please input Staff Name and press enter")
            ID = input()  # This section will need the user to enter a character or characters
            print("Please input the description and press enter")
            print("[If you require a ID number, input 'id' and press enter]")
            print("[If you require a new password please input 'c' and press enter]")
            Order_Desc = input()
            print("Please input your Name (optional) and press enter")
            Name = input()

            if Name == "":  # If the user does not enter a name the end will result in Not specified
                Name = "Not specified"

            Order = Create_Ticket(ID, Name, Order_Desc)

            if "id" in Order.Problem:  # This will give the user their new id number with hexadecimal and binary
                Order = Helper_Func.UniqueToken(Order)
                Helper_Func.Ticket_Iformation(Order)
                Order_LIST.append(Order)
            elif "c" in Order.Problem:  # Sends the user to the password reset
                Order = Helper_Func.UniqueToken(Order)
                Helper_Func.Ticket_Iformation(Order)
                Order_LIST.append(Order)
                print("You will no be directed back to the login menu\n")
                print("To change password please input 'c' then press enter\n")
                Welcome()

            else:
                Order_LIST.append(Order)

            print("Do you want to create another request? (Y/N)")
            user_in = input()
            if user_in == "N" or user_in == "n":  # This will appear when trhe user has completed a new ticket
                CREATE_FLAG = 0

    elif option == 2:
        for obj in Order_LIST:
            print("*******************")
            print("Order No: ", obj.OrderNo)
            print("ID: ", obj.ID)  # This will display all the information on the current ticket
            print("Name: ", obj.Name)
            print("Description of the request: ", obj.Problem)
            print("Ticket Status: ", obj.Ticket_STATUS)

            if obj.Response != "N/A":
                print("Response: ", obj.Response)
            print("*******************")

    elif option == 3:
        print("Please enter the ticket number to respond: ")
        USER_IN_Order_NO = int(input())  # This will open up a current ticket in use, requesting a ticket number

        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                print("Please enter the response for the ticket No: ", obj.OrderNo)
                RESPONSE_INPUT = input()
                obj.Response = RESPONSE_INPUT  # This will be activated once the user has entered a response
                obj.Ticket_STATUS = "Closed"  # After the response has been given the ticket status will close

    elif option == 4:
        print("Please enter the ticket number to reopen: ")
        USER_IN_Order_NO = int(input())
        # This will re open an exiting ticket that you can edit again
        for obj in Order_LIST:
            if obj.OrderNo == USER_IN_Order_NO:
                if obj.Ticket_STATUS == "Closed":
                    obj.Ticket_STATUS = "Reopened"
                    print("Please enter the description for the ticket No: ", obj.OrderNo)
                    print("[If you require a ID, input 'id' and press enter]")
                    print("[If you require a new password please input 'c' and press enter]")
                    Order_Desc = input()
                    obj.Problem = Order_Desc
                    if "id" in obj.Problem:
                        TK = Helper_Func.UniqueToken(obj)
                        Helper_Func.Ticket_Iformation(TK)

    elif option == 5:
        print("Displaying ticket details")
        C, F, R = Create_Ticket.Stats(Order_LIST)

        print("-----------------------------")
        print("Created: ", C)
        print("Finished: ", F)  # These three characters represent Created Finished and Remaining
        print("Remaining: ", R)
        print("-----------------------------")

    else:
        OPTION_FLAG = 0
        print("Exiting, thank you have a great day...") #This will exit the program
        os._exit(0)

"""Test case: Testing that making a new account will work
input: Tim
input: 123
expected output: Expected to store the username and password
actual output: Creates a new file to save username and passwords
result pass"""

"""Test case: Testing to see if i can enter a random name
input: Timmy
input: 1
expected output: Should crash
actual output: Does crash which is good
result pass"""

"""Test case: Testing the change password feature
input: '1'create a request
input: 'Tim' Staff name
input: 'c' Change password
input: 'Tim' enter username
input: '1' Enter a new password
input: '1' Confirm password
expected output: Should overwrite current password
actual output: Overwrites current password
result pass"""

"""Test case: Testing to see if programme ends
input: 0
expected output: should exit
actual output: Exits 
result pass"""

"""Test case: See if the input 2 will display the current ticket 
input: 2
expected output: Prints out ticket information
actual output: Prints out ticket information
result pass"""

"""Test case: Testing response function
input: 3
input: Completed
expected output: should ask the user to enter their response
actual output: Requires the user to enter a response and will print Completed under the response section in the ticket
result pass"""

"""Test case: Testing to see if i can reopen and existing request
input: 4
expected output: Re open up the existing request
actual output: Re opens up the existing request
result pass"""

"""Test case: Testing to see if 5 input works 
input: 5
expected output: should display how many tickets have been created , finished and remaining tickets 
actual output: Displays all information 
result pass"""

"""Test case: Testing to what happens when i enter a random character
input: 1
expected output: should crash because it does not have knowledge of this charter
actual output: continues onto the next stage just this the user dose not have a username or password 
result failed"""
