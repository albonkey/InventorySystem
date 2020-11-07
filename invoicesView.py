import tkinter as tk
from clients import Clients

class ClientsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label = tk.Label(master=self, text="Clients")
        self.label.pack()

    def clientsList():
