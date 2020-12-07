from classes import Invoice
from classes import Product

class InvoiceModule():
    invoice_id = 2;
    invoices = [
        Invoice(1, "Carl", "Alejandro", "Socks", "Bought 1 pair of socks.", "22.Januar")
    ]
    #id_counter:
    #Create Invoice (id, user, client, title, description, products [], dueDate){}
    def createInvoice(user_id, client_id, title, description, dueDate):
        invoices.add(Invoice(++self.invoice_id, user_id, client_id, title, description, dueDate))

    #update invoice(invoice id)
    #remove invoice(invoice id)

    #Invocies.addInvoice(user, client, title, description, products [], dueDate)
