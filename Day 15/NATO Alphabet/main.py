import pandas
# nato_code = {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
df = pandas.DataFrame(df)

nato_code = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
# print(nato_code)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input('Enter name: ').upper()
nato_encoding = {letter: nato_code[letter] for letter in word}
print(nato_encoding)
