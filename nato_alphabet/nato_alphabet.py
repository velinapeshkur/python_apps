import pandas

data = pandas.read_csv('nato_alphabet/nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in data.iterrows()}

word = input('Enter a word: ').upper()

codes = [alphabet_dict[letter] for letter in word]
print(codes)