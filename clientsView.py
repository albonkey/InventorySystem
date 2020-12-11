import tkinter as tk
import uuid
from clientModule import clientModule
from invoiceModule import invoiceModule
from sidebar import Sidebar
from createListFrame import createListFrame


class ClientsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Clients", background="lightgrey", pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Clients")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)

        self.clientList = createListFrame(self.main, "Clients", clientModule.get_all_clients(),"No Clients", "See Invoices", self.clientInvoiceView)

        self.clientAdd = tk.Frame(master=self.main, padx=30, pady=100)
        self.clientAddInit()

        self.clientView = tk.Frame(master=self.main)


        self.switchMain("Client List")

    #Creating a view of the invoices of clients
    def clientInvoiceView(self, client_id):
        client = clientModule.getClient(client_id)
        print(client)
        self.clientView = createListFrame(self.main, client["CustomerName"], invoiceModule.getInvoices(client_id), "No Invoices", "Pay Invoice", lambda: invoiceModule.payInvoice(client_id) )
        self.switchMain("Client View")
    #creating a view of the form for adding clients
    def clientAddInit(self):
        lbl_name = tk.Label(master=self.clientAdd, text="Name")
        ent_name = tk.Entry(master=self.clientAdd)
        lbl_email = tk.Label(master=self.clientAdd, text="Email")
        ent_email = tk.Entry(master=self.clientAdd)
        lbl_address = tk.Label(master=self.clientAdd, text="Address")
        ent_address = tk.Entry(master=self.clientAdd)
        btn_submit = tk.Button(master=self.clientAdd, text="Add Client", height=3, width=10,
                                command=lambda: buttonAction())
        lbl_name.pack()
        ent_name.pack()
        lbl_email.pack()
        ent_email.pack()
        lbl_address.pack()
        ent_address.pack()
        btn_submit.pack()

        def buttonAction():
            self.createClient(ent_name.get(), ent_email.get(), ent_address.get())

            ent_name.delete(0,100)
            ent_email.delete(0,100)
            ent_address.delete(0,100)


    def createClient(self, name, email, address):
        clientModule.createClient( name, email, address)
        self.switchMain("Client List")

    #Changing between the views.
    def switchMain(self, name):
        self.clientList.pack_forget()
        self.clientAdd.pack_forget()
        self.clientView.pack_forget()
        if name == "Client List":
            self.clientList = createListFrame(self.main, "Clients", clientModule.get_all_clients(),"No Clients", "See Invoices", self.clientInvoiceView)
            self.clientList.pack()
        elif name == "Add Client":
            self.clientAdd.pack()
        elif name == "Client View":
            self.clientView.pack()

        self.main.pack()
