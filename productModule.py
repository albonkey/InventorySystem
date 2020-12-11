
import pymongo
from bson.objectid import ObjectId


class ProductModule:
    def __init__(self):
        self.connection_string = "mongodb+srv://ultra:dundun428@ims.bnlzj.mongodb.net/inventory_MS?retryWrites=true&w" \
                                 "=majority"
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client.inventory_MS
        self.collection = self.db.products

    def createProduct(self, name, description, category, cost, qty):
        """This function creates a new product in the DB"""
        product = {
            "ProductName": name,
            "Description": description,
            "Category": category,
            "Cost": cost,
            "Inventory": qty
        }
        self.collection.insert_one(product)

    def getProduct(self, product_id):
        """This function returns a product from the DB"""
        query = {"_id": ObjectId(product_id)}
        product = self.collection.find_one(query)
        return product

    def getAllProducts(self):
        """This function returns all products in the DB"""
        all_products = self.collection.find({})
        return all_products

    def updateProduct(self, product_id, name, description, category, cost, qty):
        """This function updates a product information in the DB"""
        query = {"_id": ObjectId(product_id)}
        new_values = {"$set":
            {
                "ProductName": name,
                "Description": description,
                "Category": category,
                "Cost": cost,
                "Inventory": qty
            }
        }
        self.collection.update_one(query, new_values)

    def RemoveProduct(self, product_id):
        """This function removes one product from the DB."""
        query = {"_id": ObjectId(product_id)}
        self.collection.delete_one(query)


productModule = ProductModule()
