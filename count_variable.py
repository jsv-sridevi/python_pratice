string_1 = input("Enter a string: ")
from functools import reduce

vowels = "aeiouAEIOU"

result = reduce(lambda count, char: count + 1 if char in vowels else count, string_1, 0)

print(f"The number of vowels in the string '{string_1}' is: {result}")