
# 4. Function to Determine if a Number is Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("\nEnter a number: "))
print("Result:", even_or_odd(number))

print("Test 1:", even_or_odd(4))
print("Test 2:", even_or_odd(7))
print("Test 3:", even_or_odd(20))