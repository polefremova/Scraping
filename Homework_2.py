# Написать приложение и функцию, которые собирают основные новости с сайта на выбор dzen.ru, lenta.ru, mail.ru . Для парсинга использовать XPath
# Структура данных должна содержать:
# * название источника
# * наименование новости
# * ссылку на новость
# * дата публикации
# минимум один сайт максимум все


import requests
from pprint import pprint
from lxml import html
import datetime

url = 'https://lenta.ru/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.2.931 Yowser/2.5 Safari/537.36'}
session = requests.Session()

report = session.get(url, headers = headers)
dom = html.fromstring(report.text)

all_info = []
top_news = dom.xpath("//div[@class='topnews__column']/a/div/span/text()")

for i in range(len(top_news)):
    dict_news = {}
    dict_news['Заголовок'] = dom.xpath("//div[@class='topnews__column']/a/div/span/text()")[i]
    dict_news['Ссылка'] = dom.xpath('//a[contains(@class, "card-mini _topnews")]//@href')[i]
    date = datetime.date.today()
    time = dom.xpath("//a[contains(@class, 'card-mini _topnews')]/div/div/time[@class='card-mini__date']/text()")[i]
    dict_news['Дата и время новости'] = str(date) + '    ' + str(time)

    all_info.append(dict_news)

pprint(all_info)