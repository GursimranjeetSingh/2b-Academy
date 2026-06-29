# Q1. Write an if-else program to check if a number entered by the user is positive, negative, or zero.


# Ask the user to enter a number
number = float(input("Enter a number: "))

# Check if the number is positive
if number > 0:
    print("The number is positive.")

# Check if the number is negative
elif number < 0:
    print("The number is negative.")

# If the number is neither positive nor negative, it must be zero
else:
    print("The number is zero.")