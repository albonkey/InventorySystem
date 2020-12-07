from classes import Client

class ClientModule():
    clients = [
        Client(1, "carl", "carl@gmail.com", "Los Angeles"),
        Client(2, "alejandro", "alejandro@gmail.com", "Los Angeles"),
        Client(3, "nicol", "nicol@gmail.com", "Los Angeles")
    ]

    #Create Clients (id, name, email, address)
    def createClient(id, name, email, address):
        clients.append(Client(id, name, email, address))


    #update clients(client id)
    #remove clients(client id)
