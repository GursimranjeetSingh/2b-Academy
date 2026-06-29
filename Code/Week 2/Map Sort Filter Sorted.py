# ==================================================
# 1. sort() Method (Lists Only)
# ==================================================

numbers = [40, 10, 30, 20]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# ==================================================
# 2. sort() with Strings
# ==================================================

names = ["John", "Alice", "Bob"]

names.sort()

print("\nSorted Names:", names)


# ==================================================
# 3. sort() using key
# ==================================================

languages = ["Python", "C", "Java", "JavaScript"]

languages.sort(key=len)

print("\nSort by Length:", languages)


# ==================================================
# 4. sorted() with Lists
# ==================================================

numbers = [50, 20, 40, 10]

new_list = sorted(numbers)

print("\nOriginal:", numbers)

print("Sorted:", new_list)


# ==================================================
# 5. sorted() with Tuples
# ==================================================

numbers = (40, 10, 30, 20)

result = sorted(numbers)

print("\nTuple Sorted:", result)


# ==================================================
# 6. sorted() with Strings
# ==================================================

text = "python"

print("\nSorted Characters:")

print(sorted(text))


# ==================================================
# 7. sorted() with Dictionary Keys
# ==================================================

student = {
    "name": "John",
    "age": 20,
    "city": "Delhi"
}

print("\nSorted Keys:")

print(sorted(student))


# ==================================================
# 8. sorted() with Dictionary Values
# ==================================================

marks = {
    "John": 80,
    "Alice": 95,
    "Bob": 70
}

print("\nSorted Values:")

print(sorted(marks.values()))


# ==================================================
# 9. sorted() on Dictionary Items
# ==================================================

print("\nSort by Keys:")

print(sorted(marks.items()))

print("\nSort by Values:")

print(sorted(
    marks.items(),
    key=lambda x: x[1]
))


# ==================================================
# 10. map() with Lists
# ==================================================

numbers = [1, 2, 3, 4, 5]

squares = list(
    map(
        lambda x: x * x,
        numbers
    )
)

print("\nSquares:")

print(squares)


# ==================================================
# 11. map() with Multiple Lists
# ==================================================

a = [1, 2, 3]

b = [10, 20, 30]

result = list(
    map(
        lambda x, y: x + y,
        a,
        b
    )
)

print("\nAddition:")

print(result)


# ==================================================
# 12. map() with Tuples
# ==================================================

numbers = (1, 2, 3, 4)

result = list(
    map(
        lambda x: x * 10,
        numbers
    )
)

print("\nTuple Mapping:")

print(result)


# ==================================================
# 13. map() with Dictionary Values
# ==================================================

marks = {
    "John": 80,
    "Alice": 90
}

result = list(
    map(
        lambda x: x + 5,
        marks.values()
    )
)

print("\nUpdated Marks:")

print(result)


# ==================================================
# 14. filter() with Lists
# ==================================================

numbers = [1, 2, 3, 4, 5, 6]

even = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print("\nEven Numbers:")

print(even)


# ==================================================
# 15. filter() with Tuples
# ==================================================

numbers = (10, 15, 20, 25)

result = list(
    filter(
        lambda x: x > 15,
        numbers
    )
)

print("\nGreater Than 15:")

print(result)


# ==================================================
# 16. filter() with Dictionary Values
# ==================================================

marks = {
    "John": 80,
    "Alice": 95,
    "Bob": 70
}

result = list(
    filter(
        lambda x: x > 80,
        marks.values()
    )
)

print("\nMarks Above 80:")

print(result)


# ==================================================
# 17. filter() with Dictionary Items
# ==================================================

result = dict(
    filter(
        lambda x: x[1] > 80,
        marks.items()
    )
)

print("\nStudents Above 80:")

print(result)


# ==================================================
# 18. Combining map() and filter()
# ==================================================

numbers = [1, 2, 3, 4, 5, 6]

result = list(
    map(
        lambda x: x * x,
        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )
)

print("\nSquare of Even Numbers:")

print(result)