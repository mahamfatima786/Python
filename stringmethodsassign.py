#  Takes a sentence as input, Converts it to lowercase, Replaces all spaces with underscores.
sent = input("Enter the Sentence:")
print(sent.lower()) # Converts all characters to lowercase.
print(sent.replace(" ","_")) # Replaces all occurrences.

# Formatted Strings (f-Strings) 
name = "Quantessa"
age = 21 
print(f"My name is {name} and I am {age} years old.") 