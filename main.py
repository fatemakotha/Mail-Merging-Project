PLACEHOLDER = "[name]"



with open("invited_names.txt") as names_file:
    names = names_file.readlines() #converts each item to an item in a list **
    print(names)

with open("starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() #reads the entire file
    for name in names: #for each name in the list of names
        stripped_name = name.strip() #we strip the name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) #we replace [name] in he letter with our stripped names
        print(new_letter)

        with open(f"letter_for_{stripped_name}.txt", mode="w") as completed_letter: #we write a new letter for each name
            completed_letter.write(new_letter)
