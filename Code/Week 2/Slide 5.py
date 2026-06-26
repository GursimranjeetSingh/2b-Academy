# Create & Access

names = ['Alice', 'Bob', 'Carol']

print(names[0])   # Alice
print(names[-1])  # Carol


# Slicing
print(names[0:2])  # ['Alice', 'Bob']


# Methods
names.append('Dave')   # Add at the end
names.remove('Bob')    # Remove by value
names.sort()           # Sort in-place

print(len(names))      # 3

#####################################################################################

# Create

coords = (10, 20)
days = ('Mon', 'Tue', 'Wed')


# Access (same as list)
print(coords[0])  # 10


# Tuples are IMMUTABLE:
# coords[0] = 99  # ❌ TypeError!


# Packing / Unpacking
x, y = coords

print(x, y)  # 10 20


# When to use tuple?
# Fixed data: GPS coordinates, RGB values, dates