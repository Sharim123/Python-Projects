# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#        # print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data['temp'].to_list()
# # print((temp_list))
#
# print(data['temp'].max())

#columns
# print(data['condition'])
# print(data.condition)

#rows
#
# print(data[data.day == 'Monday' ])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == 'Monday']
# print(monday.condition)
# print((monday.temp*1.8)+32)
#
# data_dict = {
#     'students': ['bb', 'cc', 'dd'],
#     'scores': [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("easy.csv")
grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
print(grey_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

dd = (pandas.DataFrame(data_dict))
dd.to_csv('squirrel.csv')