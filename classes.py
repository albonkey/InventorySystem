class User:
    def __init__(self, id, name, email, password, isAdmin ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.isAdmin = isAdmin

class Client:
    def __init__(self, id, name, email, address):
        self.id = id
        self.name = name
        self.email = email
        self.address= address
        self.invoices = []
        self.joined = "01/01/2020"

        #Function to calculate how much they owe
        def calcOwed():
            total = 0
            for invoice in self.invoices:
                if invoice.isPaid:
                    total += invoice.totalCost

        #Function to see Invoices that is not paid
        def notPaidYet():
            for invoice in self.invoices:
                counter = 0
                if invoice.isPaid:
                    print(str(counter + 1) + "Invoices not paid: " + invoice)
        #Functions to see Invoices that are paid
        def PaidAlready():
            for invoice in self.invoices:
                counter = 0
                if not invoice.isPaid:
                    print(str(counter + 1) + "Invoices paid: " + invoice)



class Product:
    def __init__(self, id, name, description, category, cost, inventory):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.cost = cost
        self.inventory = inventory

class Invoice:
    def __init__(self, id, user, client, title, description, dueDate):
        self.id = id
        self.user = user
        self.client = client
        self.title = title
        self.description = description
        self.dueDate = dueDate
        self.date = "01/01/2020"
        self.isPaid = False
        

        #Function to check total cost of products


        #Function to pay it.
        def toPay():
            self.isPaid = True #Update database to be paid


products = []
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
