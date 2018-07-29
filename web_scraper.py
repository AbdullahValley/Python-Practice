import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

# print(page)

# print(page.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# print(soup)

# print('\n')

page_second = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup_2 = BeautifulSoup(page_second.content, 'html.parser')

# print(soup_2)

print('\n')

a = soup_2.find_all('p')

# print(a)

b = soup_2.find_all(class_="outer-text")

# print(page_second.content)

# print(b)

c = soup_2.find_all(id="first")

# print(c)

# d = soup_2.select(div)

# print(d)

page_three = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.W1QhYnYzZaY")

soup_3 = BeautifulSoup(page_three.content, 'html.parser')

seven_days = soup_3.find(id="seven-day-forecast")

forecast_items = seven_days.find_all(class_="tombstone-container")

tonight = forecast_items[3]

# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

# print(period)
# print(desc)
# print(temp)

period_tags = seven_days.select(".tombstone-container .period-name")
periods = [abc.get_text() for abc in period_tags]
print(periods)


'''
import pandas as pd

weather = pd.DataFrame(["period":periods])

print(weather)


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Assignment :: # Home Work >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



'''

