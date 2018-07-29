# Create Arrays
import numpy as np
import pandas as pd

my_house = np.array([18.5, 20, 10, 9.50])
your_house = np.array([14, 24, 14.25, 9.0])

print("\n")

print(my_house >= 18)

print(my_house < your_house)

print("\n")


my_kitchen = 18.0
your_kitchen = 14.0

print(my_kitchen >10 and my_kitchen < 18)

print(my_kitchen > 14 or my_kitchen < 17)

print(np.logical_or(my_house > 18.5, my_house < 10))

print(np.logical_and(my_house < 11, my_house < 11))

print("\n")

room = "bed"
area = 15

if room == "amar":
    print("Its My Room")
elif room == "bed":
    print("ache bhai")
else:
    print("nai jao")

cars = pd.read_csv('cars.csv', index_col=0)

cpc = cars['car_per_cap']
many_cars = cpc > 200

car_maniac = cars[many_cars]

print(car_maniac)

# Check Assignment Below ---

for lab, row in cars.iterrows():
    print(lab + ": " + str(row["car_per_cap"]))

'''

'''