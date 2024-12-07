import telebot
from telebot import types



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

