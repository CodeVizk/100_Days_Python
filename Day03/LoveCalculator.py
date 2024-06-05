print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names=name1+name2
name=combined_names.lower()

t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")

first_digit=t+r+u+e


l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
second_digit=l+o+v+e


total_digit=int(str(first_digit)+str(second_digit))


if total_digit<10 or total_digit>90:
  print(f"Your score is {total_digit}, you go together like coke and mentos.")
elif total_digit>=40 and total_digit<=50:
  print(f"Your score is {total_digit}, you are alright together.")
else:
  print(f"Your score is {total_digit}.")