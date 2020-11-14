import tkinter as tk
from tkinter import ttk
from invoices import Invoices
from clients import Clients
#from products import Products
from sidebar import Sidebar

class InvoicesView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.sidebar = Sidebar(self, "Invoices")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.invoicesList = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoicesListInit()
        self.invoiceAdd = tk.Frame(master=self.main, padx=30, pady=30)
        self.invoiceAddInit()
        self.switchMain("Invoice List")


    def invoicesListInit(self):
        rowcount = 1
        for invoice in Invoices.invoices:
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
        lbl_user = tk.Label(master=self.invoiceAdd, text="User")
        ent_user = tk.Entry(master=self.invoiceAdd)

        lbl_client = tk.Label(master=self.invoiceAdd, text="Client")
        cbox_client = ttk.Combobox(self.invoiceAdd, width = 27)
        cbox_client['values'] = (Clients.clients)

        lbl_title = tk.Label(master=self.invoiceAdd, text="Title")
        ent_title = tk.Entry(master=self.invoiceAdd)
        lbl_description = tk.Label(master=self.invoiceAdd, text="Description")
        ent_description = tk.Entry(master=self.invoiceAdd)

        lbl_products = tk.Label(master=self.invoiceAdd, text="Products")
        a = tk.StringVar()
        cbox_products = ttk.Combobox(self.invoiceAdd, width = 27, textvariable = a)
        cbox_products['values'] = (Clients.clients)

        btn_submit = tk.Button(master=self.invoiceAdd, text="Add Invoice", height=3, width=10)
        lbl_user.pack()
        ent_user.pack()
        lbl_client.pack()
        cbox_client.pack()
        lbl_title.pack()
        ent_title.pack()
        lbl_description.pack()
        ent_description.pack()
        lbl_products.pack()
        cbox_products.pack()
        btn_submit.pack()



    def switchMain(self, name):
        self.invoicesList.pack_forget()
        self.invoiceAdd.pack_forget()
        if(name == "Invoice List"):
            self.invoicesList.pack()
        elif(name == "Add Invoice"):
            self.invoiceAdd.pack()

        self.main.pack()
