#here we are using key error class
dict_1={}
try:
    length=int(input("enter the number of key value pairs:"))
    for i in range(length):
        key=input("enter the key element")
        value=input("enter the value of key element")
        dict_1[key]=value
    try:    
        key=input("enter the key you want check")
        given_key=dict_1[key]    
        print(f"{key} is exist ")
    except KeyError as e:
        print(f"key is not exist {e}")
    else:
        print(f"the value of given key is {value}")
except ValueError as a:
    print(f"ValueError:{a}")