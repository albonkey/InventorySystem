import tkinter as tk
from header import Header
from sidebar import Sidebar
from clientsView import ClientsView
from invoicesView import InvoicesView
from productsView import ProductsView
import tkinter.font as tkFont

class UserInterface(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.header = Header(self)
        self.header.pack(side="top", fill="both")
        self.view = tk.Frame(master=self)
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.welcome = tk.Label(master=self.view, text="WELCOME", pady=10, font=fontStyle, bg="lightgrey")
        self.welcome.pack(fill="x", expand=True)
        self.underHeading = tk.Label(master=self.view, text="Press the menu to get started", pady=30)
        self.underHeading.pack()
        self.view.pack(fill="both")



    #def switchSidebar(self, sidebar):
    #    self.sidebar.pack_forget()
    #    self.sidebar = Sidebar(self, sidebar)
    #    self.sidebar.pack(side="left", fill = "x")

    def switchView(self, view):
        self.view.pack_forget()
        if(view == "Clients"):
            self.view = ClientsView(self)
        elif(view == "Invoices"):
            self.view = InvoicesView(self)
        elif(view == "Products"):
            self.view = ProductsView(self)
        self.view.pack(fill= "both")
