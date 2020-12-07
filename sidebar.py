import tkinter as tk

invoices = ["Invoice List", "Create Invoice"]
clients = ["Client List", "Add Client"]
products = ["Product List", "Add Product"]

class Sidebar(tk.Frame):
    def __init__(self, parent, sidebar, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.loadSidebar(sidebar)


    def loadSidebar(self, sidebar):
        if sidebar == "Invoices":
            for a in invoices:
                button = tk.Button(master=self, width=20, height=5, text=a, command=lambda a=a :self.parent.switchMain(a))
                button.pack(fill="x")
        elif sidebar == "Clients":
            for a in clients:
                button = tk.Button(master=self, width=20, height=5, text=a, command=lambda a=a :self.parent.switchMain(a))
                button.pack(fill="x")
        elif sidebar == "Products":
            for a in products:
                button = tk.Button(master=self, width=20, height=5, text=a, command=lambda a=a :self.parent.switchMain(a))
                button.pack(fill="x")
