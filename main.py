with open("./Input/Names/invited_names.txt", mode="r") as name:
    name_list = name.readlines()

new_name_list = []
for name in name_list:
    new_name_list.append(name.strip())

with open("./Input/Letters/starting_letter.txt", mode="r") as example:
    example_letter = example.read()

for edited_name in new_name_list:
    ready_letter = example_letter.replace('[name]', edited_name)

    with open(f"./Output/ReadyToSend/letter_for_{edited_name}.txt", mode="w") as letter:
        letter.write(ready_letter)
