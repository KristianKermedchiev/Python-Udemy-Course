# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
    
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data['temp'].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)

# #Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)

#Createa a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

#2018 Squirrel Census
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241123.csv')

grey_squirrel = data[data['Primary Fur Color'] == "Gray"].count()
grey_squirrel_count = grey_squirrel[0]
red_squirrel = data[data['Primary Fur Color'] == "Cinnamon"].count()
red_squirrel_count = red_squirrel[0]
black_squirrel = data[data['Primary Fur Color'] == "Black"].count()
black_squirrel_count = black_squirrel[0]

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

squirrel_census = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [f"{grey_squirrel_count}", f"{red_squirrel_count}", f"{black_squirrel_count}"]
}

data_to_export = pandas.DataFrame(squirrel_census)
data_to_export.to_csv('new_data.csv')