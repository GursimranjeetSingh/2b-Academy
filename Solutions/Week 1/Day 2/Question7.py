# Write a login check using nested if statements: first check if the username matches "admin", and only if it
# does, check if the password matches "1234". Print "Access granted", "Wrong password", or "Unknown user"
# accordingly.


# Ask the user to enter the username
username = input("Enter username: ")

# First check if the username is correct
if username == "admin":

    # Ask for the password only if the username matches
    password = input("Enter password: ")

    # Check if the password is correct
    if password == "1234":
        print("Access granted")
    else:
        print("Wrong password")

# Execute this block if the username is incorrect
else:
    print("Unknown user")