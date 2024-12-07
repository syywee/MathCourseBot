import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# URL_TEMPLATE = "https://mccme.ru/ru/nmu/courses-of-nmu/osen-20242025/"
# r = requests.get(URL_TEMPLATE)
# soup = bs(r.text, "html.parser")
# # cours_names = list(set(map(str, soup.find_all('dd'))))
# raw = set(soup.find_all('dd'))
#
# c = 0
# for name in raw:
#     separ = (str(name.a)).find(">") +1
#     c+=1
#     # print(str(name.a)[separ:-4], name.a["href"], c)
#     print(name)
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# # URL страницы для парсинга
# url = 'https://old.mccme.ru/ium/s24/s24.html'
# # Отправляем GET-запрос к странице
# response = requests.get(url)
#
# # Проверяем, что запрос выполнен успешно
# if response.status_code == 200:
#     # Парсим содержимое страницы
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Находим все элементы, содержащие названия курсов и ссылки
#     courses = []
#     for item in soup.select('dd'):  # Измените селектор в зависимости от структуры страницы
#         print(item)

import fitz  # PyMuPDF

# Путь к вашему PDF-файлу
pdf_path = '+ course_book_2425.pdf'
raw = []
current = {}
final = []
# Функция для извлечения оглавления
# def extract_contents(pdf_path):
#     contents = []
#     # Открываем PDF-файл
#     with fitz.open(pdf_path) as pdf:
#         for i in range(1, 6):
#             page = pdf[i]
#             text = page.get_text()
#             if text:
#                 lines = list(text.split('\n'))
#                 start = lines.index("Описания курсов на русском")
#                 for _ in range(start, len(lines)):
#                     print(lines[_])
#                     contents.append((lines[_].strip(), i + 1))  # i + 1, так как страницы начинаются с 1
#     return contents
#
# # Извлекаем оглавление
# contents = extract_contents(pdf_path)
#
# # Выводим названия курсов и номера страниц
# for course, page in contents:
#     print(f"Курс: {course}, Страница: {page}")
with fitz.open(pdf_path) as pdf:
    for i in range(1, 6):
        page = pdf[i]
        text = page.get_text()
        if text:
            lines = list(text.split('\n'))
            for _ in lines:
                if len(_) > 5 and ("Course descriptions" not in _):
                    raw.append(_)
    counter = raw.index("Описания курсов на русском") + 2
    while counter < len(raw):
        cc = -1
        if '(' in raw[counter]:
            cc = raw[counter].index("(")


        name = raw[counter][:cc]
        if raw[counter][-1].isnumeric():
            page = raw[counter][-3::]
        else:
            page = raw[counter+1][-3::]
            counter+=1
        counter +=1
        current[name] = page


df = pd.DataFrame(list(current.items()), columns=['Ключи', 'Значения'])
df.to_excel('output.xlsx', index=False)
