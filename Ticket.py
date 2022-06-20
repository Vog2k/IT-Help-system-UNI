class Create_Ticket(object):
    OrderNo = 2000  # Ticket number displayed starts from 2000

    def __init__(self, ID, Name, problem):
        self.ID = ID  # ID made up of the first characters of both first and last name plus the hexadecimal
        self.Name = Name  # Users name
        self.Problem = problem  # User will enter problem and send a request
        self.OrderNo += 1
        Create_Ticket.OrderNo += 1
        self.Ticket_STATUS = "Open"
        self.Response = "N/A"
        # body of the constructor

    def Stats(Order_LIST):
        # Will display the created , finished amd remaining tickets
        created = 0
        finished = 0
        remaining = 0
        for obj in Order_LIST:
            created += 1
            if obj.Ticket_STATUS == "Closed" or obj.Ticket_STATUS == "Reopened":
                finished += 1
            else:
                remaining += 1
        return created, finished, remaining
