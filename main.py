import tkinter as tk
from controller import UserInterface


root = tk.Tk()
root.geometry("1200x800")
UserInterface(root).pack(side="top", fill="both", expand=True)
root.mainloop()
