#build simple calculator using if condition
num_1=int(input("enter first value:"))
num_2=int(input("enter second value:"))
opr=input("enter operator :")
operator=('+','-','*','/')
if opr in operator:
    if opr=='+':
        sum=num_1+num_2
        print(f"the first value is{ num_1} and second value is {num_2} its sum is {sum}")
    elif opr=='-':
        difference=num_1-num_2
        print(f"the first value is{ num_1} and second value is {num_2} its difference is {difference}")
    elif opr=='*':
        multiplication=num_1*num_2
        print(f"the first value is{ num_1} and second value is {num_2} its multiplication is {multiplication}")
    elif opr=='/'and num_2!=0: 
        division=num_1/num_2
        print(f"the first value is{ num_1} and second value is {num_2} its divison is {division}")
else:
    print("given operator is invalid")