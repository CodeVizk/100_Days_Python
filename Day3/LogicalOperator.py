print("Welcome to Roller Coaster ride!!!!!")


height=int(input("Enter your height- "))
bill=0
if height>=120:
  print("You can enter.")
  age=int(input("Enter your age- "))
  if age<12:
    print("Child tickets are 40rs. ")
    bill+=40
  elif age>=45 and age <=55:
    print("Everything going to be ok. Have a ride on us.")  
    bill=0
  elif age<18:
    print("Teens tickets are 50rs. ")
    bill+=50    
  else:
    print("Adult tickets are 70rs.")
    bill+=70
  wants_photo=input("Do you want a photo? Enter Y or N ")
  if wants_photo=="Y" :
    bill+=50
  print(f"Total bill is {bill}rs")  
else:
  print("You cannot ride this ride.")