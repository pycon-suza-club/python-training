# 3. Function to Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("\nEnter temperature in Celsius: "))
print("Fahrenheit =", celsius_to_fahrenheit(celsius))

print("Test 1:", celsius_to_fahrenheit(0))
print("Test 2:", celsius_to_fahrenheit(25))
print("Test 3:", celsius_to_fahrenheit(100))

