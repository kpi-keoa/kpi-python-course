## laboratory work №1 Pyton, student Bodak Yegor
#
# Даная програма получает входные даные из датчика температуры\ влажности\ 
# Цель прогрмы, вывод значений в сообщении телеграм бота.
# Предусмотрено что датчик не может выйти за рамки своих измерений.  
#!/bin/sh

import random
import telebot
from datetime import datetime
# token
bot = telebot.TeleBot('')

# Тест скорости циклов // результат в терминале

def time_test():
    ## начинаем мерять скорость
    start_t = datetime.now()
    ## тело
    for i in range(100000000):
        temp_d = 0 
    ## стоп
    stop_t  = datetime.now()
    print("\nfor time   = ",stop_t - start_t)
    ## запоминаем
    test = stop_t - start_t
    ## обновляем
    start_t = datetime.now()
    i = 0
    ## тело
    while i < 100000000:
        temp_d = 0
        i+= 1
    ## стоп
    stop_t  = datetime.now()
    print("\nwhile time = ",stop_t - start_t)
    ## проверка
    if test > (stop_t - start_t):
        print("\n\nПОБЕДИТЕЛЬ: while")
    else:
        print("\n\nПОБЕДИТЕЛЬ: for")


# тест скорости
time_test()
       
print("\n    БОТ ЗАПУЩЕН И ГОТОВ К РАБОТЕ")  
# Обработчик команд
def input_comand(message): 
  temp_d = random.randint(0, 45) # Сюда приходят даные с датчиков
  ham_d =  random.randint(0, 45) # Для тестов сделал рандомайзер
  temp_v = random.randint(0, 45) # Размах больше, это нужно для
  ham_v =  random.randint(0, 45) # тестов на ошибку приборов

  # Стaратововое окно
  keyboard = telebot.types.ReplyKeyboardMarkup(True)
  if message.text == "/start": 
      bot.send_message(message.from_user.id, \
      "⚙️Привет\nЯ бот для создания твоего умного дома. \
      Давай начнём работу.\n🔄Панель управления.")
      # меню
      keyboard.row('🌡Температура')
      bot.send_message(message.chat.id,'Меню', reply_markup=keyboard)
  # Меню термоклимата в доме та снаружи 
  elif message.text == "🌡Температура":
      current_datetime = datetime.now()
      bot.send_message(message.from_user.id, \
      "🕰Cегодня: %s \n\nДом🏠\n\n🌡Температура: %s° \n 💧Влажность: %s%% \
      \n\nУлица⛰\n\n🌡Температура: %s° \n 💧Влажность: %s%% \n\n" \
       % (current_datetime, temp_d, ham_d, temp_v, ham_v))
      if temp_d | temp_v > 40:
          bot.send_message(message.from_user.id, "🧪ERROR: Температура слишком высокая, нужно проверить исправность датчика")
  elif message.text == "help":
      bot.send_message(message.from_user.id, "🔧Часто возникающие проблемы ещё в обработке \
      обратитесь к администратору => @yegor_yevgenyevich")
  # защита от дурака
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Нажми ➡️ /start")
  

@bot.message_handler(content_types=['text'])
# Обработчик сообщений
def get_text_messages(message):
  # Входные команды
  input_comand(message)
  
  
bot.polling()