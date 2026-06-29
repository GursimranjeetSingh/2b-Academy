# ==================================================
# 1. Creating a Class
# A class is a blueprint for creating objects.
# ==================================================

class Student:

    # ==================================================
    # 2. Constructor
    # __init__ automatically executes when an object is created.
    # ==================================================
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

        print(f"Object created for {self.name}")

    # ==================================================
    # 3. Instance Method
    # Methods define the behavior of an object.
    # ==================================================
    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    # ==================================================
    # 4. Another Method
    # Objects can have multiple behaviors.
    # ==================================================
    def study(self):
        print(f"{self.name} is studying {self.course}.")


# ==================================================
# 5. Creating Objects
# Objects are instances of a class.
# ==================================================

student1 = Student("John", 20, "Python")

student2 = Student("Alice", 22, "Data Science")


# ==================================================
# 6. Calling Methods
# Objects can access their methods using dot notation.
# ==================================================

student1.display()

student1.study()

student2.display()

student2.study()


# ==================================================
# 7. Accessing Instance Variables
# Each object stores its own data.
# ==================================================

print("\nAccessing Variables:")

print(student1.name)

print(student2.course)


# ==================================================
# 8. Modifying Object Data
# Instance variables can be changed.
# ==================================================

student1.age = 21

print("\nUpdated Age:")

print(student1.age)


# ==================================================
# 9. self Keyword Demonstration
# self refers to the current object.
# ==================================================

print("\nCurrent Object Data:")

print(student1.name)

print(student2.name)


# ==================================================
# 10. Multiple Objects
# Each object maintains separate data.
# ==================================================

print("\nDifferent Object Data:")

print(student1.name, student1.age)

print(student2.name, student2.age)