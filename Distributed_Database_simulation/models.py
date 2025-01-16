import re

class User:
    _existing_emails = set()  # Add this to track unique emails

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.validate()

    def validate(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Invalid user ID: {self.id}")
        if not self.name or not isinstance(self.name, str) or self.name.isspace():
            raise ValueError(f"Invalid name: {self.name}")
        if self.email in User._existing_emails:
            raise ValueError(f"Duplicate email: {self.email}")
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(self.email)):
            raise ValueError(f"Invalid email format: {self.email}")
        User._existing_emails.add(self.email)

class Product:
    _existing_names = set()  # Class variable to track unique names

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = float(price)
        self.validate()

    def validate(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Invalid product ID")
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid name")
        if self.name in Product._existing_names:
            raise ValueError(f"Product name '{self.name}' already exists")
        Product._existing_names.add(self.name)
        if self.price < 0:
            raise ValueError("Price cannot be negative")

class Order:
    def __init__(self, id, user_id, product_id, quantity):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.validate()

    def validate(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Invalid order ID")
        if not isinstance(self.user_id, int) or self.user_id <= 0:
            raise ValueError("Invalid user ID")
        if not isinstance(self.product_id, int) or self.product_id <= 0:
            raise ValueError("Invalid product ID")
        if not isinstance(self.quantity, int) or self.quantity <= 0:
            raise ValueError("Invalid quantity")
