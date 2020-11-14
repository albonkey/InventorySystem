import tkinter as tk
import tkinter.font as tkFont

class Header(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        lbl_logo = tk.Label(master=self, text="Inventory System", bg="grey", activebackground="grey", padx=15, font = fontStyle)
        lbl_logo.pack(side=tk.LEFT, fill="y")
        self.addButton('Invoices')
        self.addButton('Products')
        self.addButton('Clients')


    def addButton(self, name):
        button = tk.Button(master=self, width=20, height=4, bg="black", text=name, relief="flat", command=lambda:self.parent.switchView(name))
        button.pack(side=tk.RIGHT)
