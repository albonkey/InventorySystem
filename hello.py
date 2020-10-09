import tkinter as tk

class User:
    def __init__(self, id, name, email, password, isAdmin ):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.isAdmin = isAdmin;

class Client:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.invoices = []
        self.joined = "01/01/2020";

        #Function to calculate how much they owe
        #Function to see Invoices that is not paid
        #Functions to see Invoices that are paid

class Product:
    def __init__(self, id, name, description, category, cost):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.cost = cost

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


#Implement Inventory Class

#Implement ClientList Class

#Implement UserList Class / Not that important

#Implement a InvoiceList Class. 

#Log In form / This we can do at the end if we get time.
#New Client Form
#New Product Form
#New Invoice Form

#Functions to implement all the form data.


#Create GUI


class Application(tk.Frame):
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World"
        self.hi_there["width"] = 40
        self.hi_there["height"] = 20
        self.hi_there.pack(side="top")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
