# Ask the user for their age and whether they have a valid ID (yes/no). Print "Entry allowed" only if age ≥ 18 and they have a valid ID — using and directly, no nested if.

# Get user input for age
age = int(input("Enter your age: "))

# Get user input for ID validity
id_valid = input("Do you have a valid ID? (yes/no): ").lower()

# Check both conditions using 'and'
if age >= 18 and id_valid == "yes":
    print("Entry allowed")
else:
    print("Entry not allowed")