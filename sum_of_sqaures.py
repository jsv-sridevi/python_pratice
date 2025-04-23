# Initialize a global variable to store the sum of squares.
# While using globals can sometimes be necessary, it's often better to
# avoid them if possible for cleaner code. We'll address this later.
sum_squares = 0

# Define a function called sum_of_squares that takes a list as input.
def sum_of_squares(list_1):
    # We want to calculate the sum of squares of ALL numbers in the list.
    # The current logic 'if num in list_1:' has a problem:
    # - 'num' is not defined within this function's scope.
    # - Even if it were, this condition would check if a specific 'num' is in the list,
    #   not iterate through all the numbers.
    # - 'num + 1' doesn't do anything to the list or the calculation.

    # Let's reset the global sum_squares to 0 at the beginning of the function
    # if we intend to reuse the global variable. However, it's better to
    # calculate and return the sum within the function.
    global sum_squares
    sum_squares = 0

    # Iterate through each number in the input list.
    for number in list_1:
        # Calculate the square of the current number.
        square = number ** 2
        # Add the square to our running total.
        sum_squares += square

    # After processing all numbers in the list, return the total sum of squares.
    return sum_squares

# Get input from the user: a string of numbers separated by spaces.
numbers_str = input("Enter numbers separated by spaces: ")

# Convert the input string into a list of integers.
numbers_list = list(map(int, numbers_str.split()))
print(numbers_list)

# Call the sum_of_squares function with the list of numbers.
# The function will calculate the sum of squares and return it.
result = sum_of_squares(numbers_list)

# Print the calculated sum of squares.
print(f"The sum of squares is: {result}")

# The line 'print(f"{sum_squares}")' before calling the function
# would print the initial value of the global 'sum_squares' (which is 0).
# We now print the result returned by the function.