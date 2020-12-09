from classes import Client
import pymongo
import uuid
from pymongo import MongoClient


class ClientModule:
    def __init__(self):
        # database connection
        self.connection_string = "mongodb+srv://ultra:dundun428@ims.bnlzj.mongodb.net/inventory_MS?retryWrites=true&w" \
                                 "=majority "
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client.inventory_MS
        self.collection = self.db.customers
        

    def get_all_clients(self):
        all_clients = self.collection.find({})
        return all_clients
    # Create Clients (id, name, email, address)
    def createClient(self, name, email, address):
        """ This functions creates a customer object in the mondoDB database using pymongo."""
        # Client document to be inserted into the DB
        client_id = uuid.uuid1()
        document = {
            "Customer": {
                "CustomerID": client_id.hex,
                "CustomerName": name,
                "Email": email,
                "Address": address,
            }
        }
        # Creating a new Client document in the DB
        self.collection.insert_one(document)
        print("Client Created")

    def getClient(self, email):
        """ This function returns a customer dictionary object from the DB using their email"""
        # Client is a dictionary object
        query = {"Customer.Email": email}
        client = self.collection.find_one(query)
        return client

    def updateClient(self, id, name, email, address):
        """ This function updates a customers info on the DB. """
        query = {"Customer.CustomerID": id}
        new_values = {"$set":
                            {"Customer":
                                {
                                    "CustomerID": id,
                                    "CustomerName": name,
                                    "Email": email,
                                    "Address": address}
                            }}
        self.collection.update_one(query, new_values)

    def removeClient(self, client_id):
        """ This function removes one customer from the DB. """
        query = {"Customer.CustomerID": client_id}
        self.collection.delete_one(query)


clientModule = ClientModule()
