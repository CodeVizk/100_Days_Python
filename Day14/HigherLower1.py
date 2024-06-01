# Their are multiple ways to make this game and here is one of them with simpler terms used and not many functions defined

import random
from art import logo , vs
from game_data import data
# from replit import clear
 
# user_answer=""
def Higher_lower():
  current_score=0
  game_over=False 
 
  
  while not game_over:
    compare_a=random.choice(data)
    compare_b=random.choice(data)
    compare_a=compare_b
    while compare_a==compare_b:
      compare_b=random.choice(data)
    followers_of_a=compare_a['follower_count']
    followers_of_b=compare_b['follower_count'] 
  
    print(logo)
  
    print(f"Compare A: {compare_a['name']},a {compare_a['description']},from {compare_a['country']}")
    
    print(vs)
    
    print(f"Compare B: {compare_b['name']},a {compare_b['description']},from {compare_b['country']}")
    
    print(compare_a['follower_count'])
    print(compare_b['follower_count'])
    
    user_answer=input("Who has more following? Type 'A' or 'B' ")
    
    if user_answer=="a" and (followers_of_a>followers_of_b):
      current_score+=10
      print(f"You're right! current score={current_score}")
      compare_a=compare_b
    
    elif user_answer=="b" and (followers_of_b >followers_of_a):
      current_score+=1
      compare_a=compare_b
      print(f"You're right! current score={current_score}")    
    else:
      # clear()
      print(f"Sorry,that's Wrong. Final score= {current_score}")
      game_over=True

Higher_lower()
