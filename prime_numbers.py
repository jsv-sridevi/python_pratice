#Write a program to display all prime numbers within a range
num_1=int(input("enter the starting number"))
num_2=int(input("enter the ending number"))
for number in range(num_1,num_2 +1):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(f"{number}is prime number")
#for 2 forloop is not executed beacuse range(2,2) means there is no number exist
