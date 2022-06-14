class Create_Ticket(object):
    OrderNo = 2000  # Ticket number displayed starts from 2000
    """Class to create orders"""

    def __init__(self, identification, name, problem):
        self.ID = identification  # ID made up of the first characters of both first and last name plus the hexadecimal
        self.Name = name  # Users name
        self.Problem = problem  # User will enter problem and send a request
        self.OrderNo += 1
        Create_Ticket.OrderNo += 1
        self.Order_STATUS = "Open"
        self.Response = "N/A"
        # body of the constructor

    def Stats(Order_LIST):
        # Will display the created , finished amd remaining tickets
        created = 0
        finished = 0
        remaining = 0
        for obj in Order_LIST:
            created += 1
            if obj.Order_STATUS == "Closed" or obj.Order_STATUS == "Reopened":
                finished += 1
            else:
                remaining += 1
        return created, finished, remaining
