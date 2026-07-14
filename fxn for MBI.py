# 1. Function to Find the Area of a Rectangle
def area_rectangle(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))
print("Area =", area_rectangle(length, width))

print("Test 1:", area_rectangle(5, 4))
print("Test 2:", area_rectangle(10, 8))
print("Test 3:", area_rectangle(7, 6))

