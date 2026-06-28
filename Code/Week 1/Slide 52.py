# ==========================================
# RECURSIVE FUNCTION: Factorial
# ==========================================

def factorial(n):

    # Base Case
    if n == 1:
        print(f"factorial({n}) = 1")
        return 1

    # Recursive Case
    print(f"factorial({n}) = {n} × factorial({n-1})")

    result = n * factorial(n - 1)

    print(f"Returning {result} from factorial({n})")

    return result


number = 5

answer = factorial(number)

print("\nFactorial =", answer)