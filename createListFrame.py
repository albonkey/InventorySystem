import tkinter as tk
from tkinter import ttk

def createListFrame(parent, list, empty_text,  btn_text, btn_function):
    frame = tk.Frame(master=parent, padx=30, pady=30)
    if(list.count() == 0):
        label = tk.Label(master=frame, text=empty_text)
        label.pack()
    else:
        rowcount = 1
        for item in list:
            colcount = 0
            for key in item:
                if(rowcount == 1):
                    label = tk.Label(master=frame, text=key)
                    label.grid(row=rowcount-1, column=colcount, ipady=10,ipadx=3, sticky="NESW")

                label = tk.Label(master=frame, text=item[key])
                if(rowcount % 2):
                    label["background"] = "lightgrey"
                label.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
                colcount += 1

            button = tk.Button(master=frame, text=btn_text, command= lambda a=item["_id"]: btn_function(a))
            button.grid(row=rowcount, column=colcount, ipady=10,ipadx=3, sticky="NESW")
            rowcount += 1

    return frame
