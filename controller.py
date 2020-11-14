import tkinter as tk
from header import Header
from sidebar import Sidebar
from clientsView import ClientsView
from invoicesView import InvoicesView

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.header = Header(self, bg= 'grey')
        self.header.pack(side="top", fill="both")
        self.view = ClientsView(self)
        self.view.pack(fill="both")



    #def switchSidebar(self, sidebar):
    #    self.sidebar.pack_forget()
    #    self.sidebar = Sidebar(self, sidebar)
    #    self.sidebar.pack(side="left", fill = "x")

    def switchView(self, view):
        print(view)
        self.view.pack_forget()
        if(view == "Clients"):
            self.view = ClientsView(self)
        elif(view == "Invoices"):
            self.view = InvoicesView(self)
        self.view.pack(fill= "both")
