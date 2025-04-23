# here sum all numbers are do if it exceeds we need to break
sum=0#inital we are declaring sum is zero
numbers=[25,30,20,40,15,25] 
index=0 #here index is we give numbering to values
while index<len(numbers):#here we are saying index number is less length numbers
    #by using combine operator we are doing addition and assign the value to same variable
    #here number[index] means in numbers list that index numbered value is entered in that place
    #example numbers[1]means it take internally 25
    sum +=numbers[index] 
    if sum>100: #here if the sum is greater than 100 than condition becomes true moves to true block code
        print("sum exceeded 100")#here we print sum exceeded 100 and than we are breaking iteration 
        break
    index+=1 1#after that it the index value is incremented
print(numbers[index])#here it display the last iterated number by index

