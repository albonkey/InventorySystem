import tkinter as tk

class Header(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        lbl_logo = tk.Label(master=self, text="Inventory System")
        lbl_logo.pack(side=tk.LEFT, fill="y")
        self.addButton('Invoices')
        self.addButton('Products')
        self.addButton('Clients')


    def addButton(self, name):
        button = tk.Button(master=self, width=20, height=4, text=name, bg='grey', command=lambda:self.parent.switchSidebar(name))
        button.pack(side=tk.RIGHT)
