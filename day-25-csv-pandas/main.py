# with open("weather_data.csv") as data:
#     print(data.readlines())

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg_temperature = round(data["temp"].sum() / data["temp"].count(), 2)
#
# print(avg_temperature)
# print(data["temp"].mean())

# max value in serie
# max_temp_value = data["temp"].max()
# print(max_temp_value)

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Challenge: Row data when temp was max
# print(data[data.day == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# def convert_celsius_to_fahrenheit(val):
#     return val * 1.8 + 32
#
#
# monday = data[data.day == "Monday"]
#
# monday_temp = monday.temp[0]
# monday_temp_F = convert_celsius_to_fahrenheit(monday_temp)

# print(monday["temp"][0])
# print(convert_celsius_to_fahrenheit(monday.temp))

# Create dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("data_data.csv")
#
# # print(data2)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250224.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colors": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")




























