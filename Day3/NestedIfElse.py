print("Welcome to Roller Coaster ride!!!!!")

height=int(input("Enter your height- "))
if height>=120:
  print("You can enter.")
  age=int(input("Enter your age- "))
  if age<12:
    print("Please pay 40rs. ")
  elif age<18:
    print("Please pay 50rs. ")
  else:
    print("Please pay 70rs.")
else:
  print("You cannot ride this ride.")