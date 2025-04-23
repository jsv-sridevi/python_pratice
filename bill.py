total=0
items = [("Apple", 99), ("Banana",99), ("Milk",  49)]
print("items               price")
print("-"*30)
for item ,price in (items):
    print(f"{item}                {price}")
    total +=price
print("-"*30)
print(f"total                 {total}")
