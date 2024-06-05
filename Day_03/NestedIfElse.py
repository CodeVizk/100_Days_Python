print("Welcome to Roller Coaster ride!!!!!")

height=int(input("Enter your height- "))
if height>=120:
  print("You can enter.")
  age=int(input("Enter your age- "))
  if age<12:
    print("Child tickets are 40rs. ")
  elif age<18:
    print("Teens tickets are 50rs. ")
  else:
    print("Adult tickets are 70rs.")
else:
  print("You cannot ride this ride.")