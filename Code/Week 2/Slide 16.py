import csv
def load_students(filename):
    students = {}
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                name, marks = row[0], float(row[1])
                students[name] = marks
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")
    except ValueError:
        print("❌ Invalid marks in CSV!")
    return students

def generate_report(students, outfile):
    if not students:
        print("No students to report.")
        return
    avg = sum(students.values()) / len(students)
    with open(outfile, 'w') as f:
        f.write("Name,Marks,Grade\n")
        for name, m in students.items():
            grade = 'A' if m >= 80 else 'B' if m >= 60 else 'C'
            f.write(f"{name},{m},{grade}\n")
        f.write(f"\nClass Average: {avg:.2f}\n")
    print(f"✅ Report saved to {outfile}")

students = load_students('students.csv')
generate_report(students, 'report.txt')