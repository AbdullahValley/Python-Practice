import requests
import pandas as pd
from bs4 import BeautifulSoup

raw_html = requests.get('http://www.fabpedigree.com/james/mathmen.htm')

html = BeautifulSoup(raw_html.content, 'html.parser')

names = set()
for li in html.select('li'):
    for name in li.text.split('\n'):
        if len(name) > 0:
            names.add(name.strip())


name_list = list(names)

hits_count_list = []
name_count_list = []

for all_name in name_list[1:14]:
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    response = requests.get(url_root.format(all_name))

    if response is not None:

        html = BeautifulSoup(response.content, 'html.parser')

        hit_link = [my_data for my_data in html.select('a')
                    if my_data['href'].find('latest-60') > -1]
        if len(hit_link) > 0:
            link_text = hit_link[0].text.replace(',', '')

    sobar_hit = int(link_text)

    hits_count_list.append(sobar_hit)
    #print(hit_link)
    #print(all_name)
    name_count_list.append(all_name)


final_job = pd.DataFrame({
    "Name": name_count_list,
    "Hits": hits_count_list

})
print(final_job)
