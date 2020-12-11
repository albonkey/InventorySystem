import tkinter as tk
from tkinter import ttk
from invoiceModule import invoiceModule
from productModule import productModule
from sidebar import Sidebar
from createListFrame import createListFrame

class ProductsView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.heading = tk.Label(self, text="Products", background="lightgrey",pady="5")
        self.heading.pack(side="top", fill="x")
        self.sidebar = Sidebar(self, "Products")
        self.sidebar.pack(side="left", fill="y")
        self.main = tk.Frame(master=self)
        self.productsList = createListFrame(self.main, "Products", productModule.getAllProducts(),"No Products", "Change Product", self.changeProduct, [""] )

        self.productAdd = tk.Frame(master=self.main, padx=30, pady=100)
        self.productAddInit()
        self.switchMain("Product List")


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


        btn_submit = tk.Button(master=self.productAdd, text="Add Product", height=3, width=10,
            command= lambda: self.createProduct(ent_name.get(), ent_description.get(), ent_category.get(), ent_cost.get(), ent_inventory.get()))
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

    def changeProduct(self, id):
        print("product Changed: " + str(id))

    def createProduct(self, name, description, category, cost, qty):
        productModule.createProduct(name, description, category, cost, qty)
        self.switchMain("Product List")

    def switchMain(self, name):
        self.productsList.pack_forget()
        self.productAdd.pack_forget()
        if(name == "Product List"):
            self.productsList = createListFrame(self.main, "Products", productModule.getAllProducts(),"No Products", "Change Product", self.changeProduct, [""] )
            self.productsList.pack()
        elif(name == "Add Product"):
            self.productAdd.pack()

        self.main.pack()
