import tkinter as tk
from header import Header
from sidebar import Sidebar

class UserInterface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.header = Header(self)
        self.header.pack(side="top", fill = "y")
        self.sidebar = Sidebar(self, "Products")
        self.sidebar.pack(side="left")


    def switchSidebar(self, sidebar):
        self.sidebar.pack_forget()
        self.sidebar = Sidebar(self, sidebar)
        self.sidebar.pack(side="left", fill = "x")
