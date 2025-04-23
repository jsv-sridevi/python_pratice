#using pass statement in conditional statement
for i in range(1,10):#here we are aking range of number 1 to 10
    if i%2==0:#here if the reminder is 0 than it is even number  if it is even number we go into true block statement
        print(f"{i} is even")
    else:#here else block for if block statement when given condition is false of if statementtha it comes to else
        pass
print(i)#here it prints the last iterated value of i