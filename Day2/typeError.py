#______________________________TypeError___________________________

#this will show an type_error as len works on int
len(234)



#This will show error as concantenation of int is not possible.
# TypeError: can only concatenate str

num_char=len(input("What is your name? "))

# print("your name has "+num_char+" characters.")



#_____________________________TypeCasting___________________________
#convert data type

# type(variable) will display the type of data

new_num_char=str(num_char) 
#will change the int to str then this code will work
print("your name has "+num_char+" characters.")






# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.

two_digit_number = input()
####################################
# Write your code below this line 👇

a=int(two_digit_number[0])
b=int(two_digit_number[1])
sum=a+b
print(sum)


sum=int(two_digit_number[0])+int(two_digit_number[1])
print(sum)
