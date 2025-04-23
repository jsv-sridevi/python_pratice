#here we are calculating factor using reduce
n=int(input("enter the number which you want get factorial"))
from functools import reduce
result=reduce(lambda i,j:i*j,range(1,n+1))
print(result)