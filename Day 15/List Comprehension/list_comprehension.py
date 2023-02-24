numbers = [1, 2, 3]
new_item = [n+1 for n in numbers]
name = 'Pradeep Chand'
new_name = [letter for letter in name]
double = [n*2 for n in range(2,5)]
names = ['caroline', 'freddie', 'eleanor', 'alex', 'jim']
short_names = [name.upper() for name in names if len(name) > 5]