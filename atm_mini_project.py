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
balance=1000#it is global variable 
def credit():#here we are defining function called credit for crediting the amount
    global balance#here we are using balance global variable to modify
    amount_input=input("enter amount to be credited")#here amount input value is taken
    if amount_input.isdigit():#here if amoun value is in digit than moves to true block statement
        amount=int(amount_input)#here amount is digit than it converted into int
        if amount>=0:#here if amount is greater than 0 than moves to true block
            balance+=amount#here amount is added to balance and balance is getting incremented
            print(f"amount that should be credit:₹{amount}")
            print(f"balance amount:₹{balance}")
        else:
            print("invalid amount")
    else:
        print(f"amount is allowed in only numerical way")
def debit():
    global balance
    amount_input=input("enter amount to be debited")
    if amount_input.isdigit():
        amount=int(amount_input)
        if amount>=0:
            balance-=amount
            print(f" enter the amount to be debited is₹{amount} ")
            print(f"balance amount is₹{balance}")
        else:
            print("invalid amount")
    else:
        print(f"amount is allowed in only numerical way")
def account_balance():
    print(f"avaible balance:₹{balance}")
def atm_operation():
    print("welcome to ATM")
    while True:
        menu()
        choice= get_choice()#here we are defining the get_choice function to choice variable
        if choice=="1":
            credit()
        elif choice=="2":
            debit()
        elif choice=="3":
            account_balance()
        elif choice=="4":
            print("Thank you for visiting ATM")
            break
atm_operation()