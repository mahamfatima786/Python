# Write a Python program that takes a number as input and prints Print Positive/Zero/Negative.

num = float(input("Enter the number:"))

if(num>0):
    print("You entered Positive number.")
elif(num<0):
    print("You entered Negative number.")
else:
    print("You entered Zero.")