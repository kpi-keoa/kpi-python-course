import telebot
from datetime import datetime
bot = telebot.TeleBot('')

temp_d = 0;
ham_d =  0;
temp_v = 0;
ham_v = 0;

  
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "/start": # Стратововое окно
      bot.send_message(message.from_user.id, "⚙️Привет\n Я бот для создания твоего умного дома. Давай начнём работу.\n" \
      "🔄Открой панель управления.\n\n /led - подсветка в комнате\n\n /temperature - термометр")
  elif message.text == "/temperature": # Управление кондиционером та параметрами температур и влажности
      current_datetime = datetime.now()
      bot.send_message(message.from_user.id, \
      "🕰Cегодня: %s \n\nДом🏠\n\n🌡Температура: %s° \n 💧Влажность: %s%% \n\nУлица⛰\n\n🌡Температура: %s° \n 💧Влажность: %s%% \n\n" \
      "🔭Общий прогноз: Комфортно" % (current_datetime, temp_d, ham_d, temp_v, ham_v))
      keyboard_tr = telebot.types.ReplyKeyboardMarkup(True)
      keyboard_tr.row('Холод❄️', 'Комфорт☀️', 'Жара🔥')
      bot.send_message(message.chat.id, "--Режимы--", reply_markup=keyboard_tr)
  elif message.text == "/led":  # Управление подсветкой в комнате
      keyboard = telebot.types.ReplyKeyboardMarkup(True)
      keyboard.row('Красный🔴', 'Синий🔵', 'x', 'Выкл\Вкл')
      keyboard.row('Оранжевий🟠', 'Фиолетовый 🟣', 'x', 'Яр. Бл. ⏫')
      keyboard.row('Желтый🟡', 'Голубой💧', 'x', 'Яр. Мн.⏬')
      keyboard.row('Зеленый🟢', 'Берюзовый', 'x', 'Белый⚪️')
      bot.send_message(message.chat.id, '---Пульт---', reply_markup=keyboard)
      """
      markup = telebot.types.InlineKeyboardMarkup()
      markup.row(telebot.types.InlineKeyboardButton(text='Выкл\Вкл❌', callback_data=1))
      markup.row(telebot.types.InlineKeyboardButton(text='Яр. Бл. ⏫', callback_data=2))   # больше яркости
      markup.row(telebot.types.InlineKeyboardButton(text='Яр. Мн.⏬', callback_data=3))    # меньше яркости
      markup.row(telebot.types.InlineKeyboardButton(text='Красный🔴', callback_data=4))    # красный
      markup.row(telebot.types.InlineKeyboardButton(text='Оранжевий🟠', callback_data=5))   # оранжевый 
      markup.row(telebot.types.InlineKeyboardButton(text='Желтый🟡', callback_data=6))      # желтый
      markup.row(telebot.types.InlineKeyboardButton(text='Зеленый🟢', callback_data=7))     # зеленый
      markup.row(telebot.types.InlineKeyboardButton(text='Фиолетовый 🟣', callback_data=8)) # синий
      markup.row(telebot.types.InlineKeyboardButton(text='Синий🔵', callback_data=9))      # фиолетовый
      markup.row(telebot.types.InlineKeyboardButton(text='Голубой💧', callback_data=10))   # голубой
      markup.row(telebot.types.InlineKeyboardButton(text='Белый⚪️', callback_data=11))     # белый
      markup.row(telebot.types.InlineKeyboardButton(text='Мод 1', callback_data=12))       # мод 1 
      markup.row(telebot.types.InlineKeyboardButton(text='Мод 2', callback_data=13))       # мод 2
      markup.row(telebot.types.InlineKeyboardButton(text='Дискотека', callback_data=14))   # епилептик
      markup.row(telebot.types.InlineKeyboardButton(text='Переливы', callback_data=15))    # графиент
      bot.send_message(message.chat.id, text="⬛️⬛️⬛️Пульт подсветки⬛️⬛️⬛️", reply_markup=markup) 
      """
  elif message.text == "Выкл\Вкл":
      print('Вкл')

  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Нажми ➡️ /start")

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text="Отправлено")
    answer = ''
    if call.data == '1':
        answer = '1'
        print("~ Подсветка выкл\вкл\n")
    elif call.data == '2':
        answer = '2'
        print("~ Больше Яркости\n")
    elif call.data == '3':
        answer = '3'
        print("~ Меньше Яркости\n")
    elif call.data == '4':
        answer = '4'
        print("~ включен Красный\n")
    elif call.data == '5':
        answer = '5'
        print("~ включен Оранжевый\n")
    elif call.data == '6':
        answer = '6'
        print("~ включен Желтый\n")
    elif call.data == '7':
        answer = '7'
        print("~ включен Зеленый\n")
    elif call.data == '8':
        answer = '8'
        print("~ включен Фиолетовый\n")
    elif call.data == '9':
        answer = '9'
        print("~ включен Синий\n")
    elif call.data == '10':
        answer = '10'
        print("~ включен Голубой\n")
    elif call.data == '11':
        answer = '11'
        print("~ включен Белый\n")
    elif call.data == '12':
        answer = '12'
        print("~ включен Мод 1\n")
    elif call.data == '13':
        answer = '13'
        print("~ включен Мод 2\n")
    elif call.data == '14':
        answer = '14'
        print("~ включен Дискотека\n")
    elif call.data == '15':
        answer = '15'
        print("~ включен Переливы\n")
       
bot.polling()