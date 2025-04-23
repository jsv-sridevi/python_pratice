#here we are using TypeError
#1st format
try:
    list_1=list(input("enter the list of numbers"))
    index='1'#here index must be integer but we gave string it is a type error
    index=1 #its correct
    print(list_1[index])
except TypeError as e:
    print(f"TypeError: {e}")
else:
    print(list_1)
#2nd format
try:
    name=input("enter your name")
    age=int(input("enter you age"))
    print(name+age)#here we cant do concatenation for str and int we can do for str and str
    #print((name)+str(age)) #correct format
except TypeError as e:
    print(f"TypeError: {e}")
else:
    print("successfully executed")