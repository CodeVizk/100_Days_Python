#Q1 Solution -
#  in line 5 replace range (1,20) to range(1,21) as range function
# omits the stop value thus we are not getting the answer at 20 

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()


# Q2 Solution -
# We get index out of range error as a list index starts from 0 and here 
# we have items in list till index 5 and we have given range (1,6) so just revert the range to (0,5) to fix the error
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Q3 Solution -
# if we give input 1994 nothing is returned because in if else condition
# we have not specified what will happen if input is 1994 just add a less than equal sign in elif.

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Q4 Solution - 
# first error is indentation after if statement
# second error is age is taking a string as input but for the 
# if condition to work it needs an integer so we will declare int (input(.....))
# last error is in the print statement, age is not returned as  we have not wriiten fstring  
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# Q5 Solution -
# by using print statement we can narrow down our bug.

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages ={pages} word_per_page ={word_per_page})
# #we can deduce that word_per_page has an error through above print statement
# print(total_words)



# Q6 Solution -
# For complex code we use a debugger like Thonny or Pythontutor to check each line of code and
#  add breakpoint where the code is not working like it's intended to 
# In this code items in b_list is not appending each item as it is not in the loop so indent the line into the loop 

#  def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)





