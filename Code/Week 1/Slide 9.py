# Output
print("Hello, World!")
print("My score is", 95)

# Input — always returns a string!
name = input("What is your name? ")
age = int(input("How old are you? "))

# f-strings (Python 3.6+)
print(f"Hello, {name}! You are {age} years old.")
print(f"In 10 years you will be {age + 10}.")

# Type conversion examples
x = int("42")      # string → integer
y = float("3.14")  # string → float
z = str(100)       # integer → string