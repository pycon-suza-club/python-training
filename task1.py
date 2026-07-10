 # Question 1
def introduce():
    #input user information
    full_name = str(input("Enter your full name: "))
    age = int(input("Enter your age: "))
    gender = str(input("Enter your gender: "))
    course = str(input("Enter your course: "))
    phone= str(input("Enter your Phone Number: "))
    hobby = str(input("Enter your hobby: "))
    country=str(input("Enter your Country: "))

    #print output
    print("-----PERSONAL INFORMATION------")
    print("Full Name: " + full_name)
    print("Age:       " + str(age))
    print("Gender:    " + gender)
    print("Country:   " + country)
    print("Phone:     " + phone)
    print("Course:    " + course)
    print("Hobby:     " + hobby)
    

# Call the function to get user information
introduce()

#Question2
# Grade checking
grade = int(input("Enter student`s marks: "))
if grade < 0 or grade > 100:
    print("Invalid Inputs, please enter between 0 to 100 ")
elif grade >= 80:
    print("students marks: " + str(grade))
    print("Grade A")
elif grade >= 70:
    print("students marks: " + str(grade))
    print("Grade B")
elif grade >= 60:
    print("students marks: " + str(grade))
    print("Grade C")
elif grade >= 50:
    print("students marks: " + str(grade))
    print("Grade D")
else:
    print("students marks: " + str(grade))
    print("Grade F")