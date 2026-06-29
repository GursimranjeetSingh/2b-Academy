# Write a program that asks for your name and age, then prints: 'Hello [name], you will turn [age+1] next year!'


# Ask the user to enter their name and store it in the variable 'name'
name = input("Enter your name: ")

# Ask the user to enter their age and convert it to an integer
age = int(input("Enter your age: "))

# Add 1 to the current age to calculate next year's age
next_age = age + 1

# Display the final message using an f-string
print(f"Hello {name}, you will turn {next_age} next year!")