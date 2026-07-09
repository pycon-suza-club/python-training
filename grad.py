
marks = int(input("Inter your marks:  "))
print("Student Marks: ",marks)
if marks <= 100:
    print("Grade: A")
elif marks <= 79:
    print("Grade: B")
elif marks <= 69:
    print("Grade: C")
elif marks <= 59:
    print("Grade: D")
elif marks <= 49:
    print("Grade: F")
else:
    print("That is not the marks! ")