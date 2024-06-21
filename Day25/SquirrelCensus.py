import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240621.csv")
color_list = squirrel_data["Primary Fur Color"].tolist()
color1 = sum(squirrel_data["Primary Fur Color"] == "Black")
print(color1)
color2 = sum(squirrel_data["Primary Fur Color"] == "Gray")
print(color2)
color3 = sum(squirrel_data["Primary Fur Color"] == "Cinnamon")
print(color3)

my_dict = {
    "FurColor": ["Gray", "Cinnamon", "Black"],
    "Count": [color2, color3, color1],
}
my_data = pd.DataFrame(my_dict)
print(my_data)
my_data.to_csv("SquirrelCount.csv")