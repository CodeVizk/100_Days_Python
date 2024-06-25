# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called weather_f
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f use this formula:
#
# (temp_c * 9/5) + 32 = temp_f
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
#
# The eval() function will help us convert the string input into a Python dictionary,
# provided that the inputs are already formatted with the correct syntax.
#
# Example Input
# {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# Example Output
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2, 'Friday': 69.8,
# 'Saturday': 71.6, 'Sunday': 75.2}


weather_c = eval(input())
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day: temp_f*9/5 + 32 for (day, temp_f ) in weather_c.items()}

print(weather_f)