import json
from getpass import getpass

# Define the Product class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_product(self, name=None, category=None, price=None, stock_quantity=None):
        if name:
            self.name = name
        if category:
            self.category = category
        if price:
            self.price = price
        if stock_quantity:
            self.stock_quantity = stock_quantity

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock_quantity": self.stock_quantity
        }

    @staticmethod
    def from_dict(data):
        return Product(data["product_id"], data["name"], data["category"], data["price"], data["stock_quantity"])

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

# Define the User class
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # "Admin" or "User"

    def to_dict(self):
        return {"username": self.username, "password": self.password, "role": self.role}

    @staticmethod
    def from_dict(data):
        return User(data["username"], data["password"], data["role"])

# User Management with default admin check
class UserManager:
    FILE_NAME = "user_data.json"

    def __init__(self):
        self.users = {}
        self.load_users()
        if not self.users:
            self.add_user("admin", "admin123", "Admin")
            print("Default admin account created with username 'admin' and password 'admin123'.")

    def add_user(self, username, password, role):
        if username in self.users:
            print("Username already exists. Choose a different username.")
            return False
        self.users[username] = User(username, password, role)
        self.save_users()
        print(f"User '{username}' registered successfully as '{role}'.")
        return True

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def save_users(self):
        with open(self.FILE_NAME, 'w') as file:
            json.dump({username: user.to_dict() for username, user in self.users.items()}, file)
        print("User data saved to file.")

    def load_users(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                data = json.load(file)
                self.users = {username: User.from_dict(user_data) for username, user_data in data.items()}
            print("User data loaded from file.")
        except FileNotFoundError:
            print("No saved user data found. Starting fresh.")

# Define the Inventory class
class Inventory:
    FILE_NAME = "inventory_data.json"

    def __init__(self):
        self.products = {}
        self.load_products()

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added successfully.")
            self.save_products()

    def edit_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if product:
            product.update_product(**kwargs)
            print(f"Product '{product_id}' updated successfully.")
            self.save_products()
        else:
            print("Product not found.")

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            print(f"Product '{product_id}' deleted successfully.")
            self.save_products()
        else:
            print("Product not found.")

    def view_inventory(self):
        if not self.products:
            print("No products in inventory.")
        for product in self.products.values():
            print(product)

    def search_by_name_or_category(self, query):
        results = [product for product in self.products.values() if query.lower() in product.name.lower() or query.lower() in product.category.lower()]
        if results:
            for product in results:
                print(product)
        else:
            print("No matching products found.")

    def filter_by_stock_level(self, threshold):
        for product in self.products.values():
            if product.stock_quantity <= threshold:
                print(f"Low stock alert: {product}")

    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.stock_quantity += quantity
            print(f"Stock for '{product.name}' updated. New quantity: {product.stock_quantity}")
            self.save_products()
        else:
            print("Product not found.")

    def save_products(self):
        with open(self.FILE_NAME, 'w') as file:
            json.dump({pid: product.to_dict() for pid, product in self.products.items()}, file)
        print("Products saved to file.")

    def load_products(self):
        try:
            with open(self.FILE_NAME, 'r') as file:
                data = json.load(file)
                self.products = {pid: Product.from_dict(prod_data) for pid, prod_data in data.items()}
            print("Products loaded from file.")
        except FileNotFoundError:
            print("No saved inventory found. Starting fresh.")

# Inventory Management System Class
class InventoryManagementSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.inventory = Inventory()

    def register_user(self):
        print("\n--- User Registration ---")
        username = input("Enter new username: ")
        password = getpass("Enter new password: ")
        role = input("Enter role ('Admin' or 'User'): ")
        if role not in ["Admin", "User"]:
            print("Invalid role. Must be 'Admin' or 'User'.")
            return
        self.user_manager.add_user(username, password, role)

    def main_menu(self, user):
        while True:
            print("\n--- Inventory Management System ---")
            print("1. View Products")
            if user.role == "Admin":
                print("2. Add Product")
                print("3. Edit Product")
                print("4. Delete Product")
                print("5. Adjust Stock")
            print("0. Logout")

            choice = input("Select an option: ")

            if choice == "1":
                self.inventory.view_inventory()
            elif choice == "2" and user.role == "Admin":
                self.add_product()
            elif choice == "3" and user.role == "Admin":
                self.edit_product()
            elif choice == "4" and user.role == "Admin":
                self.delete_product()
            elif choice == "5" and user.role == "Admin":
                self.adjust_stock()
            elif choice == "0":
                print("Logging out...")
                break
            else:
                print("Invalid option or permission denied.")

    def add_product(self):
        try:
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            category = input("Enter Product Category: ")
            price = float(input("Enter Product Price: "))
            stock_quantity = int(input("Enter Stock Quantity: "))
            product = Product(product_id, name, category, price, stock_quantity)
            self.inventory.add_product(product)
        except ValueError:
            print("Invalid input. Please enter the correct data type for price and stock quantity.")

    def edit_product(self):
        try:
            product_id = input("Enter Product ID to edit: ")
            name = input("Enter new Product Name (or press Enter to keep current): ")
            category = input("Enter new Product Category (or press Enter to keep current): ")
            price = input("Enter new Product Price (or press Enter to keep current): ")
            stock_quantity = input("Enter new Stock Quantity (or press Enter to keep current): ")
            kwargs = {
                "name": name if name else None,
                "category": category if category else None,
                "price": float(price) if price else None,
                "stock_quantity": int(stock_quantity) if stock_quantity else None
            }
            self.inventory.edit_product(product_id, **{k: v for k, v in kwargs.items() if v is not None})
        except ValueError:
            print("Invalid input. Please enter valid values.")

    def delete_product(self):
        product_id = input("Enter Product ID to delete: ")
        self.inventory.delete_product(product_id)

    def adjust_stock(self):
        try:
            product_id = input("Enter Product ID to adjust stock: ")
            quantity = int(input("Enter quantity to adjust (+ for restock, - for sale): "))
            self.inventory.adjust_stock(product_id, quantity)
        except ValueError:
            print("Invalid input. Quantity must be an integer.")

def main():
    system = InventoryManagementSystem()

    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Register")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            user = system.user_manager.authenticate(username, password)
            if user:
                system.main_menu(user)
            else:
                print("Invalid credentials. Access denied.")
        elif choice == "2":
            system.register_user()
        elif choice == "0":
            print("Exiting the system...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
