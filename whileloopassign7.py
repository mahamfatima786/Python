# Write a program to print the multiplication table of any number using a while loop.

table = int(input("Enter a number:"))

n = 1
while(n<=10):
    print(f"{table} x {n} = {table*n}")
    n += 1