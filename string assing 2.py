# takes any word or sentence as input and prints: The first character, The last character, The total number of character.

word = input("Enter any word or sentence:")
print(f"The first character you enterd is  {word[0]}")
print(f"The last character you enterd is  {word[-1]}")
print(f"Total characters: {len(word)}")