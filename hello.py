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


#Implement Inventory Class

#Implement ClientList Class

#Implement UserList Class / Not that important

#Implement a InvoiceList Class.

#Log In form / This we can do at the end if we get time.
#New Client Form
#New Product Form
#New Invoice Form

#Functions to implement all the  form data.


#Create GUI
color1 = "grey"
color2 = "lightgrey"

#Window
window = tk.Tk()

#Header
frm_header = tk.Frame(master=window, width=1200, height=100, bg=color1)
frm_header.pack(side=tk.TOP, fill=tk.BOTH)

lbl_logo = tk.Label(master=frm_header, width=20, height=4, text="Inventory System", bg=color1)
lbl_logo.pack(side=tk.LEFT)

btn_add = tk.Button(master=frm_header, height=4, width=15, text="+", bg=color1)
btn_add.pack(side=tk.RIGHT)

btn_invoice = tk.Button(master=frm_header, height=4, width=15, text="Invoice    ", bg=color1)
btn_invoice.pack(side=tk.RIGHT)

btn_products = tk.Button(master=frm_header, height=4, width=15, text="Products", bg=color1)
btn_products.pack(side=tk.RIGHT)

btn_client = tk.Button(master=frm_header, height=4, width=15, text="Client", bg=color1)
btn_client.pack(side=tk.RIGHT)

#Main
frm_main = tk.Frame(master=window, width=1000, height=600)
frm_main.pack(fill=tk.BOTH, expand=True)

#Sidebar
frm_sidebar = tk.Frame(master=frm_main, width=200, height=600, bg=color2)
frm_sidebar.pack(side=tk.LEFT, fill=tk.BOTH)

frm_sidebarAdd = tk.Frame(master=frm_sidebar)
frm_sidebarAdd.pack()

btn_sidebarAddProduct = tk.Button(master=frm_sidebarAdd, width=20, height=5, text="Add Product")
btn_sidebarAddProduct.pack(fill=tk.X)

btn_sidebarAddClient = tk.Button(master=frm_sidebarAdd, width=20, height=5, text="Add Client")
btn_sidebarAddClient.pack()

btn_sidebarAddInvoice = tk.Button(master=frm_sidebarAdd, width=20, height=5, text="Add Invoice")
btn_sidebarAddInvoice.pack()

#Footer
frm_footer = tk.Frame(master=window, width=1000, height=50, bg="grey")
frm_footer.pack(side=tk.BOTTOM, fill=tk.BOTH)

#New Form
frm_newProduct = tk.Frame(master=frm_main, pady=50)

lbl_newProductName = tk.Label(master=frm_newProduct, text="Name", pady=10)
lbl_newProductName.pack()
ent_newProductName = tk.Entry(master=frm_newProduct)
ent_newProductName.pack()

lbl_newProductDescription = tk.Label(master=frm_newProduct, text="Description", pady=10)
lbl_newProductDescription.pack()
ent_newProductDescription = tk.Entry(master=frm_newProduct)
ent_newProductDescription.pack()

lbl_newProductCost = tk.Label(master=frm_newProduct, text="Cost", pady=10)
lbl_newProductCost.pack()
ent_newProductCost = tk.Entry(master=frm_newProduct)
ent_newProductCost.pack()

lbl_newProductInventory = tk.Label(master=frm_newProduct, text="Inventory", pady=10)
lbl_newProductInventory.pack()
ent_newProductInventory = tk.Entry(master=frm_newProduct)
ent_newProductInventory.pack()

btn_newProductSubmit = tk.Button(master=frm_newProduct, width=20, height=3, text="Add Product")
btn_newProductSubmit.pack()

frm_newProduct.pack(expand=True)


window.mainloop()
