class Book: 
    def __init__(self, name) -> None:
        self.name = name
    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name) 
    def read(self):
        print('reading physics vector chapter')

topon = Physics('topon', True)

print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read()









# Practice Task


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to the shop.")

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                if product.quantity > 0:
                    product.quantity -= 1
                    print(f"Congratulations! You have successfully bought '{product.name}'.")
                else:
                    print(f"Sorry, '{product.name}' is out of stock.")
                return
        print(f"Sorry, '{product_name}' is not available in the shop.")

# Usage example:

# Create some products
product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Tablet", 300, 3)

# Create a shop and add products to it
shop = Shop()
shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

# Try to buy products
shop.buy_product("Laptop")
shop.buy_product("Phone")
shop.buy_product("Tablet")
shop.buy_product("Desktop")  # Product not available
