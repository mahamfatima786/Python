# Write a program that takes your favorite food name as input and prints: The middle 3 characters, The last 2 characters.

food = input("Enter your favorite food: ")
n = len(food)
mid = n // 2
print(f"Middle 3 characters: {food[mid-1:mid+2]}")
print(f"Last 2 characters: {food[-2:]}")
