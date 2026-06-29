# ==================================================
# 1. Creating Lists
# ==================================================

numbers = [10, 20, 30, 40, 50]
fruits = ["Apple", "Mango", "Banana"]
mixed = [10, "Python", True, 3.14]

print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)


# ==================================================
# 2. Indexing
# ==================================================

print("\nFirst Element:", fruits[0])
print("Second Element:", fruits[1])
print("Last Element:", fruits[-1])


# ==================================================
# 3. Slicing
# ==================================================

print("\nFirst 3 Numbers:", numbers[:3])
print("Middle Numbers:", numbers[1:4])
print("Last 2 Numbers:", numbers[-2:])
print("Reverse List:", numbers[::-1])


# ==================================================
# 4. Modifying Elements
# ==================================================

fruits[1] = "Orange"

print("\nModified List:", fruits)


# ==================================================
# 5. append()
# ==================================================

fruits.append("Grapes")

print("\nAfter append():", fruits)


# ==================================================
# 6. insert()
# ==================================================

fruits.insert(1, "Kiwi")

print("After insert():", fruits)


# ==================================================
# 7. extend()
# ==================================================

fruits.extend(["Cherry", "Pineapple"])

print("After extend():", fruits)


# ==================================================
# 8. remove()
# ==================================================

fruits.remove("Orange")

print("\nAfter remove():", fruits)


# ==================================================
# 9. pop()
# ==================================================

removed = fruits.pop()

print("Removed:", removed)
print("After pop():", fruits)


# ==================================================
# 10. del
# ==================================================

del fruits[0]

print("After del:", fruits)


# ==================================================
# 11. clear()
# ==================================================

temp = [1, 2, 3]

temp.clear()

print("\nAfter clear():", temp)


# ==================================================
# 12. sort()
# ==================================================

numbers2 = [50, 10, 30, 20, 40]

numbers2.sort()

print("\nAscending:", numbers2)

numbers2.sort(reverse=True)

print("Descending:", numbers2)


# ==================================================
# 13. reverse()
# ==================================================

numbers2.reverse()

print("Reverse:", numbers2)


# ==================================================
# 14. count()
# ==================================================

values = [10, 20, 10, 30, 10]

print("\nCount of 10:", values.count(10))


# ==================================================
# 15. index()
# ==================================================

print("Index of 30:", values.index(30))


# ==================================================
# 16. copy()
# ==================================================

original = [1, 2, 3]

copied = original.copy()

copied.append(4)

print("\nOriginal:", original)
print("Copied:", copied)


# ==================================================
# 17. Aliasing vs Copying
# ==================================================

a = [1, 2, 3]

b = a

b.append(4)

print("\nAliasing:")
print("a:", a)
print("b:", b)


# ==================================================
# 18. Built-in Functions
# ==================================================

numbers3 = [10, 20, 30, 40]

print("\nLength:", len(numbers3))
print("Maximum:", max(numbers3))
print("Minimum:", min(numbers3))
print("Sum:", sum(numbers3))


# ==================================================
# 19. Membership Operators
# ==================================================

print("\n20 in numbers:", 20 in numbers3)
print("100 not in numbers:", 100 not in numbers3)


# ==================================================
# 20. List Operators
# ==================================================

a = [1, 2]
b = [3, 4]

print("\nConcatenation:", a + b)

print("Repetition:", a * 3)


# ==================================================
# 21. Looping Through Lists
# ==================================================

print("\nFor Loop:")

for fruit in fruits:
    print(fruit)


# ==================================================
# 22. enumerate()
# ==================================================

print("\nEnumerate:")

for index, value in enumerate(fruits):
    print(index, value)


# ==================================================
# 23. List Comprehension
# ==================================================

squares = [x * x for x in range(5)]

print("\nSquares:", squares)

even = [x for x in range(10) if x % 2 == 0]

print("Even Numbers:", even)


# ==================================================
# 24. Nested Lists
# ==================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("\nMatrix Element:", matrix[1][2])


# ==================================================
# 25. List Unpacking
# ==================================================

numbers4 = [100, 200, 300]

a, b, c = numbers4

print("\nUnpacking:")
print(a)
print(b)
print(c)