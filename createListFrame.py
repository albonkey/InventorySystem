import tkinter as tk
from tkinter import ttk

def createListFrame(parent, list, btn_text, btn_function):
    frame = tk.Frame(master=parent, padx=30, pady=30)

    rowcount = 1
    for item in list:
        colcount = 0
        for attribute, value in item.__dict__.items():
            if(rowcount == 1):
                label = tk.Label(master=frame, text=attribute)
                label.grid(row=rowcount-1, column=colcount, ipady=10,ipadx=3, sticky="NESW")

            label = tk.Label(master=frame, text=value)
            if(rowcount % 2):
                label["background"] = "lightgrey"
            label.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
            colcount += 1
        button = tk.Button(master=frame, text=btn_text, command= lambda a=item.id: btn_function(a))
        button.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
        rowcount += 1

    return frame
