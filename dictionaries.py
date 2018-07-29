
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany');

print(capitals[ind_ger])

my_dist = {
    "spain": "madrid",
    "france": "paris",
    "germany": "berlin",
    "norway": "oslo"
}

print(my_dist)

keys = my_dist.keys()

values = my_dist.values()

print(keys)

print(values)

print(my_dist['spain'])

my_dist['italy'] = 'rome'

print(my_dist)

print('italy' in my_dist)

del(my_dist["norway"])

print(my_dist)

new_dist = {
    'spain': {'capital': 'madrid', 'population': 46.77},
    'france': {'capital': 'paris', 'population': 22.11},
    'bangladesh': {'capital': 'dhaka', 'population': 99.99},
    'china': {'capital': 'nai', 'population': 55.88},
}

print(new_dist)

capital = new_dist['bangladesh']['capital']
population = new_dist['bangladesh']['population']

print(capital)
print(population)

data = {'capital': 'delhi', 'population': 11.22}

new_dist['india'] = data

print(new_dist)



names = ['USA', 'UK', 'Bangladesh', 'India']
dr = [True, False, True, False]
cpc = [100, 200, 300, 400]


import pandas as pd


last_dist = {
    'country': ['USA', 'UK', 'Bangladesh', 'India'],
    'drive_right': [True, False, True, False],
    'car_per_cap': [100, 200, 300, 400]
}


cars = pd.DataFrame(last_dist)
print(cars)

row_labels = ['US', 'UK', 'BD', 'IN']

cars.index = row_labels

print(cars)

cars = pd.read_csv('cars.csv')

print(cars)

cars = pd.read_csv('cars.csv', index_col=0)

print(cars)

# panda series
print(cars['country'])  # [] checking data type

# data frame
print(cars[['country']])  # [[]] printing values

print(cars[0:1])  # Rows

print(cars[1:3])

print(cars[0:4])

print(cars.loc[['BD']])

print(cars.iloc[[1, 3]])

print(cars.loc[['UK'], ['car_per_cap']])

print(cars.loc[['UK', 'BD'], ['country', 'car_per_cap']])

print(cars.loc[:, 'drive_right'])  # data type

print(cars.loc[:, ['drive_right']])  # values

print(cars.loc[:, ['car_per_cap', 'country']])

'''

'''