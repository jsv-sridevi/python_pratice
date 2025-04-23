import math  # Import the math module for mathematical functions
try:
    num=int(input("enter the value for exponential "))
    try:
        # Calculate e raised to a large power, likely to exceed float limits
        large_float = math.exp(num)#exp is exponential function
        print(large_float)  # This line might not be reached if overflow occurs
    except OverflowError as e:
        # If the result is too large for a float, an OverflowError is raised
        print(f"OverflowError occurred: {e}")  # Print the error message
except ValueError as e:
    print(f"ValueError:{e}")