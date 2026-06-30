# ==================================================
# 1. Creating Dictionaries
# ==================================================

student = {
    "name": "John",
    "age": 20,
    "marks": 85
}

print("Student:", student)


# ==================================================
# 2. Accessing Values
# ==================================================

print("\nName:", student["name"])

print("Age:", student.get("age"))


# ==================================================
# 3. Adding New Key-Value Pairs
# ==================================================

student["city"] = "Delhi"

print("\nAfter Adding:", student)


# ==================================================
# 4. Modifying Values
# ==================================================

student["marks"] = 90

print("\nAfter Modification:", student)


# ==================================================
# 5. get() Method
# ==================================================

print("\nName:", student.get("name"))

print("Phone:", student.get("phone"))

print("Phone:", student.get("phone", "Not Found"))


# ==================================================
# 6. keys() Method
# ==================================================

print("\nKeys:")

print(student.keys())


# ==================================================
# 7. values() Method
# ==================================================

print("\nValues:")

print(student.values())


# ==================================================
# 8. items() Method
# ==================================================

print("\nItems:")

print(student.items())


# ==================================================
# 9. update() Method
# ==================================================

student.update({
    "age": 21,
    "country": "India"
})

print("\nAfter Update:")

print(student)


# ==================================================
# 10. pop() Method
# ==================================================

removed = student.pop("city")

print("\nRemoved:", removed)

print(student)


# ==================================================
# 11. popitem() Method
# ==================================================

last_item = student.popitem()

print("\nLast Item Removed:")

print(last_item)

print(student)


# ==================================================
# 12. copy() Method
# ==================================================

copy_student = student.copy()

print("\nCopied Dictionary:")

print(copy_student)


# ==================================================
# 13. clear() Method
# ==================================================

temp = {
    "a": 10,
    "b": 20
}

temp.clear()

print("\nAfter clear():")

print(temp)


# ==================================================
# 14. Membership Operators
# ==================================================

print("\n'name' in student:", "name" in student)

print("'phone' not in student:", "phone" not in student)


# ==================================================
# 15. Checking Values
# ==================================================

print("\nJohn in values:")

print("John" in student.values())


# ==================================================
# 16. Looping Through Keys
# ==================================================

print("\nKeys:")

for key in student:
    print(key)


# ==================================================
# 17. Looping Through Values
# ==================================================

print("\nValues:")

for value in student.values():
    print(value)


# ==================================================
# 18. Looping Through Items
# ==================================================

print("\nKey-Value Pairs:")

for key, value in student.items():
    print(key, ":", value)


# ==================================================
# 19. Built-in Functions
# ==================================================

print("\nLength:", len(student))

print("Maximum Key:", max(student))

print("Minimum Key:", min(student))


# ==================================================
# 20. Dictionary Comprehension
# ==================================================

squares = {
    x: x * x
    for x in range(5)
}

print("\nSquares Dictionary:")

print(squares)


# ==================================================
# 21. Nested Dictionaries
# ==================================================

students = {
    "student1": {
        "name": "John",
        "age": 20
    },
    "student2": {
        "name": "Alice",
        "age": 22
    }
}

print("\nNested Dictionary:")

print(students["student1"]["name"])


# ==================================================
# 22. fromkeys()
# ==================================================
# fromkeys() creates a new dictionary using a collection of keys and assigns the same default value to all of them.

keys = ["name", "age", "marks"]

data = dict.fromkeys(keys, 0)

print("\nfromkeys():")

print(data)


# ==================================================
# 23. setdefault()
# ==================================================
# setdefault() returns the value of a key if it exists. If the key does not exist, it creates the key with a default value.

student.setdefault("city", "Delhi")

print("\nsetdefault():")

print(student)


# ==================================================
# 24. Dictionary Constructor
# ==================================================

person = dict(
    name="David",
    age=25
)

print("\nDictionary Constructor:")

print(person)


# ==================================================
# 25. Duplicate Keys
# ==================================================

data = {
    "a": 10,
    "a": 20
}

print("\nDuplicate Keys:")

print(data)


# ==================================================
# 26. Dictionary Unpacking
# ==================================================

student = {
    "name": "John",
    "age": 20
}

print("\nUnpacking:")

print(*student)

print(*student.values())


# ==================================================
# 27. Merging Dictionaries
# ==================================================

a = {"x": 1}

b = {"y": 2}

merged = {**a, **b}

print("\nMerged Dictionary:")

print(merged)