'''while condition :
    expression'''

# Initialize offset
offset=8

# Code the while loop
while offset !=0 :
    print("correcting...")
    offset=offset-1
    print(offset)


# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset=offset-1
    else :
       offset=offset+1
    print(offset)


areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for area in areas:
    print(area)

#print index value and list value
for h,a in enumerate(areas) :
    print("room " + str(h) +": "+str(a))


'''house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
 prints out the x is y sqm, where x is the name of the room and y is the area of the room. '''

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

'''world = { "afghanistan":30.55, 
          "albania":2.77,
          "algeria":39.21 }
        
  afghanistan --- 30.55  '''



import numpy as np

height= [1.73,1.68,1.71,1.89,1.79]
np_height=np.array(height)
np_baseball=np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
               [65.4, 59.2, 63.6,88.4,68.7]])


# For loop over np_height
for x in np_height:
  print( x,"inches")



# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)


# Adapt for loop
for lab, row in cars.iterrows() :
   print(lab + ": "+ str(row["cars_per_cap"]))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"]=(row["country"]).upper()


print(cars)


# Use .apply(str.upper)
cars["COUNTRY"]=cars['country'].apply(str.upper)
print(cars)