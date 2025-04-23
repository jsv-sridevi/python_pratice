#fibinacci series
def fibinacci(num):
    if num>3:
        a,b=0,1
        for i in range(2,num+1):
            next_fibinacci=a+b
            a=b#here changing value of  a by assiging  b value
            b = next_fibinacci #here b value is changed by assigning value of variable next_fibinocci
        return b
    elif num==1:
        return 0
    elif num==2:
        return 1
number= int(input("enter the number for fibinacci"))
fibinacci(number)
print(f"fibinacci of {number} is {fibinacci(number)}")