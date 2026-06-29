# Take a student's marks as input and print their grade using an elif chain: 90+ → "A+", 75–89 → "A",
# 60–74 → "B", below 60 → "Fail".

# Ask the user to enter the student's marks
marks = float(input("Enter the student's marks: "))

# Check the grade using an if-elif-else chain
if marks >= 90:
    print("Grade: A+")

elif marks >= 75:
    print("Grade: A")

elif marks >= 60:
    print("Grade: B")

else:
    print("Grade: Fail")