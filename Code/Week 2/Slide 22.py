class Person:  # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"I'm {self.name}, age {self.age}")

class Student(Person):  # Inherits Person
    def __init__(self, name, age, marks):
        super().__init__(name, age)  # Call parent constructor
        self.marks = marks
    def study(self):
        print(f"{self.name} is studying...")
    def introduce(self):  # Override parent method
        super().introduce()
        print(f"I scored {self.marks}")

class Teacher(Person):  # Inherits Person
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def teach(self):
        print(f"{self.name} teaches {self.subject}")

s = Student('Alice', 20, 95)
s.introduce()  # Calls overridden version
s.study()