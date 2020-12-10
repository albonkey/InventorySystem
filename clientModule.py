from classes import Client
import pymongo
from bson.objectid import ObjectId
import uuid
from pymongo import MongoClient


class ClientModule:
    def __init__(self):
        # database connection
        self.connection_string = "mongodb+srv://ultra:dundun428@ims.bnlzj.mongodb.net/inventory_MS?retryWrites=true&w" \
                                 "=majority"
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client.inventory_MS
        self.collection = self.db.customers
        self.updateClient("5fd147f06c11628f7a24d78e", "Carl123", "Carl123", "Carl123")


    def get_all_clients(self):
        all_clients = self.collection.find({})
        return all_clients
    # Create Clients (id, name, email, address)
    def createClient(self, name, email, address):
        #This functions creates a customer object in the mondoDB database using pymongo.
        # Client document to be inserted into the DB

        customer = {
            "CustomerName": name,
            "Email": email,
            "Address": address,
        }
        # Creating a new Client document in the DB
        _id = self.collection.insert_one(customer)
        print("--------")
        print(_id.inserted_id)

    def getClient(self, email):
        """ This function returns a customer dictionary object from the DB using their email"""
        # Client is a dictionary object
        query = {"Email": email}
        client = self.collection.find_one(query)
        return client

    def updateClient(self, id, name, email, address):
        """ This function updates a customers info on the DB. """
        query = {"_id": ObjectId(id)}
        new_values = {"$set":
                                {
                                    "CustomerName": name,
                                    "Email": email,
                                    "Address": address}
                            }
        self.collection.update_one(query, new_values)

    def removeClient(self, client_id):
        """ This function removes one customer from the DB. """
        query = {"Customer.CustomerID": client_id}
        self.collection.delete_one(query)


clientModule = ClientModule()
