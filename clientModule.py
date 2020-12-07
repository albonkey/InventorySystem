from classes import Client

class ClientModule():
    def __init__(self):
        self.clients = [
            Client(1, "carl", "carl@gmail.com", "Los Angeles"),
            Client(2, "alejandro", "alejandro@gmail.com", "Los Angeles"),
            Client(3, "nicol", "nicol@gmail.com", "Los Angeles")
        ]

    #Create Clients (id, name, email, address)
    def createClient(self,id, name, email, address):
        self.clients.append(Client(id, name, email, address))


    def getClients(self):
        return self.clients

    #update clients(client id)
    #remove clients(client id)

clientModule = ClientModule()
