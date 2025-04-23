#here finding the prime numbers
def prime(number):
    if number>1:
        for i in range(2,int(number**0.5)+1):
            #number**0.5 it is optimization techinic for large numbers 
            #if it have a square than it not prime number
            if number%i==0:
                return False
            else:
                return True
        else:
            return True
    elif number==0:
        print("zero is not a prime number")
    else:
        print("negative number or not prime numbers")

num=int(input("enter the number"))
prime(num)
print(prime(num))
                