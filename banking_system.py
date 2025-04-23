import uuid
balance=0
users={}

def menu():
    print("1.create a account")
    print("2.login")
    print("3.exit")
def get_choice():
    while True:#until program ends the loop runs
        choice =input("enter your choice(1-3:")#here we have to give input for choice
        if choice in ("1","2","3"):#if choice input is betwwen 1-4 than if condition becomes to true and moves to true block code
           return choice#here returns the value of choice to choice variable
        else:#here if choice input is false 
            print("enter valid input the input must be between 1-3")#print statemne tfor else block
def generate_user_id():
    """Generates a unique user ID."""
    return str(uuid.uuid4())
class account:#here it is a base class    
    def __init__(self,user_id, user_name, password):#Initializes a new user with a unique user_id, username,password
        self.user_id=user_id
        self._user_name=user_name
        self._password=password
        self.balance=0
    def credit(self,amount):
            global balance
            if amount>0:
                balance+=amount
                print(f"amount that should be credit:₹{amount}")
                print(f"balance amount:₹{balance}")   
            else:
                print("invalid input so amount is credited")
    def debit(self,amount):
            global balance
            if amount<balance:
                balance-=amount
                print(f"amount that should be debited:₹{amount}")
                print(f"balance amount:₹{balance}")   
            else:
                print("invalid input so amount is debited")
    def account_balance(self):
            print(f"avaible balance:₹{balance}")
class banking_system:
    def create(self):
        user_name=input("create username:")
        password=input("create password")
        if user_name in users:
            print("Username already exists. Please choose a different one.")
            return
        confirm_password = input("Confirm password ")
        if password == confirm_password:
            user_id = generate_user_id()
            new_user = account(user_id, user_name, password) # We still store the original for simplicity in this version
            users[user_name] = new_user
            print("Created account successfully!")
        else:
            print("Passwords do not match. Account creation failed.")
    def login(self):
        user_name = input("enter the use_name:").strip()
        password = input("enter your password:")
        if user_name in users:
            logged_in_user = users[user_name]  # Get the User object
            if password == logged_in_user._password:  # Compare directly with the password attribute
                print("you have login successfully")
                self.account_menu()  # Call account_menu on the BankingSystem instance
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
            choice1 =input("enter your choice(1-4):")#here we have to give input for choice
            if choice1 in ("1","2","3","4"):#if choice input is betwwen 1-4 than if condition becomes to true and moves to true block code         choice=choice1
                if choice1=='1':
                    amount_input= input("enter the amount to be credited")
                    if amount_input.isdigit():
                        amount=int(amount_input)
                        account.credit(self,amount)

                    else:
                        print(f"amount is allowed in only numerical way")
                elif choice1=='2':
                    amount_input= input("enter the amount to be debited")
                    if amount_input.isdigit():
                        amount=int(amount_input)
                        account.debit(self,amount)
                    else:
                        print(f"amount is allowed in only numerical way")
                elif choice1=='3':
                    account.account_balance(balance)
                elif choice1=='4':
                    print("thank you visiting")
                    break
            else:#here if choice input is false
                print("enter valid input the input must be between 1-4")#print statemne tfor else block
def banking_operation():
    bank=banking_system()
    print("welcome to bank")
    while True:
        menu()
        choice=get_choice()
        if choice=='1':
            bank.create()
        elif choice=='2':
            bank.login()
        elif choice =='3':
            print("thank you for visiting")
            break
banking_operation()
                
                