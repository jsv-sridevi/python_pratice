#creating unique list from orginal list
unique_list=[]#here empty list declared using name unique_list
original_list = [1, 2, 2, 3, 4, 4, 5]
for i  in original_list:
     if i not in unique_list: #if i value is not there in unique_list than moves to true block  
         unique_list.append(i)#that value is append in unique_list
print(unique_list)