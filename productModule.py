from classes import Product

class ProductModule():
    products = [
        Product(1, "Product X", "Super cool.", "Category 1", 100, 10),
        Product(2, "Product Y", "Don't use this at home.", "Category 2", 750, 10),
        Product(3, "Product Z", "Might explode...", "Category 3", 500, 10)
    ]

    def createProduct(id, name, description, category, cost, qty):
        products.append(Product(id, name, description, category, cost, qty))
#Add product AddProduct(id, name, description, category, cost, inventory)
#Remove product RemoveProduct(id)
#Update Product UpdateProduct(id)
#Get Product
