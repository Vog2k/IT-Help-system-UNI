import datetime


class Helper_Func(object):
    """Class to make the system more readable"""

    def __init__(self):
        pass

    def DisplayOrder(obj):
        print("*******************")
        print("Order No: ", obj.OrderNo) # Pulling the variable made from Ticket.py
        print("ID: ", obj.ID)
        print("Name: ", obj.Name)
        print("Description of the issue: ", obj.Problem)
        print("Order Status: ", obj.Order_STATUS)

        if obj.Response != "N/A":
            print("Response: ", obj.Response)
        print("*******************")

    def UniqueToken(Order):
        timestamp = datetime.datetime.now()
        timestamp_req = str(timestamp.day + timestamp.month + timestamp.year)
        timestamp_req = int(timestamp_req[0:3])
        OrderNo_req = int(Order.OrderNo)
        HEX_Token = Order.ID[0:2] + hex(OrderNo_req) + hex(timestamp_req)
        Order.Response = "Your unique token is: " + HEX_Token

        if Order.Order_STATUS == "Closed":
            Order.Order_STATUS = "Reopened"
        elif Order.Order_STATUS == "Open":
            Order.Order_STATUS = "Closed"

        return Order

    def Menu():
        print("--------------------------")
        print("Select an option from the list below and press enter...")
        print("0. Exit")
        print("1. Create an request")
        print("2. Display requests")
        print("3. Respond to an existing request")
        print("4. Reopen to an existing request")
        print("5. Display ticket stats")
        print("------------------------\n")
        option = int(input("Enter the option number here: "))
        return option
