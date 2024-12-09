import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


token='7843616127:AAGn8WMZFim-9XgMn-CwirVRdgzR4w7MFgY'
bot=telebot.TeleBot(token)
data = pd.read_csv('Raw_Table - Sheet1.csv')

def searcher(course_type):
    message = []
    for index, row in data[data[course_type] == 1.0].iterrows():
        if row['link'][1:].isdigit() == True: 
            link_course = f'<b>Подробнее о курсе:</b> https://www.dropbox.com/scl/fi/26o842k1rxnnhkzkg6wpu/course_book_2425.pdf?rlkey=x3qdfggkfnz67ab9bgoe0egyo&e=2&dl=0<br> <b>Страница</b>: {row["link"]}.<br>'
        else:
            link_course = f'<b>Ссылка на страницу курса НМУ</b>: {row["link"]}<br>'   
        strochka_v_message = f'<b>Название курса:</b> {row["name"]}.<br> <b>Сложность курса</b>: {int(row["lvl"])}. {link_course}'
        message.append(strochka_v_message)
    return message


@bot.message_handler(commands=['start'])
def start_message(message):
  markup= types.ReplyKeyboardMarkup()
  markup.add(types.KeyboardButton('Прикладные'))
  markup.add(types.KeyboardButton('Фундаментальные'))
  bot.send_message(message.chat.id, "Выберите, пожалуйста, какие курсы Вы рассматриваете для внесения в свой иуп:", reply_markup= markup)
  bot.register_next_step_handler(message, on_click)
  
def on_click(message):
  if message.text == 'Прикладные':
    markup_1= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Компьютерные науки и АД')
    btn_2=types.KeyboardButton('Матстат и теорвер')
    markup_1.row(btn_1,btn_2)
    btn_4=types.KeyboardButton('Экономика')
    markup_1.row(btn_4)
    bot.send_message(message.chat.id, 'К какому из основных разделов прикладных курсов Вы склоняетесь?', reply_markup= markup_1)
    bot.register_next_step_handler(message, on_click_1)
  elif message.text == 'Фундаментальные':
    markup_2= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Алгебра')
    btn_2=types.KeyboardButton('Анализ')
    markup_2.row(btn_1,btn_2)
    btn_3=types.KeyboardButton('Теория чисел')
    btn_4=types.KeyboardButton('Геометрия')
    markup_2.row(btn_3,btn_4)
    bot.send_message(message.chat.id, 'Выберете категорию фундаментальной математической дисциплины, из которой Вы бы больше хотели зачесть спецкурс:', reply_markup= markup_2)
    bot.register_next_step_handler(message, on_click_2) #, parse_mode='html'
    
def on_click_2(message):  
  if message.text == 'Алгебра':
    markup_3= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Логика')
    btn_2=types.KeyboardButton('Алгебраическая теория чисел')
    markup_3.row(btn_1,btn_2)
    btn_4=types.KeyboardButton('Алгебраическая геометрия')
    markup_3.row(btn_4)
    bot.send_message(message.chat.id, 'Какой ты сегодня Албеброид?', reply_markup= markup_3)
    bot.register_next_step_handler(message, on_click_1)
  elif message.text == 'Анализ':
    markup_4= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Классический анализ')
    btn_2=types.KeyboardButton('Дифференциальная геометрия')
    markup_4.row(btn_1,btn_2)
    btn_3=types.KeyboardButton('Физика')
    btn_4=types.KeyboardButton('Дифференциальные уравнения и динамические системы')
    markup_4.row(btn_3, btn_4)
    bot.send_message(message.chat.id, 'Ну анализ это бэ, конечно, но какой?', reply_markup= markup_4)
    bot.register_next_step_handler(message, on_click_1)
  elif message.text == 'Теория чисел':
    markup_5= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Аналитическая теория чисел')
    markup_5.row(btn_1)
    btn_4=types.KeyboardButton('Алгебраическая теория чисел')
    markup_5.row(btn_4)
    bot.send_message(message.chat.id, 'О, наш числовичок, заходи. каких чисел охота?', reply_markup= markup_5)
    bot.register_next_step_handler(message, on_click_1)
  elif message.text == 'Геометрия':
    markup_6= types.ReplyKeyboardMarkup()
    btn_1=types.KeyboardButton('Дифференциальная геометрия')
    btn_2=types.KeyboardButton('Алгебраическая геометрия')
    markup_6.row(btn_1,btn_2)
    btn_4=types.KeyboardButton('Топология')
    markup_6.row(btn_4)
    bot.send_message(message.chat.id, 'Геометров уважаем, а какая интересует геометрия?', reply_markup= markup_6)
    bot.register_next_step_handler(message, on_click_1) 
 
def on_click_1(message):
  if message.text == 'Компьютерные науки и АД':
    for el in searcher('CS and DS'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Матстат и теорвер':
    for el in searcher('Math.Stat and Probability'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Экономика':
    for el in searcher('Economics'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Логика':
    for el in searcher('Logic'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start') 
  elif message.text == 'Алгебраическая теория чисел':
    for el in searcher('Number Theory'):
      if el not in searcher('Calculus'):
        bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start') 
  elif message.text == 'Алгебраическая геометрия':
    for el in searcher('algem'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start') 
  elif message.text == 'Классический анализ':
    for el in searcher('Calculus'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start') 
  elif message.text == 'Дифференциальная геометрия':
    for el in searcher('Diff Gem'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Физика':
    for el in searcher('Physics'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Дифференциальные уравнения и динамические системы':
    for el in searcher('Dynamics and Diff.Equations'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Аналитическая теория чисел':
    for el in searcher('Number Theory'):
      if el in searcher('Calculus'):
        bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start')
  elif message.text == 'Топология':
    for el in searcher('Topology'):
      bot.send_message(message.chat.id, el)
    bot.send_message(message.chat.id, '/start') 
  
    
    

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