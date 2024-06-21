import pandas

data = pandas.read_csv("weather_data.csv")

# To get mean of series

data_list = data["temp"].to_list()
# Below method is correct but pandas have inbuilt methods for computation

# avg = sum(data_list)/len(data_list)
# print(avg)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)


# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# Convert temperature on monday in Fahrenheit
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Jaam", "Rohan"],
    "scores": [23, 54, 34],
}

dataframe = pandas.DataFrame(data_dict)
print(dataframe)

# Convert our dataframe in many formats
# E.g
dataframe.to_csv("Dict.csv")