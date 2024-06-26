import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(alphabet_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter your word - ").upper()
phonetic_word = [alphabet_dict[letter] for letter in user_word]

print(phonetic_word)
