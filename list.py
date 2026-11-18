# List in python:)

foods = ["Samosa", "Pizza",  "GulabJamun", "Burger"]
print(foods[0])
print(foods[3])
print(foods)
foods[0] = "Barfi"
print(foods)
#Slicing in List:)

marks = [87, 64, 33, 95, 76]
print(marks[1:4])
print(marks[:3])
print(marks[-3:-1])

# List Functions:)

print(len(foods)) # Returns length
print(max(foods)) # Largest value
print(min(foods)) # Smallest value

# Common List Methods:)

print(foods.append("Biriyani")) # Adds at end 
print(foods.sort()) # Sorts ascending
print(foods.reverse()) # Reverses list
print(foods.pop(5)) # Removes at index
print(foods.insert("Shawarma" , "Ladu")) # Inserts at index
print(foods.remove("Shawarma")) # Removes first occurrence
