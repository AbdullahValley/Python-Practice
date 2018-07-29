import requests

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

print(page)

print(page.content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

print('\n')
a=soup.find_all('p')
print(a)

print('\n')
b=soup.find_all(class_="outer-text")
print(b)
print('\n')

c=soup.find_all(id="first")
print(c)
print('\n')

d=soup.select("div p")
print(d)
print("\n")


page=requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W0iuPNIzY2w")
soup=BeautifulSoup(page.content,'html.parser')
seven_day=soup.find(id="seven-day-forecast")
forecast_items=seven_day.find_all(class_="tombstone-container")
tonight=forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)

img = tonight.find("img")
desc = img['title']
print(desc)
print('\n')

period_tags=seven_day.select(".tombstone-container .period-name")
periods=[a.get_text() for a in period_tags]
print(periods)

short_descs=[b.get_text() for b in seven_day.select(".tombstone-container .short-desc")]
print(short_descs)

temps=[c.get_text() for c in seven_day.select(".tombstone-container .temp")]
print(temps)

descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(descs)



import pandas as pd
weather = pd.DataFrame({
        "desc":descs,
        "period": periods,
        "short_desc": short_descs,
        "temp": temps

    })

print(weather)


is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)

print(weather[is_night])