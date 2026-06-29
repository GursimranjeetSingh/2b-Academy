#Write a function count_vowels(word) that returns the number of vowels in the given string.​

# Function to count the number of vowels in a word
def count_vowels(word):

    # Store all vowels
    vowels = "aeiouAEIOU"

    # Initialize the counter
    count = 0

    # Check each character in the word
    for letter in word:

        # If the character is a vowel, increase the count
        if letter in vowels:
            count += 1

    # Return the total number of vowels
    return count


# Test the function
text = input("Enter a word: ")

print("Number of vowels:", count_vowels(text))