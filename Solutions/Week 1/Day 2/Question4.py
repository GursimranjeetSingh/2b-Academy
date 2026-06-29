# Write a program that prints numbers 1–20 but skips multiples of 3 (use continue).

# Use a for loop to iterate from 1 to 20
for number in range(1, 21):

    # Check if the number is a multiple of 3
    if number % 3 == 0:
        # Skip the current iteration and move to the next number
        continue

    # Print the number if it is not a multiple of 3
    print(number)