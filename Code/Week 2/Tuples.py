# ==================================================
# 1. Creating Tuples
# ==================================================

numbers = (10, 20, 30, 40, 50)

fruits = ("Apple", "Mango", "Banana")

mixed = (10, "Python", True, 3.14)

print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)


# ==================================================
# 2. Single Element Tuple
# ==================================================

single = (100,)

print("\nSingle Element Tuple:", single)
print(type(single))


# ==================================================
# 3. Indexing
# ==================================================

print("\nFirst Element:", fruits[0])

print("Second Element:", fruits[1])

print("Last Element:", fruits[-1])


# ==================================================
# 4. Slicing
# ==================================================

print("\nFirst 3 Numbers:", numbers[:3])

print("Middle Numbers:", numbers[1:4])

print("Last 2 Numbers:", numbers[-2:])

print("Reverse Tuple:", numbers[::-1])


# ==================================================
# 5. Immutability
# ==================================================

# fruits[1] = "Orange"   ❌ TypeError

print("\nTuples are immutable.")
print("Elements cannot be modified.")


# ==================================================
# 6. Tuple Concatenation
# ==================================================

a = (1, 2)

b = (3, 4)

print("\nConcatenation:", a + b)


# ==================================================
# 7. Tuple Repetition
# ==================================================

print("Repetition:", a * 3)


# ==================================================
# 8. Membership Operators
# ==================================================

print("\n2 in a:", 2 in a)

print("10 not in a:", 10 not in a)


# ==================================================
# 9. count() Method
# ==================================================

values = (10, 20, 10, 30, 10)

print("\nCount of 10:", values.count(10))


# ==================================================
# 10. index() Method
# ==================================================

print("Index of 30:", values.index(30))


# ==================================================
# 11. Built-in Functions
# ==================================================

nums = (10, 20, 30, 40)

print("\nLength:", len(nums))

print("Maximum:", max(nums))

print("Minimum:", min(nums))

print("Sum:", sum(nums))


# ==================================================
# 12. Looping Through Tuples
# ==================================================

print("\nLooping Through Fruits:")

for fruit in fruits:
    print(fruit)


# ==================================================
# 13. enumerate()
# ==================================================

print("\nEnumerate:")

for index, value in enumerate(fruits):
    print(index, value)


# ==================================================
# 14. Tuple Packing
# ==================================================

student = ("John", 20, 85)

print("\nPacked Tuple:", student)


# ==================================================
# 15. Tuple Unpacking
# ==================================================

name, age, marks = student

print("\nName:", name)

print("Age:", age)

print("Marks:", marks)


# ==================================================
# 16. Variable Swapping
# ==================================================

a = 10

b = 20

a, b = b, a

print("\nAfter Swapping:")

print("a =", a)

print("b =", b)


# ==================================================
# 17. Nested Tuples
# ==================================================

matrix = (
    (1, 2, 3),
    (4, 5, 6)
)

print("\nNested Tuple Element:", matrix[1][2])


# ==================================================
# 18. Tuple Conversion
# ==================================================

my_list = [1, 2, 3]

tuple_data = tuple(my_list)

print("\nList to Tuple:", tuple_data)

my_tuple = (4, 5, 6)

list_data = list(my_tuple)

print("Tuple to List:", list_data)