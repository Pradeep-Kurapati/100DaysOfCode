import pandas

data = pandas.read_csv('weather-data.csv')

# Converting temp column into list
temp_list = data['temp'].to_list()

# mean using series method
print(round(data['temp'].mean(), 2))

# Finding highest number using Series method
print(data.temp.max())

#  The row which has highest temperature of the week
# print(data[data.temp == data.temp.max()])

# Converting Monday's temperature to Fahrenheit
monday = data[data.day == 'Monday']
monday_temp = int(monday.temp)
monday_temp = monday_temp * 9/5 + 32
print(f'{monday_temp}F')
