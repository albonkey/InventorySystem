class User:
    def __init__(self, id, name, email, password, isAdmin ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.isAdmin = isAdmin;
        #possible client array for each user? 
        self.clients = []

class Client:
    def __init__(self, id, name, email, address):
        self.id = id
        self.name = name
        self.email = email
        self.address= address
        self.invoices = []
        self.joined = "01/01/2020";

        #Function to calculate how much they owe
        #Function to see Invoices that is not paid
        #Functions to see Invoices that are paid

class Product:
    def __init__(self, id, name, description, category, cost, inventory):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.cost = cost
        self.inventory = inventory

class Invoice:
    def __init__(self, id, user, client, title, description, products, dueDate):
        self.id = id
        self.user = user
        self.client = client
        self.title = title
        self.description = description
        self.products = products
        self.dueDate = dueDate
        self.date = "01/01/2020"
        self.isPaid = False;

        #Function to check total cost of products
        #Function to check number of products
        #Function to pay it.


products = [];
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
products.append(Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10))
