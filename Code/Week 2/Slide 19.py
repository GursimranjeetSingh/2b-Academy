class Student:  # Blueprint
    def __init__(self, name, marks):
        # 'self' = the object itself
        self.name = name    # attribute
        self.marks = marks  # attribute
    def get_average(self):
        return self.marks
    def is_passing(self):
        return self.marks >= 40

# Create OBJECTS (instances)
s1 = Student('Alice', 95)
s2 = Student('Bob', 38)

# Access attributes & call methods
print(s1.name)           # Alice
print(s2.is_passing())   # False