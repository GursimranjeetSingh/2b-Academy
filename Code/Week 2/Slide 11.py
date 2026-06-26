def is_palindrome(word):
    clean = word.lower().strip()
    return clean == clean[::-1]

print(is_palindrome("racecar"))  # True
print(is_palindrome("Python"))   # False


##############################################################################


sentence = input("Enter sentence: ")
words = sentence.split()
vowels = sum(
    1 for c in sentence.lower()
    if c in 'aeiou'
)
print(f"Words : {len(words)}")
print(f"Vowels: {vowels}")



##############################################################################

# Triangle
n = 5
for i in range(1, n + 1):
    print('*' * i)

# Number Pyramid
for i in range(1, n + 1):
    print(' '.join(str(j) for j in range(1, i + 1)))