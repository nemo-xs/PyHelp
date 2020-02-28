import requests


# region #* HTTP запросы, библиотека requests ---------------------------------
# ** https://stepik.org/lesson/24471/step/1?unit=6780
"""
в http протоколе объявлено несколько методов
#** get - запрос html кода, картинок и тп. не изменяет данные на сервере.
возвращает response object, где response это класс, описанный внутри requests
в качестве атрибутов там есть статус коды, хедеры, и само содержимое (см ниже)
#? res = requests.get('http://rabbitroom.ru/')  # сам запрос
#? print(res.status_code)  # код ответа (200, 404 и.т.д.)
#? print(res.url)  # вывод url страницы
#? print(res.headers["Content-Type"])  # словарь headers, значение Content-Type
#? print(res.content)  # содержимое ответа в бинарном виде
#? print(res.text)  # содердимое ответа в виде такста
#** post - предназначен для изменения данных на сервере. Смена паролей,
банковские транзакции и другая инфо, которая пОстится
#** res - response - ответ на запрос от сервера. Сначала код ответа (200, 404,
503) затем служебная информация, пустая строка и сам ответ.
"""
# #* format stroke на примере requests
# template = "Response from {0.url} whith code {0.status_code}"
# res = requests.get('http://rabbitroom.ru/')
# print(template.format(res))
""" #* Пример записи в файл полученного ответа (картинка)
whith open("file.png", "wb") as f:
    f.write(res.content)
"""
# endregion -------------------------------------------------------------------


url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
cookies = {'cookies_are': 'working'}

r = requests.get(url, params=par, cookies=cookies)
# стандартный запрос при парсинге (par&cookies - не обязательные)

print(r.text)  # вывод текстового ответа от сервера (response)
print(r.url)  # адрес который сформировался с учетом всех параметров
print(r.content)  # все содержимое полученное от сервера
print(r.cookies['example_cookies_name'])  # принимать куки от сервера

# * Пример запроса url из файла, получения текста из файла на сервере и подсчет
# // количества строк в этом тексте

# file = open('dataset_3378_2.txt', 'r')
# url = file.readline().strip()

# r = requests.get(url)
# text = r.text
# print(text)
# ls = len(text.splitlines())
# print(ls)

# * Пример цикла, который меняет окончание url (берет из списка файлов)

# file = open('dataset_3378_3.txt', 'r')
# url = file.readline().strip()
# r = requests.get(url)

# while r.text[0] != "We":
#     url = "https://stepic.org/media/attachments/course67/3.6.3/"+r.text.strip()
#     r = requests.get(url)
#     print(r.url)
