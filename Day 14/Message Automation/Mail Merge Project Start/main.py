# for each name in invited_names.txt
with open('input/Names/invited_names.txt') as name_list:
    name = name_list.readlines()

letters = []

with open('input/Letters/starting_letter.txt') as starting:
    starting_letter = starting.read()
    for index in range(len(name)):
        letter = starting_letter.replace('[name]', name[index].strip('\n'))
        letters.append(letter)

count = 1
for letter in letters:
    with open(f'Output/ReadyToSend/letter{count}.txt', mode='w') as final_letter:
        final_letter.write(letter)
    count += 1
