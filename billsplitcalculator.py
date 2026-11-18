# Write a program that takes total bill amount and number of friends as input.Calculate how much each person will pay.Also print the data type of each variable used.

bill = float(input("Total bill:"))
friends = int(input("Friends:"))
pay = bill / friends

print("Each will pay:", pay)

print("The datatype of bill is", type(bill))
print("The datatype of friends is", type(friends))
print("The datatype of pay is", type(pay))