#here printing common elements in 2 lists
list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
empty_list=[]
for element in list_1:
    if element in list_2:
        empty_list.append(element)
print(empty_list)