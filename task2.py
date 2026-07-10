# function to calculate area of rectangle
def area_rectangle(length, width):
    return length * width

print("Area: ", area_rectangle(5, 4))
print("Area: ", area_rectangle(10, 8))

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area = area_rectangle(length, width)

print("The area of the rectangle is:", area)

print("--------------------------------------------------------------")

# function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is:",round(bmi,2))
if bmi < 20:
    print("Underweight")
elif bmi < 30:
    print("Normal")
elif bmi < 50:
    print("Overweight")
else:
    print("Obese")

print("-----------------------------------------------------------------------")

# function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0), "F")
print(celsius_to_fahrenheit(25), "F")
print(celsius_to_fahrenheit(100), "F")

celsius = float(input("Enter temperature "))

fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)

print("-----------------------------------------------------------------------------------------------")

# function to check even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(20))

number = int(input("Enter number: "))

result = even_or_odd(number)

print("The number is:", result)
