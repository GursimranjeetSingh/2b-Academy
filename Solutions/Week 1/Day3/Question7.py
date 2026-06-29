# Write a function print_profile(**details) that prints each key-value pair it receives, one per line. Call it like print_profile(name="John", age=20, city="Delhi").

# Function that accepts any number of keyword arguments
def print_profile(**details):

    # Loop through each key-value pair
    for key, value in details.items():

        # Print the key and its value
        print(f"{key}: {value}")


# Call the function with keyword arguments
print_profile(name="John", age=20, city="Delhi")