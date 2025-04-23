#discount calculator
orginal_amount=int(input("enter the amount"))
discount_percent= int(input("enter the discount percent"))
discount_amount=orginal_amount*(discount_percent/100)
after_discount=orginal_amount-discount_amount
print(f"the orginal price is {orginal_amount} its discount percentage is {discount_percent} than after discount peice is{after_discount}")