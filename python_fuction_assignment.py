# Function To Finf the Area of Rectangle
def area_rectangle(length, width):
    #Calculate and return the area
    return length * width

#Ask user for input

#Ask the User to Enter the Length
length = float(input("Enter length: "))

#Ask the User to Enter the Width
width = float(input("Enter width: "))

#Call tthe function and display the result

#Call the Fuction 
area = area_rectangle(length, width)

#Display the Results
print("area =", area)

# Test Cases

#Test 1
print(area_rectangle(5, 4))

#Test 2
print(area_rectangle(10, 8))

#Test 3
print(area_rectangle(7, 3))




#Fuction To Calculate BMI
def calculate_bmi(weight, height):
    #calculate and return the BMI
    return weight / (height ** 2)

#Ask user to Enter Weight and Height

#Ask the User to Enter the Weight
weight = float(input("Enter weight in kg: "))

#Ask the User to Enter the Height
height = float(input("Enter height in meters: "))

#Call the Fuction and display the results

#Call the Fuction

bmi = calculate_bmi(weight, height)

#Display the BMI results rounded to 2 decimal places

print("BMI =", round(bmi, 2))


# Determine BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")


# Test cases

# Test 1
print("Test 1 BMI:", round(calculate_bmi(50, 1.7), 2))

# Test 2
print("Test 2 BMI:", round(calculate_bmi(70, 1.75), 2))

# Test 3
print("Test 3 BMI:", round(calculate_bmi(90, 1.8), 2))




#Fuction To Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    #Calculate and return the Fahrenheit Value
    return (celsius * 9/5) + 32

#Ask the user to Enter the Celsius Value
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)


# Testing values
print("Test 1 (0°C):", celsius_to_fahrenheit(0))
print("Test 2 (25°C):", celsius_to_fahrenheit(25))
print("Test 3 (100°C):", celsius_to_fahrenheit(100))



#Fuction to Determine if a Number is Even or Odd
def even_or_odd(number):
    #Calculate and return whether the number is even or odd

    #Calculate if the number is even or odd using modulus operator (%)
    if number % 2 == 0:
        #return "Even" if the number is even
        return "Even"
    else:
        #return "Odd" if the number is odd
        return "Odd"



#Ask the user to Enter a Number
number = int(input("Enter a number: "))


result = even_or_odd(number)

print("The number is:", result)


# Testing values
print("Test 1 (4):", even_or_odd(4))
print("Test 2 (7):", even_or_odd(7))
print("Test 3 (20):", even_or_odd(20))