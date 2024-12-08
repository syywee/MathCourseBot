import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


token='7843616127:AAGn8WMZFim-9XgMn-CwirVRdgzR4w7MFgY'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
  markup= types.ReplyKeyboardMarkup()
  markup.add(types.KeyboardButton('Пидорское'))
  markup.add(types.KeyboardButton('Фундаментальное'))
  bot.send_message(message.chat.id, "Начнем же смертельный бой", reply_markup= markup)
  bot.register_next_step_handler(message, on_click)
  
def on_click(message):
  if message.text == 'Пидорское':
    markup_1= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Компьютерные науки и АД')
    btn_2=types.KeyboardButton('Матстат и теорвер')
    markup_1.row(btn_1,btn_2)
    btn_4=types.KeyboardButton('Экономика')
    markup_1.row(btn_4)
    bot.send_message(message.chat.id, 'Педик', reply_markup= markup_1)
    #bot.register_next_step_handler(message, on_click_1)
  elif message.text == 'Фундаментальное':
    markup_2= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Алгебра')
    btn_2=types.KeyboardButton('Анализ')
    markup_2.row(btn_1,btn_2)
    btn_3=types.KeyboardButton('Теория чисел')
    btn_4=types.KeyboardButton('Геометрия')
    markup_2.row(btn_3,btn_4)
    bot.send_message(message.chat.id, 'Сначала разберемся с разделом:', reply_markup= markup_2)
    #bot.register_next_step_handler(message, on_click_2)
  
# def on_click_2(message):
#   if message.text == 'Компьютерные науки и АД':
    
    
    

bot.infinity_polling() 




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


# import fitz
# pdf_path = '+ course_book_2425.pdf'
# raw = []
# current = {}
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
#         name = raw[counter][:cc]
#         if raw[counter][-1].isnumeric():
#             page = raw[counter][-3::]
#         else:
#             page = raw[counter+1][-3::]
#             counter+=1
#         counter +=1
#         current[name] = page

# df = pd.DataFrame(list(current.items()), columns=['Ключи', 'Значения'])
# df.to_excel('output.xlsx', index=False)