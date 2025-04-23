class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Buddy")

try:
    print(my_dog.breed)  # 'breed' attribute_value doesn't exist
except AttributeError as e:
    print(f"Error: {e}")