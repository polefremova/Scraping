# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH(обязательно)
# и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
# Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия.
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов.
# Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.

import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = 'https://hh.ru/search/vacancy'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.3.949 Yowser/2.5 Safari/537.36'}
job_name = input('Введите название вакансии: ')
job_name = 'бухгалтер'
params = {'text': job_name, 'page': 0}


session = requests.Session()
answer = session.get(url, headers=headers, params=params)
answer_dom = BeautifulSoup(answer.text, 'html.parser')
num_of_max_page = int((list(list(answer_dom.find('div', {'class': 'pager'}))[-2])[-1]).text)
vacancy_info_from_all_pages = []
vacancy_dict = {}


for i in range(num_of_max_page):
    vacancy_info = []
    params = {'text': job_name, 'page': i}
    answer = session.get(url, headers=headers, params=params)
    answer_dom = BeautifulSoup(answer.text, 'html.parser')
    all_vacancies = list(answer_dom.find_all('a', {'class': 'serp-item__title'}))
    # all_salary = list(answer_dom.find_all('span', {'data-qa': 'vacancy-serp__vacancy-compensation',
    #                                                'class': 'bloko-header-section-3'}))
    all_links = list(answer_dom.find_all('a', {'class': 'serp-item__title'}))
    all_companies = list(answer_dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-employer'}))

    for el in range(len(list(answer_dom.find_all('a', {'class': 'serp-item__title'})))):
        vacancy_dict['Название'] = all_vacancies[el].text
        vacancy_dict['Работодатель'] = all_companies[el].text
        vacancy_dict['Ссылка'] = all_links[el].get('href')
        vacancy_info.append(vacancy_dict)
        vacancy_info_from_all_pages.append(vacancy_dict)
    print(f'Страница {i+1}: {vacancy_info}')
    sleep(2)
    
df = pd.DataFrame(vacancy_info_from_all_pages)