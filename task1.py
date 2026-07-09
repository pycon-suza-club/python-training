def introduce():
    #input user information
    first = str(input("Enter your first name: "))
    second = str(input("Enter your second name: "))
    third = str(input("Enter your third name: "))
    age = int(input("Enter your age: "))
    course = str(input("Enter your course: "))
    year = int(input("Enter your year of study: "))
    address = str(input("Enter your address: "))
    hobby = str(input("Enter your hobby: "))

    #print output
    print("My name is " + first + " " + second + " " + third + ". I am " + str(age) + " years old. I am studying " + course + " in year " + str(year) + ". I live in " + address + ". My hobby is " + hobby)

# Call the function to get user information
introduce()

# Grade checking
grade = int(input("Enter your grade: "))
if grade >= 90:
    print("Your grade is A")
elif grade >= 80:
    print("Your grade is B")
elif grade >= 70:
    print("Your grade is C")
elif grade >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")