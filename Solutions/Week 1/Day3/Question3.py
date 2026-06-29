#Write a function celsius_to_fahrenheit(c) and call it for 0°C, 100°C, and 37°C.​

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    # Apply the conversion formula
    fahrenheit = (c * 9/5) + 32

    # Return the converted temperature
    return fahrenheit


# Call the function for different temperatures
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"37°C = {celsius_to_fahrenheit(37)}°F")