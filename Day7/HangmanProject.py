#Step 1
# print (word_list[random_choice])

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.ep 1 

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)

print(chosen_word)

guess=input("Guess the letter- ").lower()

for letter in chosen_word:
  if guess==chosen_word[letter]:
    print("Right")
  else:
    print("Wrong")
    