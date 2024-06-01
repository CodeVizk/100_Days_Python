
def Guess_game():
  import random
  from GuessArt import logo
  print(logo)
  game_answer=random.randint(1,100)
  no_of_attempts=0
  Game_over=False
  print(game_answer)
  print("Welcome to the Number Guessing game!!\nI'm thinking of a number between 1 and 100.")
  difficulty=input("Choose a difficulty. Type 'Easy' or Hard':  ").lower
  if difficulty=="easy":
    no_of_attempts=10
    
  else:
    no_of_attempts=5
  print(f"You have {no_of_attempts} attempts remaining to guess the number.")
  while not Game_over :
    
    
    user_answer=int(input("Make a guess: "))
    if user_answer==game_answer:
      print(f"You got it. The answer is {user_answer}")
      Game_over=True
    elif user_answer>game_answer:
      print("Too high\nGuess again.")
      no_of_attempts-=1
      print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    else:
      print("Too low")
      no_of_attempts-=1
      print(f"You have {no_of_attempts} attempts remaining to guess the number.") 
    if no_of_attempts==0:
      print("You have run out of guesses. You lose")
      Game_over=True
  if input("Do you want to play again? Type y or n: ")=="y":
    Guess_game()
  else:
    print("GoodBye.")
Guess_game()