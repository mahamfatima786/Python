# "if-elif-else" Conditional Statement

marks = float(input("Enter your marks: "))

if(marks >= 90):
    print("Your grade is A+.")
elif(marks >= 80):
    print("Your grade is A.")
elif(marks >= 70):
    print("Your grade is B+.")
elif(marks >= 60):
    print("Your grade is B.")
elif(marks >= 50):
    print("Your grade is C.")
elif(marks >= 40):
    print("Your grade is D.")
else:
    print("Your grade is F.")