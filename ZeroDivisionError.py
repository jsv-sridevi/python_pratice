#here we are using zero divsion error class
try:
    number_1=int(input("enter the 1st number"))
    number_2=int(input("enter the 2nd number"))
    result=number_1/number_2
except ValueError as e:
    print(f"the given value is not an integer {e}")
except ZeroDivisionError as e:
    print(f"divisble by zero")
else:
    print(result)