#request for performing HTTP request
#BeautifulSoup for handling all HTML processing
import requests
from bs4 import BeautifulSoup

#raw_html=requests.get("http://www.fabpedigree.com/james/mathmen.htm")
#html=BeautifulSoup(raw_html.content,'html.parser')
#print(html.prettify())

#for i,li in enumerate(html.select('li')):
    #print(i, li.text)





def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)





def get_names():
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    raw_html = requests.get(url)
    #response=simple_get(url)
    html = BeautifulSoup(raw_html.content, 'html.parser')
    names=set()
    for li in html.select('li'):
        for name in li.text.split('\n'):
            if len(name)> 0:
                names.add(name.strip())
    return list(names)

        # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def get_hits_on_name(name):
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    response = requests.get(url_root.format(name)).content


    html = BeautifulSoup(response, 'html.parser')

    hit_link = [a for a in html.select('a')
                if a['href'].find('latest-60') > -1]

    if len(hit_link) > 0:
        # Strip commas
        link_text = hit_link[0].text.replace(',', '')
        try:
            # Convert to integer
            return int(link_text)
        except:
            log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None



print('Getting the list of names....')
names = get_names()
print('... done.\n')

results = []

print('Getting stats for each name....')

for name in names:
    try:
        hits = get_hits_on_name(name)
        if hits is None:
            hits = -1
        results.append((hits, name))
    except:
        results.append((-1, name))
        log_error('error encountered while processing '
                    '{}, skipping'.format(name))

print('... done.\n')

results.sort()
results.reverse()

if len(results) > 5:
    top_marks = results[:5]
else:
    top_marks = results

print('\nThe most popular mathematicians are:\n')
for (mark, mathematician) in top_marks:
    print('{} with {} pageviews'.format(mathematician, mark))

no_results = len([res for res in results if res[0] == -1])
print('\nBut we did not find results for '
        '{} mathematicians on the list'.format(no_results))