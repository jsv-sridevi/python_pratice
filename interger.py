#checking whether given number is which type of integer
integer=int(input("enter the number"))
if integer<0:
    print(f"{integer}is negative integer")
elif integer>0:
    print(f"{integer} is postive integer")
else:
    print(f"{integer} is neither positive nor negative integer")
    