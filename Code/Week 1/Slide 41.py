print("Hello Alice!")
print("Alice is 20 years old.")

# ... 30 lines later ...

print("Hello Bob!")
print("Bob is 25 years old.")

# Repeating the same logic
# everywhere — hard to change!


##########################################################

def greet(name, age):
    print(f"Hello {name}!")
    print(f"{name} is {age}.")


# Use it anywhere, anytime:
greet("Alice", 20)
greet("Bob", 25)
greet("Carol", 22)

# Change once → updates everywhere