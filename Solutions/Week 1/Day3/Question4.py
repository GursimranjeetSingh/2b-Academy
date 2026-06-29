# What is the difference between return and print inside a function? Give an example of each.​

# This function prints the result directly
def add_print(a, b):
    print(a + b)

# Call the function
add_print(10, 20)


##########################################################

# This function returns the result
def add_return(a, b):
    return a + b

# Store the returned value
result = add_return(10, 20)

# Print the returned value
print(result)