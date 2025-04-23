#remove duplicates and print list
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
index=0 #here we re index varibale declaring it as zero
while index <len(duplicate_list):#if the index value is less than the length of duplicate_list than goes into loop
    element=duplicate_list[index]#here we declaring duplicate_list[index] elements to element variable
    if duplicate_list.count(element)>1:
    #here count checks how many times a variable is repeated if it morethan 1 moves to true block statement
        duplicate_list.remove(element)
        #here it removes the duplicate element from the list
    else:
        index+=1#here index value is going to increment
print(duplicate_list)#here duplicate_list is  going to print without duplicate element

