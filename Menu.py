import datetime


class Helper_Func(object):

    def __init__(self):
        pass

    def Ticket_Iformation(obj):
        print("*******************")
        print("Order No: ", obj.OrderNo)  # Pulling the variable made from Ticket.py
        print("Name: ", obj.Name)
        print("ID: ", obj.ID)
        print("Email: ", obj.Name, "@Whitecliffe.co.nz") # Used the Name object to
        print("Description of the issue: ", obj.Problem)
        print("Order Status: ", obj.Ticket_STATUS)

        if obj.Response != "N/A":
            print("Response: ", obj.Response)
        print("*******************")

    def UniqueToken(Order):
        timestamp = datetime.datetime.now()
        timestamp_req = str(timestamp.day + timestamp.month + timestamp.year)
        timestamp_req = int(timestamp_req[0:3])
        OrderNo_req = int(Order.OrderNo)
        HEX_Token = Order.ID[0:2] + hex(OrderNo_req) + hex(timestamp_req)
        Order.Response = "Your ID is: " + HEX_Token

        if Order.Ticket_STATUS == "Closed":
            Order.Ticket_STATUS = "Reopened"
        elif Order.Ticket_STATUS == "Open":
            Order.Ticket_STATUS = "Closed"

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
