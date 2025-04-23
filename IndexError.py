#here we trying index error
list_1=['1','2','2','3']
try:
    index=int(input("enter the index of element you want:"))
    result=list_1[index]
except IndexError as e:
    print(f"IndexError:{e}")
else:
    print(result)