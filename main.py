# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help https://www.w3schools.com/python/ref_string_strip.asp
list_names = []

with open("invited_names.txt") as names_file:
    names = names_file.readlines() #converts each item to an item in a list **
    print(names)