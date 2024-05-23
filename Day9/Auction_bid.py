# To use clear function easily try this code in replit by removing the comment sign
# from replit import clear 

from art_auction import logo
print(logo)

def bid_winner(bidding_record):
  highest_bid=0
  highest_bidder=""
  for bidders in bidding_record:
    bid_price=bidding_record[bidders]
    if bid_price>highest_bid:
      highest_bid=bid_price
      highest_bidder=bidders 
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

action=True
bidder={}

while action:
  name_of_bidder=str(input("What is your name?: "))
  bidding_amount=int(input("What is your bid?: $"))
  bidder[name_of_bidder]=bidding_amount
  new_bidder=str(input("Are there any other bidders? type yes or no "))
  if new_bidder=="no":
    action=False
    bid_winner(bidder)
  # elif new_bidder=="yes":
    # clear()
