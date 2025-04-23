#multiplication table using for loop
table=int(input("enter the number of tables"))
multiples=int(input("how many multiples"))
for i in range (1,table+1):
    for j in range(1,multiples+1):
        print(f"{i}x{j}={i*j}")
    print('-'*10)