# Write a function is_prime(n) that returns True if n is a prime number, False otherwise.
# Function to check whether a number is prime
def is_prime(n):

    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check for factors from 2 to n-1
    for i in range(2, n):
        # If n is divisible by i, it is not prime
        if n % i == 0:
            return False

    # If no factors are found, the number is prime
    return True


# Test the function
num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")