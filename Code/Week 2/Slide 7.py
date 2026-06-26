# Student Marks Program
students = {}
n = int(input("How many students? "))
for _ in range(n):
    name = input("Student name: ")
    marks = float(input(f"Marks for {name}: "))
    students[name] = marks

# Calculate stats
marks_list = list(students.values())

average = sum(marks_list) / len(marks_list)
top = max(students, key=students.get)
low = min(students, key=students.get)

# Print report
print("\n========= MARKS REPORT =========")
for name, m in students.items():
    grade = 'A' if m >= 80 else 'B' if m >= 60 else 'C'
    print(f"{name:<15} {m:>5.1f} [{grade}]")

print(f"Average : {average:.2f}")
print(f"Topper  : {top} ({students[top]})")
print(f"Lowest  : {low} ({students[low]})")