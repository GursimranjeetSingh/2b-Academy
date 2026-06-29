# ==================================================
# 1. Writing to a File (w)
# Creates a new file or overwrites an existing file.
# ==================================================

file = open("sample.txt", "w")

file.write("Hello Python\n")
file.write("Welcome to File Handling\n")

file.close()


# ==================================================
# 2. Reading Entire File
# read() reads the complete contents of the file.
# ==================================================

file = open("sample.txt", "r")

print("\nread():")
print(file.read())

file.close()


# ==================================================
# 3. Reading Specific Characters
# read(size) reads a fixed number of characters.
# ==================================================

file = open("sample.txt", "r")

print("\nread(10):")
print(file.read(10))

file.close()


# ==================================================
# 4. Reading One Line
# readline() reads one line at a time.
# ==================================================

file = open("sample.txt", "r")

print("\nreadline():")
print(file.readline())

file.close()


# ==================================================
# 5. Reading All Lines
# readlines() returns all lines as a list.
# ==================================================

file = open("sample.txt", "r")

print("\nreadlines():")
print(file.readlines())

file.close()


# ==================================================
# 6. Appending Data
# Append mode adds new data without removing old data.
# ==================================================

file = open("sample.txt", "a")

file.write("Appending a new line.\n")

file.close()


# ==================================================
# 7. Using with Statement
# with automatically closes the file after use.
# ==================================================

print("\nwith statement:")

with open("sample.txt", "r") as file:
    print(file.read())


# ==================================================
# 8. tell()
# tell() returns the current file pointer position.
# ==================================================

file = open("sample.txt", "r")

print("\nCurrent Position:")

print(file.tell())

file.read(5)

print(file.tell())

file.close()


# ==================================================
# 9. seek()
# seek() moves the file pointer to a specific position.
# ==================================================

file = open("sample.txt", "r")

file.seek(7)

print("\nAfter seek(7):")

print(file.read())

file.close()


# ==================================================
# 10. flush()
# flush() immediately writes buffered data to the file.
# file is open in ram flush writes to the file on disk
# ==================================================

file = open("temp.txt", "w")

file.write("Temporary Data")

file.flush()

file.close()


# ==================================================
# 11. File Properties
# File objects provide information about the file.
# ==================================================

file = open("sample.txt", "r")

print("\nFile Name:", file.name)

print("File Mode:", file.mode)

print("Is Closed:", file.closed)

file.close()

print("After close:", file.closed)


# ==================================================
# 12. writelines()
# writelines() writes multiple lines to a file.
# ==================================================

file = open("languages.txt", "w")

lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

file.writelines(lines)

file.close()


# ==================================================
# 13. Looping Through a File
# Files can be read line by line using loops.
# ==================================================

print("\nLooping Through File:")

with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())


# ==================================================
# 14. Exception Handling
# Prevents program crashes when file errors occur.
# ==================================================

try:
    file = open("unknown.txt", "r")

except FileNotFoundError:
    print("\nFile not found.")


# ==================================================
# 15. Binary Files
# Binary mode is used for images, videos, and PDFs.
# ==================================================

file = open("image.jpg", "rb")
data = file.read()
file.close()


# ==================================================
# 16. File Pointer Example
# The file pointer tracks the current reading position.
# ==================================================

file = open("sample.txt", "r")

print("\nPointer Position:")

print(file.tell())

file.read(8)

print(file.tell())

file.seek(0)

print(file.tell())

file.close()


# ==================================================
# 17. OS File Operations
# The os module performs file system operations.
# ==================================================

import os

print("\nFile Exists:")

print(os.path.exists("sample.txt"))

# os.rename("sample.txt", "newfile.txt")

# os.remove("newfile.txt")


# ==================================================
# 18. CSV Files
# CSV files store tabular data using rows and columns.
# ==================================================

import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])

    writer.writerow(["John", 85])

    writer.writerow(["Alice", 92])


# ==================================================
# 19. JSON Files
# JSON is commonly used for APIs and data exchange.
# ==================================================

import json

student = {
    "name": "John",
    "age": 20
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print("\nJSON Data:")

print(data)