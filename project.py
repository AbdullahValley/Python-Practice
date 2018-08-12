import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get("http://www.worldometers.info/world-population/bangladesh-population/")

soup = BeautifulSoup(page.content, 'html.parser')

# Get All Tables from that Website
my_table = soup.find_all(class_="table table-striped table-bordered table-hover table-condensed table-list")

# First Table is for me, So I get it from Zero Index
temp = my_table[0]

# Here I'm getting Population Column
new_body = temp.select("strong")

population_list = []

# This Loop is for clear noise and make a perfect view list : Populations

for i, col_one in enumerate(new_body[:]):
    col_one = new_body[i].text.replace(',', '')
    population_list.append(int(col_one))

print(population_list)


# Getting differences from this bangladesh population list
diff_BD = []

for i, val in enumerate(population_list[:15]):
    light = val - population_list[i + 1]
    diff_BD.append(light)

print(diff_BD)


# Here I'm getting Years
for_get_year = temp.find_all("td")

year_list = []

# This Loop is for clear noise and get all years from that list : Years

for j in range(0, 208, 13):
    for zero in enumerate(for_get_year):
        zero = for_get_year[j].text.replace(',', '')
    year_list.append(int(zero))

print(year_list)

# Here I'm getting Growth Rate
get_growth = temp.find_all("td")

growth_list = []

# This Loop is for clear noise and get all growth rate from that list : Growth Rate

for k in range(6, 214, 13):
    for growth in enumerate(get_growth):
        growth = get_growth[k].text.replace(',', '')
    growth_list.append(growth)

print(growth_list)


# Here I'm getting World Population
get_world = temp.find_all("td")

world_population = []

# This Loop is for clear noise and get all growth rate from that list : Growth Rate

for k in range(11, 219, 13):
    for world in enumerate(get_world):
        world = get_world[k].text.replace(',', '')
    world_population.append(int(world))

print(world_population)

# Getting differences from this bangladesh population list
diff_world = []

for i, value in enumerate(world_population[:15]):
    tube = value - world_population[i + 1]
    diff_world.append(tube)

print(diff_world)


print("Difference Between World Population and Bangladesh Population")
difference = [a - b for a, b in zip(world_population, population_list)]
print(difference)

print('\n')

# This Data Frame is for create a perfect view table

population = pd.DataFrame({
        "Year": year_list,
        "Population": population_list,
        "Growth": growth_list,
        "World": world_population,
        "Difference": difference

    })

print(population)

print('\n')

# This Data Frame is for difference view

diff = pd.DataFrame({
        "Diff-BD": diff_BD,
        "Diff-World": diff_world

    })

print(diff)

# Here I'm reverse my data list for low to high view in Python Visualization
year_list.reverse()
population_list.reverse()
growth_list.reverse()
world_population.reverse()
difference.reverse()
diff_BD.reverse()
diff_world.reverse()


# After Reverse then I'm insert into new list
x = year_list
y = population_list
z = growth_list
w = world_population
d_bd = diff_BD
d_world = diff_world
d = difference


# Making Plot as well as Scatter for Years with Populations
plt.plot(x, y)
plt.scatter(x, y)

plt.title("Bangladesh Population")
plt.xlabel("Year")
plt.ylabel("Population")

plt.legend(["Population Plot", "Population Scatter"])
plt.show()

# Making Plot as well as Scatter for Years with Growth Rate
plt.plot(x, z)
plt.scatter(x, z)

plt.title("Population Growth Rate")
plt.xlabel("Year")
plt.ylabel("Growth Rate")

plt.legend(["Growth Plot", "Growth Scatter"])
plt.show()


plt.hist([d, w], color=['red', 'green'], bins=25)
plt.title('Comparison :: Bangladesh Vs World Population')
plt.legend(["Bangladesh Population", "World Population"])

plt.show()

# Bar

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()
