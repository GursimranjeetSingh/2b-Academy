#Using a while loop, keep asking the user for a number until they enter 0. Print the sum of all numbers entered.

# Initialize the sum variable to store the total
total = 0

# Ask the user to enter the first number
number = int(input("Enter a number (0 to stop): "))

# Continue the loop until the user enters 0
while number != 0:
    # Add the entered number to the total
    total += number

    # Ask for the next number
    number = int(input("Enter a number (0 to stop): "))

# Display the final sum
print(f"The sum of all numbers is: {total}")