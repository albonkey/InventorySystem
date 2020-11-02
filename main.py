import tkinter as tk
from controller import UserInterface


root = tk.Tk()
UserInterface(root).pack(side="top", fill="both", expand=True)
root.mainloop()
