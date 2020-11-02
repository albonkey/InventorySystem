import tkinter as tk

invoices = ["Invoice History", "Unpaid Invoices", "Add Invoice"]
clients = ["Category 1", "Category 2", "Category 3"]
products = ["Products 1", "Products 2", "Products 3"]

class Sidebar(tk.Frame):
    def __init__(self, parent, sidebar, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.loadSidebar(sidebar)


    def loadSidebar(self, sidebar):
        if sidebar == "Invoices":
            for a in invoices:
                button = tk.Button(master=self, width=20, height=5, text=a)
                button.pack(fill="x")
        elif sidebar == "Clients":
            for a in clients:
                button = tk.Button(master=self, width=20, height=5, text=a)
                button.pack(fill="x")
        elif sidebar == "Products":
            for a in products:
                button = tk.Button(master=self, width=20, height=5, text=a)
                button.pack(fill="x")