#checking whether the given character is vowel or not
character=input("enter the string")
#here we are declaring vowels in tuple
vowels=('a','e','i','o','u')
if character in vowels :#here we are checking whether the condition is true or false
    print(f"{character} is a vowel")#it is a true block statment
#it is alternative block statement is executed when if condition is false
else:
    print(f"{character} is a not vowel")
