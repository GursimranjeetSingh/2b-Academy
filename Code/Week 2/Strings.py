# ==================================================
# 1. Creating Strings
# ==================================================

text = "Python Programming"

single = 'Hello'

multi = """This is
a multiline
string"""

print("Text:", text)


# ==================================================
# 2. Indexing
# ==================================================

print("\nFirst Character:", text[0])

print("Last Character:", text[-1])


# ==================================================
# 3. Slicing
# ==================================================

print("\nFirst 6 Characters:", text[:6])

print("From Index 7:", text[7:])

print("Reverse:", text[::-1])



# ==================================================
# 4. String Operations
# ==================================================

print("\nConcatenation:")

print("Hello" + " World")

print("\nRepetition:")

print("Hi " * 3)


# ==================================================
# 5. Membership Operators
# ==================================================

print("\n'Python' in text:", "Python" in text)

print("'Java' not in text:", "Java" not in text)


# ==================================================
# 6. Case Conversion Methods
# ==================================================

print("\nUpper:", text.upper())

print("Lower:", text.lower())

print("Title:", text.title())

print("Capitalize:", text.capitalize())

print("Swapcase:", text.swapcase())


# ==================================================
# 7. Searching Methods
# ==================================================

print("\nFind:", text.find("Program"))

print("Index:", text.index("Program"))

print("Count:", text.count("m"))

print("Startswith:", text.startswith("Python"))

print("Endswith:", text.endswith("ing"))


# ==================================================
# 8. Replace Method
# ==================================================

new_text = text.replace("Python", "Java")

print("\nReplace:")

print(new_text)


# ==================================================
# 9. Splitting Strings
# ==================================================

words = text.split()

print("\nSplit:")

print(words)

csv = "John,20,Delhi"

print(csv.split(","))


# ==================================================
# 10. Joining Strings
# ==================================================

words = ["Python", "is", "awesome"]

sentence = " ".join(words)

print("\nJoin:")

print(sentence)


# ==================================================
# 11. Removing Spaces
# ==================================================

name = "   Python   "

print("\nStrip:", name.strip())

print("Left Strip:", name.lstrip())

print("Right Strip:", name.rstrip())


# ==================================================
# 12. Validation Methods
# ==================================================

print("\nisdigit():", "123".isdigit())

print("isalpha():", "Python".isalpha())

print("isalnum():", "abc123".isalnum())

print("islower():", "python".islower())

print("isupper():", "PYTHON".isupper())

print("isspace():", "   ".isspace())

print("istitle():", "Python Programming".istitle())


# ==================================================
# 13. String Formatting
# ==================================================

name = "John"

age = 20

print("\nf-string:")

print(f"My name is {name}")

print(f"I am {age} years old")

print("\nformat():")

print("Name: {}".format(name))


# ==================================================
# 14. Escape Characters
# ==================================================

print("\nHello\nWorld")

print("Name:\tJohn")

print("He said \"Hello\"")


# ==================================================
# 15. Looping Through Strings
# ==================================================

print("\nCharacters:")

for ch in "Python":
    print(ch)


# ==================================================
# 16. String Comprehension
# ==================================================

result = "".join(
    ch.upper()
    for ch in "python"
)

print("\nComprehension:")

print(result)


# ==================================================
# 17. Built-in Functions
# ==================================================

print("\nLength:", len(text))

print("Maximum:", max(text))

print("Minimum:", min(text))

print("Sorted:", sorted(text))


# ==================================================
# 18. String Immutability
# ==================================================

# text[0] = "J"   ❌ TypeError

new_string = "J" + text[1:]

print("\nImmutable Example:")

print(new_string)
