#palindrome
def palindrome(num):
    reverse=num[::-1]
    if num==reverse:
        print(f"{number} is palindrome")
    else:
        print(f"{number} is not palindrome")
number=(input("enter the number"))
palindrome(number)
