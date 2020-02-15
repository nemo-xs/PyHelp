import requests

url = 'http://example.com'
par = {'key1':'value1', 'key2': 'value2'}
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
