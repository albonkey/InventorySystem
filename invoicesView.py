import tkinter as tk
from tkinter import ttk
from invoiceModule import invoiceModule
from clientModule import clientModule
from productModule import productModule
from sidebar import Sidebar

class InvoicesView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Invoices", background="lightgrey",pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Invoices")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.invoicesList = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoicesListInit()
        self.invoiceAdd = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoiceAddInit()
        self.products = []
        self.productList = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoiceProductList()
        self.switchMain("Invoice List")


    def invoicesListInit(self):
        rowcount = 1
        for invoice in invoiceModule.getInvoices():
            colcount = 0
            for attribute, value in invoice.__dict__.items():
                if(rowcount == 1):
                    self.label = tk.Label(master=self.invoicesList, text=attribute)
                    self.label.grid(row=rowcount-1, column=colcount)
                self.label = tk.Label(master=self.invoicesList, text=value)
                self.label.grid(row=rowcount, column=colcount)
                colcount += 1
            rowcount += 1


    def invoiceAddInit(self):

        dropdownClients = []
        for client in clientModule.getClients():
            dropdownClients.append(client.name)
        tkvar_client = tk.StringVar(master=self.invoiceAdd)
        lbl_client = tk.Label(master=self.invoiceAdd, text="Client")
        opt_client = ttk.OptionMenu(self.invoiceAdd, tkvar_client, dropdownClients[1], *dropdownClients)
        opt_client["width"] = 18

        lbl_title = tk.Label(master=self.invoiceAdd, text="Title")
        ent_title = tk.Entry(master=self.invoiceAdd)
        lbl_description = tk.Label(master=self.invoiceAdd, text="Description")
        ent_description = tk.Entry(master=self.invoiceAdd)
        lbl_dueDate = tk.Label(master=self.invoiceAdd, text="Due Date")
        ent_dueDate = tk.Entry(master=self.invoiceAdd)
        btn_submit = tk.Button(master=self.invoiceAdd, text="Create Invoice", height=3, width=10,
            command= lambda: self.createInvoice(tkvar_client.get(), ent_title.get(), ent_description.get(), ent_dueDate.get())
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

    def invoiceProductList(self):
        dropdownProducts = []
        for product in productModule.getProducts():
            dropdownProducts.append(product.name)
        lbl_products = tk.Label(master=self.productList, text="Products")
        tkvar_product = tk.StringVar(master=self.productList)
        opt_products = ttk.OptionMenu(self.productList, tkvar_product, dropdownProducts[1], *dropdownProducts)
        opt_products["width"] = 18

        btn_addProduct = tk.Button(master=self.productList, text="Add Product",padx=5, pady=3, command= lambda: self.addProduct(tkvar_product.get()))

        lbl_products.pack(padx=5, pady=5, fill="x")
        opt_products.pack(padx=5, pady=5, fill="x")
        btn_addProduct.pack(padx=5, pady=5, fill="x")



    def addProduct(self, product):
        self.products.append(product)
        self.label = tk.Label(master=self.productList, text=product)
        self.label.pack(padx=5, pady=5, fill="x")

        self.switchMain("Create Invoice")


    def createInvoice(self, client, title, description, dueDate):
        invoiceModule.createInvoice(1, client, title, description, dueDate)
        self.invoicesListInit()
        self.switchMain("Invoice List")


    def switchMain(self, name):
        self.invoicesList.pack_forget()
        self.invoiceAdd.pack_forget()
        self.productList.pack_forget()
        if(name == "Invoice List"):
            self.invoicesList.pack()
        elif(name == "Create Invoice"):
            self.invoiceAdd.pack(fill="both", side="left", expand=True)
            self.productList.pack(fill="both", side="right", expand=True)

        self.main.pack(fill="both")
