# Modify the Number Guessing Game: add a maximum attempts limit of 7. If exceeded, print 'Game
# over!'

import random

# Generate a random number between 1 and 100
secret = random.randint(1, 100)

# Keep track of the number of attempts
attempts = 0

# Maximum number of attempts allowed
max_attempts = 7

print("🎯 Guess the number between 1 and 100!")

# Continue the game until the user guesses correctly
# or exceeds the maximum attempts
while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("📈 Too low! Try higher.")
    elif guess > secret:
        print("📉 Too high! Try lower.")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break

# This else belongs to the while loop.
# It runs only if the loop ends normally
# (without encountering break).
else:
    print("❌ Game over!")

# Display the secret number at the end
print(f"The secret number was {secret}.")