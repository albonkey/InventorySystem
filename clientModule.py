from classes import Client

class ClientModule():
    def __init__(self):
        self.clients = [
            Client(1, "carl", "carl@gmail.com", "Los Angeles"),
            Client(2, "alejandro", "alejandro@gmail.com", "Los Angeles"),
            Client(3, "nicol", "nicol@gmail.com", "Los Angeles")
        ]

    #Connect database here. And make the functions update the database

    #Create Clients (id, name, email, address)
    def createClient(self,id, name, email, address):
        self.clients.append(Client(id, name, email, address))


    def getClients(self):
        return self.clients

    def updateClient(self, id, name, email, address):
        return null

    def removieClient(self, client_id):
        return nulll


clientModule = ClientModule()
