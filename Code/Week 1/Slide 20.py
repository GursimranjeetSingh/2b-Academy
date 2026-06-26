# Basic function — no parameters
def greet():
    print("Hello, everyone!")

# Function with parameters
def greet_person(name):  # name is a parameter
    print(f"Hello, {name}!")

# Function with return value
def add(a, b):
    result = a + b
    return result  # Sends the answer back

# Default parameter value
def power(base, exp=2):  # exp defaults to 2
    return base ** exp


# --- Calling functions ---
greet()
greet_person("Alice")

total = add(10, 5)  # total = 15
print(total)

print(power(3))     # 3^2 = 9
print(power(3, 3))  # 3^3 = 27