from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customar(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def view_menu(self, restaurant):
        restaurant.menu.show_menu()
    
    def Add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded !!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("Item Not Found")

    def view_cart(self):
        print("**View Cart**")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid Successfully")
        self.cart.clear()

class Employee(User):
    def __init__(self, name, email, phone, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employees(self, restaurant, employee):
        restaurant.add_employees(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)
    
    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

class Resturent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employees(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List !!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item] 

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted")
        else:
            print("Item Not Found")

    def show_menu(self):
        print("*****Menu*****")
        print("Name\t Price \t Quantity")
        for item in self.items:
            print(f"{item.name}\t {item.price}\t {item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

mamar_restaurant = Resturent("Mamar Restaurant")

def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customar(name, email, phone, address)
    
    while True:
        print(f"Welcome, {customer.name}!")
        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter Quantity: "))
            customer.Add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")

def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name, email, phone, address)
    
    while True:
        print(f"Welcome, {admin.name}!")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Menu")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = int(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurant, item)
        elif choice == 2:
            emp_name = input("Enter Employee Name: ")
            emp_email = input("Enter Employee Email: ")
            emp_phone = input("Enter Employee Phone: ")
            emp_address = input("Enter Employee Address: ")
            emp_age = input("Enter Employee Age: ")
            emp_designation = input("Enter Employee Designation: ")
            emp_salary = input("Enter Employee Salary: ")
            employee = Employee(emp_name, emp_email, emp_phone, emp_address, emp_age, emp_designation, emp_salary)
            admin.add_employees(mamar_restaurant, employee)
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter Item Name to Delete: ")
            admin.remove_item(mamar_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Input")

while True:
    print("1. Customer Menu")
    print("2. Admin Menu")
    print("3. Exit")
    option = int(input("Enter Your Choice: "))
    if option == 1:
        customer_menu()
    elif option == 2:
        admin_menu()
    elif option == 3:
        break
    else:
        print("Invalid Option")
