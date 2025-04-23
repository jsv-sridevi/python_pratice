#here we have to filter only positive number from list 
result=filter(lambda i:i>0,[-1,-2,0,1,2,3,4,5,6])#here it filter according to condition  if it is true than it returns true values
print(list(result))#if we dont do type conversion it prints object