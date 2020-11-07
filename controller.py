import tkinter as tk
from header import Header
from sidebar import Sidebar
from clientsView import ClientsView

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.header = Header(self)
        self.header.pack(side="top", fill = "y")
        self.view = ClientsView(self)
        self.view.pack()
        


    #def switchSidebar(self, sidebar):
    #    self.sidebar.pack_forget()
    #    self.sidebar = Sidebar(self, sidebar)
    #    self.sidebar.pack(side="left", fill = "x")

    def switchView(self, view):
        self.view.pack_forget()
        self.view = ClientsView(self)
        self.view.pack(side="center", fill= "both")
