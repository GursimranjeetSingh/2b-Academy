# Everything scattered

student1_name = 'Alice'
student1_marks = 95
student2_name = 'Bob'
student2_marks = 72

# Functions everywhere, hard
# to know what belongs where
def get_grade(marks):
    return 'A' if marks >= 80 else 'B'

print(get_grade(student1_marks))

# Works, but messy for 100 students!



#####################################################################


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_grade(self):
        return 'A' if self.marks >= 80 else 'B'
    def introduce(self):
        g = self.get_grade()
        print(f"I am {self.name}, Grade: {g}")


# Create objects (instances)
s1 = Student('Alice', 95)
s2 = Student('Bob', 72)

s1.introduce()  # I am Alice, Grade: A
s2.introduce()  # I am Bob, Grade: B