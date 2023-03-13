# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет добавлять только новые
# вакансии/продукты в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты).
# Для тех, кто выполнил задание с Росконтролем - напишите запрос для поиска продуктов с рейтингом не ниже введенного или качеством не ниже введенного
# (то есть цифра вводится одна, а запрос проверяет оба поля).

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError                              # подключаем все необходимые модули и библиотеки
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

from pprint import pprint

url = 'https://hh.ru/search/vacancy'                                      # настройка сайта для парсинга
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36'}
job_name = input('Введите название вакансии: ')
# job_name = 'бухгалтер'
params = {'text': job_name, 'page': 0}

session = requests.Session()                                              # создание запроса к сайту с 0 страницы
answer = session.get(url, headers=headers, params=params)
answer_dom = BeautifulSoup(answer.text, 'html.parser')                    # преобразование полученного ответа к ДОМу
num_of_max_page = int((list(list(answer_dom.find('div', {'class': 'pager'}))[-2])[-1]).text)
vacancy_info_from_all_pages = []
vacancy_dict = {}
salary_info = []


client = MongoClient('127.0.0.1', 27017)                              # подключение к монго клиенту
db_hh = client.db_hh                                                  # создание базы данных для хранения информации о вакансиях HH


for i in range(num_of_max_page):
    vacancy_info = []
    params = {'text': job_name, 'page': i}
    answer = session.get(url, headers=headers, params=params)
    answer_dom = BeautifulSoup(answer.text, 'html.parser')
    all_vacancies = list(answer_dom.find_all('a', {'class': 'serp-item__title'}))
    all_salary = list(answer_dom.find_all('span', {'data-qa': 'vacancy-serp__vacancy-compensation',
                                                   'class': 'bloko-header-section-3'}))
    all_links = list(answer_dom.find_all('a', {'class': 'serp-item__title'}))
    all_companies = list(answer_dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-employer'}))

    for i in range(len(all_salary)):
        salary_info.append(all_salary[i].text)
    print(salary_info)

    for el in range(len(list(answer_dom.find_all('a', {'class': 'serp-item__title'})))):
        vacancy_dict['Название'] = all_vacancies[el].text
        vacancy_dict['Работодатель'] = all_companies[el].text
        vacancy_dict['Ссылка'] = all_links[el].get('href')
        vacancy_info.append(vacancy_dict)
        try:                                                                          #обработка ошибки
            db_hh.vacancies.insert_one(vacancy_dict)
            del vacancy_dict['_id']
        except DuplicateKeyError:
            print(f'ОШИБКА!!! Объект с id {vacancy_dict["_id"]} уже существует')
        vacancy_info_from_all_pages.append(vacancy_dict)



    for doc in db_hh.vacancies.find():
        pprint(f'Страница {i+1}: {doc}')
    sleep(2)


df = pd.DataFrame(vacancy_info_from_all_pages)


# БУХГАЛТЕР