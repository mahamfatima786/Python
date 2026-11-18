# Write a program that prints the sum of first n natural numbers. 

num = int(input("Enter Natural Number:"))

sum = 0
while(num>=1):
    sum = sum + num
    num = num - 1

print("Sum =",sum)
print("Number =",num)