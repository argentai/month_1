import requests
from bs4 import BeautifulSoup
import csv

CSV = 'ycombinator_news.csv'
URL = 'https://news.ycombinator.com/news'
HOST = 'https://news.ycombinator.com'
HEADERS = {
         'User - Agent':
         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params, verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('table', class_='itemlist')


    l =[]
    for item in items:
        l.append({
            # 'Названия': item.find('tr', class_='athing').get_text(strip=True),
            # 'Цена': item.find('td', class_='titlelink').get_text(strip=True),
            #'Фото': item.find('div', class_='is-content').find('a').find('img').get('src'),
            'Комментарий': item.find('td', class_='title').find('a').get('href')
        })
    return l

def save(items, path):
    with open(path,'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Названия','Цена','Фото','Комментарий']) #записать в калонку
        for item in items:
            writer.writerow([item['Названия'], item['Цена'], item['Фото'], item['Комментарий']])

def pagination():
    PAGENATION = input("Введите количество страниц: ")
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        list_page =[]
        for page in range(1, PAGENATION):
            print (f"Страница {page} готова")
            html = get_html(URL, params={'page':page})
            list_page.extend(get_content(html.text))
        save(list_page, CSV)
        print("Парсинг готов")
    else:
         print("ERROR")

pagination()