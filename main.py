PLACEHOLDER = ['name']

with open("./Input/Names/invited_names.txt", mode="r") as name:
    name_list = name.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as example:
    example_letter = example.read()

    for name in name_list:
        stripped_name = name.strip()
        ready_letter = example_letter.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as letter:
            letter.write(ready_letter)
