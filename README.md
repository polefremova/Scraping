# Урок 1. Основы клиент-серверного взаимодействия. Работа с API
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide). Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.



# Урок 2. Парсинг данных. HTML, DOM, XPath
Написать приложение и функцию, которые собирают основные новости с сайта на выбор dzen.ru, lenta.ru, mail.ru . Для парсинга использовать XPath
Структура данных должна содержать:
* название источника
* наименование новости
* ссылку на новость
* дата публикации

минимум один сайт максимум все



# Урок 3. Парсинг данных. HTML, Beautiful Soap
Вариант 1
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.
