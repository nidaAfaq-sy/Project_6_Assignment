class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative.")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
product = Product(100)
print(product.price)  # Get the price

product.price = 150  # Set a new price
print(product.price)

product.price = -50  # Try setting a negative price

del product.price  # Delete the price

