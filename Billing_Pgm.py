import datetime

class BillingSystem:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, name, price, quantity):
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)
        self.total += price * quantity

    def generate_invoice(self):
        invoice = "Invoice\n"
        invoice += "-" * 20 + "\n"
        invoice += "Date: {}\n".format(datetime.date.today())
        invoice += "\nItem\t\tPrice\tQuantity\tTotal\n"
        invoice += "-" * 40 + "\n"

        for item in self.items:
            line_total = item["price"] * item["quantity"]
            invoice += "{}\t{:.2f}\t{}\t\t{:.2f}\n".format(
                item["name"], item["price"], item["quantity"], line_total
            )

        invoice += "\nTotal: {:.2f}".format(self.total)
        return invoice

# Example usage
billing_system = BillingSystem()
billing_system.add_item("Product A", 9.99, 2)
billing_system.add_item("Product B", 14.99, 1)
billing_system.add_item("Product C", 4.99, 3)

print(billing_system.generate_invoice())