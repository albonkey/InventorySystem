from classes import Invoice
from classes import Product

class InvoiceModule():
    def __init__(self):
        self.invoices = [
                Invoice(1, "Carl", "Alejandro", "Socks", "Bought 1 pair of socks.", "22.Januar")
            ]

    #id_counter:
    def getInvoices(self):
        return self.invoices

    #Create Invoice (id, user, client, title, description, products [], dueDate){}
    def createInvoice(self, user_id, client_id, title, description, dueDate):
        self.invoices.append(Invoice(1, user_id, client_id, title, description, dueDate))



    def updateInvoice(self, id, user_id, client_id, title, description, dueDate):
        return null

    def removeInvoice(self, id):
        return null 
    #update invoice(invoice id)
    #remove invoice(invoice id)

    #Invocies.addInvoice(user, client, title, description, products [], dueDate)

invoiceModule = InvoiceModule()
