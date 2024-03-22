class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.food_items = []

    def login(self, username, password):
        return self.username == username and self.password == password

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                break

    def view_food_items(self):
        for food_item in self.food_items:
            print(f"Food ID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: {food_item.price}")
            print(f"Discount: {food_item.discount}")
            print(f"Stock: {food_item.stock}")
            print("------------------")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                break


class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def register(self):
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email address: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter a password: ")
        print("Registration Successful!")

    def login(self, email, password):
        print("==== User Login ====")
        if email == self.email and password == self.password:
            print("Login Successful!")
            # Perform further actions after successful login
        else:
            print("Invalid credentials. Login Failed.")

    def update_profile(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

    def place_new_order(self):
        print("==== Place New Order ====")
        # Show list of food items
        print("Available Food Items:")
        for index, food_item in enumerate(self.food_menu, start=1):
            print(f"{index}. {food_item['name']} ({food_item['quantity']}) [INR {food_item['price']}]")

        # Get user input for selected food items
        selection = input("Enter the numbers of the food items you want to order (comma-separated): ")
        selected_items = []
        try:
            selected_indices = [int(item) - 1 for item in selection.split(",")]
            selected_items = [self.food_menu[index] for index in selected_indices if 0 <= index < len(self.food_menu)]
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        # Display selected food items
        print("Selected Food Items:")
        for item in selected_items:
            print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")

        # Place the order
        confirmation = input("Do you want to place this order? (yes/no): ")
        if confirmation.lower() == "yes":
            # Implement logic to place the order
            print("Order placed successfully!")
        else:
            print("Order cancelled.")

    def order_history(self):
        print("==== Order History ====")
        if self.orders:
            for order in self.orders:
                print(f"Order ID: {order['order_id']}")
                print("Food Items:")
                for item in order['items']:
                    print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
                print(f"Total Amount: INR {order['total_amount']}")
                print("==============")
        else:
            print("No order history found.")


# Usage Example

# Admin functionalities
admin = Admin("admin", "admin123")
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 2)

# User functionalities
user = User("John Doe", "1234567890", "john@example.com", "123 Main St", "password")
user.update_profile("John Doe", "9876543210", "john.doe@example.com", "456 Park Ave", "newpassword")

# Print the list of food items for the admin
admin.view_food_items()