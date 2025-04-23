#list comprehension are the writing code in concise way to create a list using for loop
#square numbers
print([i**2 for i in range(1,11)])
#even numbers
print([i for i in range(1,21)if i%2==0])

#length of words in a list
words = ["apple", "banana", "cherry", "date"]
print([len(word)for word in words])
