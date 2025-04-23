#here we are creating a atm using inheritance
balance=0
#using functions create a atm project
def menu():#here we defining a function called menu which have set print statements for choice
    print("1.credit")
    print("2.debit")
    print("3.balance")
    print("4.exit")
def get_choice():#here e have to choose the above print statement numbers for performing a operation
    while True:#until program ends the loop runs
        choice =input("enter your choice(1-4):")#here we have to give input for choice
        if choice in ("1","2","3","4"):#if choice input is betwwen 1-4 than if condition becomes to true and moves to true block code
           return choice#here returns the value of choice to choice variable
        else:#here if choice input is false 
            print("enter valid input the input must be between 1-4")#print statemne tfor else block
class bank_info:#class defining
    def __init__(self,bank_name,location):#here we defining init method is know as special function used to for initializing attributes
        self.bank_name=bank_name
        self.location=location
    def bankdetials(self):
        def bankname():
            print(f"ATM of {self.bank_name}")
        def banklocation():
            print(f"{self.bank} is located at{self.location}")
class Account(bank_info):
    def __init__(self,account_no,bank_name,location):
        self.account_no=account_no
        bank_info.__init__(self, bank_name, location)
        
    def credit(self):
            global balance
            amount_input= input("enter the amount to be credited")
            if amount_input.isdigit():
                amount=int(amount_input)
                if amount>0:
                    balance+=amount
                    print(f"amount that should be credit:₹{amount}")
                    print(f"balance amount:₹{balance}")   
                else:
                    print("invalid input so amount is credited")
            else:
                print(f"amount is allowed in only numerical way")
    def debit(self):
            global balance
            amount_input= input("enter the amount to be debited")
            if amount_input.isdigit():
                amount=int(amount_input)
                if amount<balance:
                    balance-=amount
                    print(f"amount that should be debited:₹{amount}")
                    print(f"balance amount:₹{balance}")   
                else:
                    print("invalid input so amount is debited")
            else:
                print(f"amount is allowed in only numerical way")
    def account_balance(self):
            print(f"avaible balance:₹{balance}")
def atm_operation():
    print("welcome to ATM")
    accounts = {1234: ("sbi", "seethamadra"), 4567: ("sbi", "dwarakanagar"), 3333: ("central_bank", "dwarakanagar")}
    logged_in_account = None  # object to store the logged-in the account class data
    while True:
        account_no_str = input("Enter the account number of account holder: ")
        bank_name = input("Enter the name of the bank: ").lower()
        location = input("Enter the location of the bank: ").lower()

        if account_no_str.isdigit():
            account_no = int(account_no_str)
            if account_no in accounts:
                account_data = accounts[account_no]  # Store the tuple directly
                if bank_name.lower() == account_data[0].lower() and location.lower() == account_data[1].lower():
                    print(f"Welcome, Account Number: {account_no} from {account_data[0]} ({account_data[1]})")
                    # Create an instance of the Account class for the logged-in user
                    logged_in_account = Account(account_no, account_data[0], account_data[1])
                    while True:
                        menu()
                        choice = get_choice()
                        
                        if choice == "1":
                            logged_in_account.credit()
                        elif choice == "2":
                            logged_in_account.debit()
                        elif choice == "3":
                            logged_in_account.account_balance()
                        elif choice == "4":
                            print("Thank you for visiting ATM")
                            break
                    break  # Exit the outer loop after successful ATM session
                else:
                    print("Invalid bank name or location for this account number. Please check the details.")
            else:
                print("Invalid account number. Please check your account number.")
        else:
            print("Invalid account number format. Please enter digits only.")

atm_operation()



        