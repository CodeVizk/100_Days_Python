#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"
# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    name = []
    for i in range(8):
        x = names.readline().strip()
        name.append(x)
    print(name)


# Replace the [name] placeholder with the actual name.
with open("./Input/Letters/starting_letter.txt") as base_letter:
    name_part = base_letter.read()

    for i in range(8):
        new_letter = name_part.replace(PLACEHOLDER, name[i])
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{name[i]}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)








