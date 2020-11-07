import tkinter as tk
from clients import Clients
from sidebar import Sidebar

class ClientsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.sidebar = Sidebar(self, "Clients")
        self.sidebar.pack(side="left")
        self.main = tk.Frame(master=self)
        self.clientList = tk.Frame(master=self.main, padx=30)
        self.clientListInit()
        self.clientAdd = tk.Frame(master=self.main, padx=30)
        self.clientAddInit()


    def clientListInit(self):
        rowcount = 0
        for client in Clients.clients:
            rowcount += 1
            colcount = 0
            for attribute, value in client.__dict__.items():
                self.label = tk.Label(master=self.clientList, text=value)
                self.label.grid(row=rowcount, column=colcount)
                colcount += 1

    def clientAddInit(self):
        lbl_name = tk.Label(master=self.clientAdd, text="Name")
        ent_name = tk.Entry(master=self.clientAdd)
        lbl_email = tk.Label(master=self.clientAdd, text="Email")
        ent_email = tk.Entry(master=self.clientAdd)
        lbl_address = tk.Label(master=self.clientAdd, text="Address")
        ent_address = tk.Entry(master=self.clientAdd)
        btn_submit = tk.Button(master=self.clientAdd, text="Add Client", height=3, width=10)
        lbl_name.pack()
        ent_name.pack()
        lbl_email.pack()
        ent_email.pack()
        lbl_address.pack()
        ent_address.pack()
        btn_submit.pack()



    def switchMain(self, name):
        self.clientList.pack_forget()
        self.clientAdd.pack_forget()
        if(name == "Client List"):
            self.clientList.pack()
        elif(name == "Add Client"):
            self.clientAdd.pack()

        self.main.pack()
