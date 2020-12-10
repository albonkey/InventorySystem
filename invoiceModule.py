from classes import Invoice
import pymongo
from bson.objectid import ObjectId
from classes import Product


class InvoiceModule:
    def __init__(self):
        self.connection_string = "mongodb+srv://ultra:dundun428@ims.bnlzj.mongodb.net/inventory_MS?retryWrites=true&w" \
                                 "=majority"
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client.inventory_MS
        self.collection = self.db.invoice
        self.collection_invoice_product = self.db.invoice_product

        self.createInvoice("5fd147a2b278696ba898e9a8", "Title", "Description", "20.Des", 50, [{
            "ProductName": "Product X",
            "Description": "Coool",
            "Category": "Toy",
            "Cost": 50
        },
        {
            "ProductName": "Product Y",
            "Description": "Coool",
            "Category": "Toy",
            "Cost": 70
        },
        {
            "ProductName": "Product Z",
            "Description": "Coool",
            "Category": "Toy",
            "Cost": 60
        }])

    # id_counter:
    def getAllInvoices(self):
        """This function returns all invoices in the DB"""
        all_invoices = self.collection.find({})
        return all_invoices

    def getInvoices(self, client_id):
        """This function returns invoices pertaining to a client"""
        query = {"_id": ObjectId(client_id)}
        invoice = self.collection.find(query)
        return invoice

    def getUnpaidInvoices(self):
        """This function returns all UNPAID invoices from the DB"""
        query = {"IsPaid": 0}
        invoices = self.collection.find(query)
        return invoices

    def getPaidInvoices(self):
        """This function returns all PAID invoices from the DB"""
        query = {"IsPaid": 1}
        invoices = self.collection.find(query)
        return invoices

    def createInvoice(self, client_id, title, description, dueDate, cost, list):
        """This function creates a new invoices object """
        invoice = {
            "Title": title,
            "ClientID": client_id,
            "InvoiceDescription": description,
            "DueDate": dueDate,
            "IsPaid": 0,  # default IsPaid to be not paid (0)
            "TotalCost": cost,
        }
        _id = self.collection.insert_one(invoice)
        self.addProductInvoice(_id.inserted_id, list)

    def addProductInvoice(self, invoice_id, productList):

        for product in productList:
            product = {
                "InvoiceID": invoice_id,
                "ProductName": product["ProductName"],
                "Description": product["Description"],
                "Category": product["Category"],
                "Cost": product["Cost"],  # default IsPaid to be not paid (0)
                "Quantity": 1
            }
            self.collection_invoice_product.insert_one(product)


    def payInvoice(self, invoice_id):
        """This function set the {IsPaid} attribute in the DB from a specific invoice"""
        query = {"_id": ObjectId(invoice_id)}
        update_query = {"$set":
            {
            "IsPaid": 1
            }
        }
        self.collection.update_one(query, update_query)

    def updateInvoice(self, invoice_id, client_id, title, description, dueDate, isPaid, cost):
        """This function updates an invoice on the database"""
        query = {"_id": ObjectId(invoice_id)}
        new_values = {"$set":
            {
                "Title": title,
                "ClientID": client_id,
                "InvoiceDescription": description,
                "DueDate": dueDate,
                "IsPaid": isPaid,
                "TotalCost": cost,
            }
        }
        self.collection.update_one(query, new_values)

    def removeInvoice(self, invoice_id):
        """ This function removes one invoice from the DB. """
        query = {"_id": ObjectId(invoice_id)}
        self.collection.delete_one(query)


invoiceModule = InvoiceModule()
