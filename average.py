#average
# Define a function called calculate_average that takes a list of numbers as input.
def calculate_average(numbers):
    # Check if the list is empty to avoid division by zero.
    if not numbers:
        return 0  # Return 0 for an empty list (or handle it differently if needed)

    # Calculate the sum of the numbers in the list.
    total = sum(numbers)

    # Calculate the average by dividing the sum by the number of elements.
    average = total / len(numbers)

    # Return the calculated average.
    return average

# Get input from the user: a string of numbers separated by spaces.
numbers_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of floating-point numbers.
# Using float here in case the average is not a whole number.
numbers_list = list(map(float, numbers_str.split()))
print(numbers_list)

# Call the calculate_average function with the list of numbers.
result_average = calculate_average(numbers_list)

# Print the calculated average.
print(f"The average of the numbers is: {result_average}")