import tkinter as tk
import uuid
from clientModule import clientModule
from sidebar import Sidebar


class ClientsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Clients", background="lightgrey", pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Clients")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)

        self.clientList = tk.Frame(master=self.main, padx=30, pady=30)

        self.clientAdd = tk.Frame(master=self.main, padx=30, pady=100)
        self.clientAddInit()

        self.clientInvoicesList = tk.Frame(master=self.main, padx=30, pady=30)

        self.switchMain("Client List")

    #Creating a view of the list of clients
    def clientListInit(self):
        rowcount = 1
        for client in clientModule.get_all_clients():
            colcount = 0
            for key in client:
                if (rowcount == 1):
                    self.label = tk.Label(master=self.clientList, text=key)
                    self.label.grid(row=rowcount - 1, column=colcount, ipady=10,ipadx=3, sticky="NESW")
                self.label = tk.Label(master=self.clientList, text=client[key])
                if(rowcount % 2):
                    self.label["background"] = "lightgrey"
                self.label.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
                colcount += 1
            self.button = tk.Button(master=self.clientList, text="See Invoices")
            self.button.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
            rowcount += 1

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

    def seeClientInvoices(self, client_id):
        return null

    def createClient(self, name, email, address):
        clientModule.createClient( name, email, address)
        self.switchMain("Client List")

    #Changing between the views.
    def switchMain(self, name):
        self.clientList.pack_forget()
        self.clientAdd.pack_forget()
        if name == "Client List":
            self.clientListInit()
            self.clientList.pack()
        elif name == "Add Client":
            self.clientAdd.pack()

        self.main.pack()
