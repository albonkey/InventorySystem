import tkinter as tk
from clientModule import clientModule
from sidebar import Sidebar

class ClientsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Clients", background="lightgrey",pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Clients")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.clientList = tk.Frame(master=self.main, padx=30, pady=30)
        self.clientListInit()
        self.clientAdd = tk.Frame(master=self.main, padx=30, pady=30)
        self.clientAddInit()
        self.switchMain("Client List")

    def clientListInit(self):
        rowcount = 1
        for client in clientModule.getClients():
            colcount = 0
            for attribute, value in client.__dict__.items():
                if(rowcount == 1):
                    self.label = tk.Label(master=self.clientList, text=attribute)
                    self.label.grid(row=rowcount-1, column=colcount)
                self.label = tk.Label(master=self.clientList, text=value)
                self.label.grid(row=rowcount+1, column=colcount)
                colcount += 1
            rowcount += 1

    def clientAddInit(self):
        lbl_name = tk.Label(master=self.clientAdd, text="Name")
        ent_name = tk.Entry(master=self.clientAdd)
        lbl_email = tk.Label(master=self.clientAdd, text="Email")
        ent_email = tk.Entry(master=self.clientAdd)
        lbl_address = tk.Label(master=self.clientAdd, text="Address")
        ent_address = tk.Entry(master=self.clientAdd)
        btn_submit = tk.Button(master=self.clientAdd, text="Add Client", height=3, width=10,
            command= lambda: self.createClient(ent_name.get(), ent_email.get(), ent_address.get())
        )
        lbl_name.pack()
        ent_name.pack()
        lbl_email.pack()
        ent_email.pack()
        lbl_address.pack()
        ent_address.pack()
        btn_submit.pack()


    def createClient(self, name, email, address):
        clientModule.createClient(1, name, email, address)
        self.clientListInit()
        self.switchMain("Client List")

    def switchMain(self, name):
        self.clientList.pack_forget()
        self.clientAdd.pack_forget()
        if(name == "Client List"):
            self.clientList.pack()
        elif(name == "Add Client"):
            self.clientAdd.pack()

        self.main.pack()
