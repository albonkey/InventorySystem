from classes import Product

class ProductModule():
    def __init__(self):
        self.products = [
            Product(1, "Product X", "Super cool.", "Category 1", 100, 10),
            Product(2, "Product Y", "Don't use this at home.", "Category 2", 750, 10),
            Product(3, "Product Z", "Might explode...", "Category 3", 500, 10)
        ]

    #Connect database here. And make the functions update the database

    def createProduct(self, id, name, description, category, cost, qty):
        self.products.append(Product(id, name, description, category, cost, qty))

    def getProducts(self):
        return self.products

    def updateProduct(self, id, name, description, category, cost, qty):
        return null

    def RemoveProduct(self, id):
        return null
#Add product AddProduct(id, name, description, category, cost, inventory)
#Remove product RemoveProduct(id)
#Update Product UpdateProduct(id)
#Get Product

productModule = ProductModule()
