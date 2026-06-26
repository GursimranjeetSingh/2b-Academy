# Create a dictionary
student = {
    'name': 'Alice',
    'age': 20,
    'grade': 'A'
}

# Access values
print(student['name'])      # Alice
print(student.get('age'))   # 20 (safe)

# Add / Update
student['email'] = 'a@b.com'
student['grade'] = 'A+'

# Delete
del student['age']

# Loop through
for key, val in student.items():
    print(key, '->', val)