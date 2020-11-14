import tkinter as tk
from tkinter import ttk
from invoices import Invoices
from products import Products
#from products import Products
from sidebar import Sidebar

class ProductsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.sidebar = Sidebar(self, "Invoices")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.productsList = tk.Frame(master=self.main, padx=30, pady=30)
        self.productsListInit()
        self.productAdd = tk.Frame(master=self.main, padx=30, pady=30)
        self.productAddInit()
        self.switchMain("Product List")


    def productsListInit(self):
        rowcount = 1
        for product in Products.products:
            colcount = 0
            for attribute, value in product.__dict__.items():
                if(rowcount == 1):
                    self.label = tk.Label(master=self.productsList, text=attribute)
                    self.label.grid(row=rowcount-1, column=colcount)
                self.label = tk.Label(master=self.productsList, text=value)
                self.label.grid(row=rowcount, column=colcount)
                colcount += 1
            rowcount += 1


    def productAddInit(self):
        lbl_name = tk.Label(master=self.productAdd, text="Name")
        ent_name = tk.Entry(master=self.productAdd)
        lbl_description = tk.Label(master=self.productAdd, text="Description")
        ent_description = tk.Entry(master=self.productAdd)
        lbl_category = tk.Label(master=self.productAdd, text="Category")
        ent_category = tk.Entry(master=self.productAdd)
        lbl_cost = tk.Label(master=self.productAdd, text="Cost")
        ent_cost = tk.Entry(master=self.productAdd)
        lbl_inventory = tk.Label(master=self.productAdd, text="Inventory")
        ent_inventory = tk.Entry(master=self.productAdd)


        btn_submit = tk.Button(master=self.productAdd, text="Add Product", height=3, width=10)
        lbl_name.pack()
        ent_name.pack()
        lbl_description.pack()
        ent_description.pack()
        lbl_category.pack()
        ent_category.pack()
        lbl_cost.pack()
        ent_cost.pack()
        lbl_inventory.pack()
        ent_inventory.pack()
        btn_submit.pack()



    def switchMain(self, name):
        self.productsList.pack_forget()
        self.productAdd.pack_forget()
        if(name == "Product List"):
            self.productsList.pack()
        elif(name == "Add Product"):
            self.productAdd.pack()

        self.main.pack()
