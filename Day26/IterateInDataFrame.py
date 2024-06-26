data_dict = {
    "student": ["Vivek", "Maddy", "Rohan"],
    "score": [59, 34, 23]
}

# Looping through dictionary
# for (key, value) in dict.items():
#     print(key, value)


import pandas
dataframe = pandas.DataFrame(data_dict)
# print(dataframe)

# Looping through dataframe
# for key, value in dataframe.items():
#     print(value)

# is not very useful therefore there is iterrows function
for (index, row) in dataframe.iterrows():
    # print(row)
    # print(row.student)
    if row.student == "Vivek":
        print(row.score)
