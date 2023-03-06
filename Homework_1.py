import requests
from bs4 import BeautifulSoup
from pprint import pprint

# url = 'https://hh.ru/vacancies/stilist'
url = 'https://hh.ru/search/vacancy'

session = requests.Session()
response = session.get(url)
dom = BeautifulSoup(response.text, 'html.parser')
pprint(dom)