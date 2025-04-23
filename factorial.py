#factorial of number
fact=1
def factorial(number_n):
    global fact
    if number_n>0:
        for i in range (1,number_n+1):
            fact *=i
            i+1
    elif number==0:
        fact=1        
    else:
        print("factorial is not calculate for negative number")
number=int(input("enter the number for factorial:"))
factorial(number)
result=int(fact)
print(f"factorial of {number } is factorial {result}")

    
    