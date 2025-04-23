import uuid

users = {}

def menu():
    print("1.create a account")
    print("2.login")
    print("3.exit")

def get_choice():
    while True:
        choice = input("enter your choice(1-3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        else:
            print("enter valid input the input must be between 1-3")

def generate_user_id():
    return str(uuid.uuid4())

class User:
    def __init__(self, user_id, user_name, password):
        self.user_id = user_id
        self._user_name = user_name
        self._password = password
        self.balance = 0

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Credited ₹{amount}. Current balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def debit(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Debited ₹{amount}. Current balance: ₹{self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def account_balance(self):
        print(f"Available balance: ₹{self.balance}")

class banking_system:
    def __init__(self):
        pass

    def create(self):
        user_name = input("create username:")
        password = input("create password")
        if user_name in users:
            print("Username already exists. Please choose a different one.")
            return
        confirm_password = input("Confirm password ")
        if password == confirm_password:
            user_id = generate_user_id()
            new_user = User(user_id, user_name, password)
            users[user_name] = new_user
            print("Created account successfully!")
        else:
            print("Passwords do not match. Account creation failed.")

    def login(self):
        user_name = input("enter the use_name:").strip()
        password = input("enter your password:")
        if user_name in users:
            logged_in_user = users[user_name]
            if password == logged_in_user._password:
                print("you have login successfully")
                current_user = logged_in_user  # Set the current_user upon successful login
                self.account_menu()
            else:
                print("incorrect password")
        else:
            print("user not found")

    def account_menu(self):
        while True:
                print("\nUser Menu:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. View Balance")
                print("4. Logout")
                choice1 = input("enter your choice(1-4): ")
                if choice1 in ("1", "2", "3", "4"):
                    if choice1 == '1':
                        amount_input = input("enter the amount to be credited: ")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            user.credit(amount)
                        else:
                            print("Invalid input. Please enter a numerical amount.")
                    elif choice1 == '2':
                        amount_input = input("enter the amount to be debited: ")
                        if amount_input.isdigit():
                            amount = int(amount_input)
                            user.debit(amount)
                        else:
                            print("Invalid input. Please enter a numerical amount.")
                    elif choice1 == '3':
                        user.account_balance()
                    elif choice1 == '4':
                        print("thank you visiting")
                        break
                else:
                    print("enter valid input the input must be between 1-4")
        else:
            print("No user logged in. Please log in first.")

def banking_operation():
    bank = banking_system()
    print("welcome to bank")
    while True:
        menu()
        choice = get_choice()
        if choice == '1':
            bank.create()
        elif choice == '2':
            bank.login()
        elif choice == '3':
            print("thank you for visiting")
            break
banking_operation()