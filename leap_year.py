#here we are checking whether the is leap year or not
year=int(input("enter year"))
#here we are nested form if-elif-else
if year%4==0:
    if year%100==0: #nested if for 1st if condition
        if year%400==0: #nested if for 2nd if condition
            print(f"{year} is a leap year")
        else:#this alternative block statement for 3rd if condition
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")