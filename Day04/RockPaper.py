rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

mode=[rock,paper,scissors]
c_mode=[rock,paper,scissors]


user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice >=3 or user_choice<0:
  print("Invalid number You lose.")
else:  
  user_chance=print(mode[user_choice])

  random_effect=random.randint(0,2)
  comp_choice=random_effect
  print("\nComputer chose.")
  comp_chance=print(c_mode[random_effect])




  user_chance

  comp_chance 
  if user_choice==comp_choice:
    print("It's a draw...")
  elif user_choice==1 and comp_choice ==0 :
    print("You win")
  elif user_choice==0 and comp_choice ==1 :
    print("You lose")
  elif user_choice==2 and comp_choice ==0 :
    print("You lose")
  elif user_choice==0 and comp_choice ==2 :
    print("You win")
  elif user_choice < comp_choice:
     print("You lose")
  elif user_choice > comp_choice:
    print("You won")