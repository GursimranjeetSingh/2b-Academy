# Write a function total(*numbers) that returns the sum of however many numbers are passed in.
# Call it with 2 numbers, then 5 numbers, then zero numbers — what does it return for zero?


# Function that accepts any number of arguments
def total(*numbers):

    # Initialize the sum
    sum = 0

    # Add each number to the sum
    for num in numbers:
        sum += num

    # Return the total
    return sum


# Call with 2 numbers
print(total(10, 20))

# Call with 5 numbers
print(total(1, 2, 3, 4, 5))

# Call with no numbers
print(total())