from classes import Invoice
from classes import Product

class Invoices():
    invoices = [
        Invoice(1, "Carl", "Alejandro", "Socks", "Bought 1 pair of socks. ",
            [Product(1, "Socks", "Put them on your feet", "Clothes", 50, 10)],
            "01/01/2020")
    ];
    #id_counter:
    #Create Invoice (id, user, client, title, description, products [], dueDate){}
    #update invoice(invoice id)
    #remove invoice(invoice id)

    #Invocies.addInvoice(user, client, title, description, products [], dueDate)
