import pandas

data = pandas.read_csv('Central-Park-Squirrel-Census-Squirrel-Data.csv')

# gray = 0
# black = 0
# cinnamon = 0

# Using for loop
# for x in data["Primary Fur Color"]:
#     if x == 'Gray':
#         gray += 1
#     elif x == 'Black':
#         black += 1
#     else:
#         cinnamon += 1

black = len(data[data['Primary Fur Color'] == 'Black'])
gray = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])


sq_dict = {
    'Squirrel Fur Color': ['Black', 'Gray', 'Cinnamon'],
    'Count': [black, gray, cinnamon]
}


sq_dict = pandas.DataFrame(sq_dict)
sq_dict.to_csv('color_count.csv')

data = pandas.read_csv('color_count.csv')
print(data)

