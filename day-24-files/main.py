# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Read
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")
#
#
# with open("new_file.txt", mode="w") as file:
#     file.write("\nNew Text.")

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []

with open("./Input/Names/invited_names.txt", mode="r") as names:
    # invited_names = names.read()
    invited_names = names.readlines()

    for name in invited_names:
        formatted_name = name.replace("\n", "")
        names_list.append(formatted_name)

# print(names_list)

for name in names_list:
    with open("./Input/Letters/starting_letter.txt") as letter:
        example_letter = letter.read()
        new_letter = example_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_for:
            letter_for.write(new_letter)
