# Task: Online Shopping System

# Create a Python program to model an online shopping system. You should define the following classes:

# Product: This class represents a generic product and should have the following attributes:

# name: Name of the product
# price: Price of the product
# ElectronicProduct: This class should inherit from Product and add an additional attribute:

# warranty_period: Warranty period of the electronic product in months
# ClothingProduct: This class should also inherit from Product and add additional attributes:

# size: Size of the clothing product (e.g., small, medium, large)
# color: Color of the clothing product
# Customer: This class represents a customer of the online shopping system and should have the following attributes:

# name: Name of the customer
# email: Email address of the customer
# It should also have methods to:

# Add products to the customer's shopping cart
# Remove products from the customer's shopping cart
# Checkout (purchase) the products in the shopping cart
# Your program should allow the following operations:

# Add new products (both electronic and clothing) to the online shopping system.
# Add new customers to the system.
# Allow customers to browse products and add them to their shopping cart.
# Allow customers to remove products from their shopping cart.
# Allow customers to checkout and purchase the products in their shopping cart.



# Creating Product Class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period


class ClothingProduct(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)
        self.size = size
        self.color = color


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = []

    def add_to_cart(self, product):
        self.shopping_cart.append(product)
        print(f"{product.name} added to cart.")

    def remove_from_cart(self, product):
        if product in self.shopping_cart:
            self.shopping_cart.remove(product)
            print(f"{product.name} removed from cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def checkout(self):
        if not self.shopping_cart:
            print("Your shopping cart is empty.")
            return

        total_price = sum(product.price for product in self.shopping_cart)
        print("Your shopping cart:")
        for product in self.shopping_cart:
            print("-", product)
        print(f"Total price: ${total_price:.2f}")

        confirm = input("Would you like to proceed with the purchase? (yes/no): ")
        if confirm.lower() == 'yes':
            print("Thank you for your purchase!")
            self.shopping_cart = []  # Empty the shopping cart after purchase
        else:
            print("Purchase canceled.")


# Create some products
iphone = ElectronicProduct("iPhone 12", 999.99, 12)
tshirt = ClothingProduct("T-Shirt", 19.99, "Medium", "Blue")
laptop = ElectronicProduct("Laptop", 1299.99, 24)

# Create a customer
customer1 = Customer("John Doe", "john@example.com")

# Add products to the customer's shopping cart
customer1.add_to_cart(iphone)
customer1.add_to_cart(tshirt)
customer1.add_to_cart(laptop)

# Remove a product from the shopping cart
customer1.remove_from_cart(iphone)

# Checkout
customer1.checkout()
