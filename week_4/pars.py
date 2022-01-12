import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp

URL = 'https://news.ycombinator.com/news?p=1'
HOST = 'https://news.ycombinator.com'
HEADERS = {
 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'

}

r = requests.get(URL, headers=HEADERS, verify=False)
print(r)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
items = soup.findAll('td', class_='title')
pp(items)


with open ("item.txt", "a") as f:
 f.write(str(items))
with open ("item.txt", "r") as ff:
 pp(ff.read())