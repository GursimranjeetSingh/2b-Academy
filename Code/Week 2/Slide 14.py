# ✅ Best practice: use 'with' (auto-closes file)

# Writing to a file
with open('students.txt', 'w') as f:
    f.write("Alice,95\n")
    f.write("Bob,82\n")

# Reading all lines at once
with open('students.txt', 'r') as f:
    lines = f.readlines()  # List of strings
for line in lines:
    print(line.strip())

# Reading line by line (memory-efficient)
with open('students.txt', 'r') as f:
    for line in f:
        name, marks = line.strip().split(',')
        print(f"{name} scored {marks}")

# Appending to a file
with open('students.txt', 'a') as f:
    f.write("Carol,91\n")

# CSV module
import csv
with open('data.csv', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)