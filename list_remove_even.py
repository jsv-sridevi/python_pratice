#here even index values should not print
list_1 = [1, 2, 3, 4, 5]
odd_index=[]
index=0
while index <len(list_1):#here if index value is less than length of list moves inside loop
    if index%2==0:#if the index is even moves to true block statement
        index +=1 #index is incremented
        continue#presentindex value is skipped
        
    else:
        odd_index.append(list_1[index])
        #here we are adding elements to odd_index list by apppend the appended values are even index of list 1
        index +=1 #index is incremented
print(odd_index)#here odd index values are printed