import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


token='7843616127:AAGn8WMZFim-9XgMn-CwirVRdgzR4w7MFgY'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
  markup= types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton('Пидорское', callback_data='var1' ))
  markup.add(types.InlineKeyboardButton('Фундаментальное', callback_data='var2'))
  markup.add(types.InlineKeyboardButton('Общеобразовательное', callback_data='var3'))
  bot.send_message(message.chat.id, "Начнем же смертельный бой", reply_markup= markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
  if callback.data == 'var1':
    markup_1= types.InlineKeyboardMarkup()
    markup_1.add(types.InlineKeyboardButton('Анализ данных', callback_data='data_anal'))
    markup_1.add(types.InlineKeyboardButton('Матстат и теорвер', callback_data='satistics_probability'))
    markup_1.add(types.InlineKeyboardButton('Алгоритмы и структуры данных', callback_data='algoses'))
    markup_1.add(types.InlineKeyboardButton('Финансовая математика', callback_data='finaclial_math'))
    bot.send_message(callback.message.chat.id, 'Педик', reply_markup= markup_1)
  elif callback.data == 'var2':
    markup_2= types.InlineKeyboardMarkup()
    markup_2.add(types.InlineKeyboardButton('Алгебра', callback_data='algebra'))
    markup_2.add(types.InlineKeyboardButton('Анализ', callback_data='analisys'))
    bot.send_message(callback.message.chat.id, 'Сначала разберемся с разделом:', reply_markup= markup_2)
  elif callback.data == 'var3':
    markup_3= types.InlineKeyboardMarkup()
    markup_3.add(types.InlineKeyboardButton('Z', callback_data='algebra'))
    markup_3.add(types.InlineKeyboardButton('O', callback_data='analisys'))
    markup_3.add(types.InlineKeyboardButton('V', callback_data='analisys'))
    bot.send_message(callback.message.chat.id, 'Сначала разберемся с разделом:', reply_markup= markup_3)
  
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


import fitz
pdf_path = '+ course_book_2425.pdf'
raw = []
current = {}
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