# ==========================================
# 1. Normal Function vs Lambda Function
# ==========================================

def square(x):
    return x * x

square_lambda = lambda x: x * x

print("Normal Function:", square(5))
print("Lambda Function:", square_lambda(5))


# ==========================================
# 2. Lambda with Multiple Parameters
# ==========================================

add = lambda a, b: a + b

print("\nAddition:", add(10, 20))


# ==========================================
# 3. Lambda with Conditional Expression
# ==========================================

largest = lambda a, b: a if a > b else b

print("\nLargest Number:", largest(15, 25))


# ==========================================
# 4. Lambda Returning Multiple Values
# ==========================================

calculate = lambda a, b: (a + b, a * b)

sum_result, product_result = calculate(5, 10)

print("\nSum:", sum_result)
print("Product:", product_result)