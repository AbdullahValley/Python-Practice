
offset = 4

while offset != 0:
    print("Testing ...")
    offset = offset - 1
    print(offset)


offset = -3

while offset != 0:
    print("Testing ...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


print("\n")

areas = [1, 2, 3, 4, 5]

for test in areas:  # areas is list name
    print(test, end=' ')   # Assignment Print Without New Line
    # print(test)


print("\n")


# print index value and list value
for h, a in enumerate(areas):
    print("room " + str(h) + ": " + str(a))

'''
for h, a in enumerate(areas):
    print("room " + str(h) + ": " + str(a))  # Assignment Print Without str()

#  How to print in a single line int and string (Google)


# House list of lists

house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
 prints out the x is y sqm, where x is the name of the room and y is the area of the room.
  
  x[0] x[1]
  
'''


house = [
        ["hallway", 11.25],
        ["kitchen", 18.0],
        ["living room", 20.0],
        ["bathroom", 9.50]
        ]

# print("\nHere " + str(house[1][0]) + " point is " + str(house[1][1]))

# print("\nHere " + format(house[1][0]) + " point is " + format(house[1][1]))

print("\nHere " + format(house[2][0]) + " point is " + format(house[2][1]))

print("\n")

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

print("\n")

world = {'afghanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}

for key, value in world.items():
    print(key + " -------- " + str(value))

print("\n")

import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
np_height = np.array(height)
np_baseball = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
               [65.4, 59.2, 63.6, 88.4, 68.7]])


# For loop over np_height
for x in np_height:
    print(x, "inches")

print("\n")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

# Import cars data

import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars

for lab, row in cars.iterrows():
    print(lab)
    print(row)

print("\n")

# Adapt for loop

for lab, row in cars.iterrows():
    print(lab + ": " + str(row["car_per_cap"]))


# Code for loop that adds COUNTRY column

for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = (row["country"]).lower()


print(cars)

print("\n")

# Use .apply(str.upper)

cars["COUNTRY"] = cars['country'].apply(str.upper)
print(cars)

'''

'''