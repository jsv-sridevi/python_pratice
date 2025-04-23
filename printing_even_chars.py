#printing even index characters of string
index=0 #here we are creating variable name index value 0
result="" #here we are creating empty string 
sentence = "Python is amazing"
while index<len(sentence):#if index value is lessthan length sentence
    if index%2==0:# if the condition becomes true  than moves true block statement
        result+=(sentence[index]) #here we are incrementing result string with help of varible with its index
    index+=1    #here index value is incremented
print(result) #here result variable data is displayed