#here we are checking the person belong to which age group using if-elif-else
age=int(input("enter the age"))
if age<0:
    print("invalid age")
elif age<=12:
    print("person is child")
elif age<=17:
    print(f"person is teenager")
elif age<=64:
    print("person is adult")
else:
    print("person is senior citizen")
    