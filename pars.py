import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
#
# #  - переназвать переменные чтобы не конфликтовали
# URL_TEMPLATE = "https://www.mi-ras.ru/index.php?c=noc2425_1"
# r = requests.get(URL_TEMPLATE)
# soup = bs(r.text, "html.parser")
# courses = (soup.find_all('script', language = None, type = None, src = None))
# # a = courses[courses.index('let semester'):courses.index("new Vue")]
# raw_mian = {}
# a= str(courses[0])
# # for i in a:
# #     print(i)
# #     print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
# import json
#
# # Пример JSON-строки, полученной из JavaScript
#
# # Преобразуем JSON-строку в словарь Python
# semester = json.loads(a)
#
# # Теперь вы можете обращаться к данным как к словарю
# print(semester['semid'])  # "2425-1"
# print(semester['y1'])     # 2024
# print(semester['announce']['text_rus'])  # "Просьба ко всем участникам НОЦ..."

# for name in courses:
#     print(name)
#     if name.a != None:
#         raw_mian[] = name.a['href']
# for k in raw_ium:
#     print(k, raw_ium[k])



# IUM
# URL_TEMPLATE = "https://mccme.ru/ru/nmu/courses-of-nmu/osen-20242025/"
# soup = bs(r.text, "html.parser")
# r = requests.get(URL_TEMPLATE)
# courses = soup.find_all('dd')
# raw_ium = {}
# for name in courses:
#     if name.a != None:
#         raw_ium[str(name.a)[(str(name.a).index('>') +1):-4]] = name.a['href']
# for k in raw_ium:
#     print(k, raw_ium[k])

# PDF
# import fitz
#
# pdf_path = '+ course_book_2425.pdf'
# raw = []
# current = {}
# final = []
#
# with fitz.open(pdf_path) as pdf:
#     for i in range(1, 6):
#         page = pdf[i]
#         text = page.get_text()
#         if text:
#             lines = list(text.split('\n'))
#             for _ in lines:
#                 if len(_) > 5 and ("Course descriptions" not in _):
#                     raw.append(_)
#     counter = raw.index("Описания курсов на русском") + 2
#     while counter < len(raw):
#         cc = -1
#         if '(' in raw[counter]:
#             cc = raw[counter].index("(")
#
#
#         name = raw[counter][:cc]
#         if raw[counter][-1].isnumeric():
#             page = raw[counter][-3::]
#         else:
#             page = raw[counter+1][-3::]
#             counter+=1
#         counter +=1
#         current[name] = page
#
#
# df = pd.DataFrame(list(current.items()), columns=['Ключи', 'Значения'])
# df.to_excel('output.xlsx', index=False)

