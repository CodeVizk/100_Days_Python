import random
def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card= random.choice(cards)
  return card

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card)
  computer_cards.append(deal_card)

game_over=False
def calculate_score(cards):
  """Takes a list of cards and return the score calculated from the cards"""
  if sum(cards)==21 and len(cards)==2:
     return 0
  if 11 in cards and sum(cards)>21:
    cards.append(1) 
    cards.remove(11)



    
  
