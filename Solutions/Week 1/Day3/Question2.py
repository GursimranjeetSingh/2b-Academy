#Write a function find_max(nums) that returns the largest number in a list WITHOUT using max().​

# Function to find the largest number in a list
def find_max(nums):

    # Assume the first element is the largest
    largest = nums[0]

    # Traverse the remaining elements
    for num in nums:
        # Update largest if a bigger number is found
        if num > largest:
            largest = num

    # Return the largest number
    return largest


# Example list
numbers = [12, 45, 7, 89, 23, 56]

# Call the function and print the result
print("Largest number:", find_max(numbers))