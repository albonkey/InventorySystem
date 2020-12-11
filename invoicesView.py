import tkinter as tk
from tkinter import ttk
from invoiceModule import invoiceModule
from clientModule import clientModule
from productModule import productModule
from sidebar import Sidebar
from createListFrame import createListFrame

class InvoicesView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Invoices", background="lightgrey",pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Invoices")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.invoicesList = tk.Frame()
        self.updateList("unpaid")

        self.invoiceAdd = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoiceAddInit()
        self.products = {}
        self.productList = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoiceProductList()
        self.switchMain("Current Invoices")

    #Creating a view of the list of invoices
    def updateList(self, type):
        if(type == "paid"):
            self.invoicesList = createListFrame(self.main, "Invoice History", invoiceModule.getPaidInvoices(),"Currently no paid invoices.", "Delete Invoice", self.payInvoice )
        elif(type == "unpaid"):
            self.invoicesList = createListFrame(self.main, "Unpaid Invoices", invoiceModule.getUnpaidInvoices(), "Currently no unpaid invoices.", "Pay Invoice", self.payInvoice )
    #creating a view of the form for creating invoices
    def invoiceAddInit(self):
        dropdownClients = {}
        dropdownClients[""] = "" # Blank space for dropdownmenu
        for client in clientModule.get_all_clients():
            dropdownClients[client["_id"]] = client["CustomerName"]

        tkvar_client = tk.StringVar(master=self.invoiceAdd)
        lbl_client = tk.Label(master=self.invoiceAdd, text="Client")
        opt_client = ttk.OptionMenu(self.invoiceAdd, tkvar_client,  *dropdownClients.values())
        opt_client["width"] = 18

        lbl_title = tk.Label(master=self.invoiceAdd, text="Title")
        ent_title = tk.Entry(master=self.invoiceAdd)
        lbl_description = tk.Label(master=self.invoiceAdd, text="Description")
        ent_description = tk.Entry(master=self.invoiceAdd)
        lbl_dueDate = tk.Label(master=self.invoiceAdd, text="Due Date")
        ent_dueDate = tk.Entry(master=self.invoiceAdd)
        btn_submit = tk.Button(master=self.invoiceAdd, text="Create Invoice", height=3, width=10,
            command= lambda: self.createInvoice(get_id(tkvar_client.get()), ent_title.get(), ent_description.get(), ent_dueDate.get(), self.products)
        )

        lbl_client.pack(padx=5, pady=5, fill="x")
        opt_client.pack(padx=5, pady=5,fill="x")
        lbl_title.pack(padx=5, pady=5, fill="x")
        ent_title.pack(padx=5, pady=5, fill="x")
        lbl_description.pack(padx=5, pady=5, fill="x")
        ent_description.pack(padx=5, pady=5, fill="x")
        lbl_dueDate.pack(padx=5, pady=5, fill="x")
        ent_dueDate.pack(padx=5, pady=5, fill="x")
        btn_submit.pack(padx=5, pady=5, fill="x")

        def get_id(*args):  # on select function
            for i,j in dropdownClients.items():
                if j==tkvar_client.get():
                    return i



    #Creating view for adding products to the invoice
    def invoiceProductList(self):
        dropdownProducts = {}
        dropdownProducts[""] = "" # Blank space for dropdownmenu
        for product in productModule.getAllProducts():
            dropdownProducts[product["_id"]] = product["ProductName"]

        lbl_products = tk.Label(master=self.productList, text="Products")
        tkvar_product = tk.StringVar(master=self.productList)
        opt_products = ttk.OptionMenu(self.productList, tkvar_product, *dropdownProducts.values())
        opt_products["width"] = 18

        btn_addProduct = tk.Button(master=self.productList, text="Add Product",padx=5, pady=3, command= lambda: self.addProduct(get_id(tkvar_product.get()),tkvar_product.get()))

        lbl_products.pack(padx=5, pady=5, fill="x")
        opt_products.pack(padx=5, pady=5, fill="x")
        btn_addProduct.pack(padx=5, pady=5, fill="x")

        def get_id(*args):  # on select function
            for i,j in dropdownProducts.items():
                if j==tkvar_product.get():
                    return i


    def addProduct(self, productID, product):
        if productID in self.products:
            self.products[productID] += 1
        else:
            self.products[productID] = 1
        self.label = tk.Label(master=self.productList, text=product)
        self.label.pack(padx=5, pady=5, fill="x")

        self.switchMain("Create Invoice")

    def payInvoice(self, id):
        invoiceModule.payInvoice(id)

    def createInvoice(self, client, title, description, dueDate, list):
        cost = 0
        for product in self.products:
            cost += productModule.getProduct(product)["Cost"]
        invoiceModule.createInvoice( client, title, description, dueDate, cost, list)

        self.switchMain("Invoice List")


    def switchMain(self, name):
        self.invoicesList.pack_forget()
        self.invoiceAdd.pack_forget()
        self.productList.pack_forget()
        if(name == "Current Invoices"):
            self.updateList("unpaid")
            self.invoicesList.pack()
        elif(name == "Invoice History"):
            self.updateList("paid")
            self.invoicesList.pack()
        elif(name == "Create Invoice"):
            self.invoiceAdd.pack(fill="both", side="left", expand=True)
            self.productList.pack(fill="both", side="right", expand=True)

        self.main.pack(fill="both")
