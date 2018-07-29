import requests
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
    population_list.append(col_one)

print(population_list)

# Here I'm getting Years
for_get_year = temp.find_all("td")

year_list = []

# This Loop is for clear noise and get all years from that list : Years

for j in range(0, 208, 13):
    for zero in enumerate(for_get_year):
        zero = for_get_year[j].text.replace(',', '')
    year_list.append(zero)

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


# This Data Frame is for create a perfect view table

population = pd.DataFrame({
        "Year": year_list,
        "Population": population_list,
        "Growth": growth_list

    })

print(population)

# Here I'm reverse my data list for low to high view in Python Visualization
year_list.reverse()
population_list.reverse()
growth_list.reverse()

# After Reverse then I'm insert into new list
x = year_list
y = population_list
z = growth_list

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
