#printing odd number using continue in for loop
for i in range(1,601):#here we taking range from 1 to 601 so it take up to 600
    if i%2==0:#here if the reminder is 0 than it is even number  if it is even number we go into true block statement
       continue# here even numbers are skipped 
    print(i)#here the unskipped values are printed
print(i)#here last iterated value is printed
