try:
    num = int(input("Enter num: "))
    result = 100 / num
    print(f"Result: {result}")
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Divide by zero!")
except Exception as e:
    print(f"Error: {e}")
else:
    # No exception → runs here
    print("Success!")
finally:
    # ALWAYS runs (cleanup)
    print("Done.")