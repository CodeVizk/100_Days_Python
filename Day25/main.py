# import csv
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# To work with csv, even for a simple task we have to write lots of code
# so for ease python developers use Pandas library


import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
