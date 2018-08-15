from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = requests.get("https://www.rottentomatoes.com/")

soup = BeautifulSoup(BASE_URL.content, 'html.parser')


get_table = soup.find('table', {"class": "movie_list", "id": "Top-Box-Office"})


get_left = []


for my_left in get_table.find_all('td', {"class": "left_col"}):
    left_values = my_left.get_text()
    get_percentage = left_values[:].strip('\n')
    get_left.append(get_percentage)

print(get_left)


get_middle = []


for my_middle in get_table.find_all('td', {"class": "middle_col"}):
    middle_values = my_middle.get_text()
    get_title = middle_values[:].strip('\n')
    get_middle.append(get_title)

print(get_middle)


get_right = []


for my_right in get_table.find_all('td', {"class": "right_col"}):
    right_values = my_right.get_text()
    get_worth = right_values[:].strip('\n')
    get_right.append(get_worth)

print(get_right)


print('\n')

movies = pd.DataFrame({
        "Box Office %": get_left,
        "Title": get_middle,
        "Worth": get_right

    })

print(movies)


plt.scatter(get_left, get_right)

plt.title("THE BOX OFFICE")
plt.xlabel("Box Office Percentage")
plt.ylabel("Business Worth")

plt.show()
