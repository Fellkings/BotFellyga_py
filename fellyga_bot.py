import telebot
from telebot import types
import random

bot = telebot.TeleBot('5221488288:AAHR4_qqgKWrWkDgbagc03HJ34HkzFLBPks')

file_random = open('random_question.txt', 'r', encoding='UTF-8')
random_f = file_random.read().split('<')
file_random.close()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_one = types.KeyboardButton("/help")
    button_two = types.KeyboardButton("Связь с разработчиком")
    markup.add(button_one, button_two)
    mess = f"Привет, <b>{message.from_user.first_name}</b>, я FellygaBot, нажми на кнопки ниже"
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_list(message):
        keyboard = types.InlineKeyboardMarkup()
        with open('help_list.txt', encoding='utf-8') as f:
            str = f.read()
        bot.send_message(message.chat.id, str, reply_markup=keyboard)

@bot.message_handler(commands=['question'])
def question_list(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Вопросы по программированию:", reply_markup=keyboard)
    with open('questions_list.txt', encoding='utf-8') as f:
        l = f.read()
    bot.send_message(message.chat.id, l , reply_markup=keyboard)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    question_1 = types.KeyboardButton("1")
    question_2 = types.KeyboardButton("2")
    question_3 = types.KeyboardButton("3")
    question_4 = types.KeyboardButton("4")
    question_5 = types.KeyboardButton("5")
    question_6 = types.KeyboardButton("6")
    question_7 = types.KeyboardButton("7")
    question_8 = types.KeyboardButton("8")
    question_9 = types.KeyboardButton("9")
    question_10 = types.KeyboardButton("10")
    markup.add(question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10)
    bot.send_message(message.chat.id, "Выбери вопрос", reply_markup=markup)

@bot.message_handler(commands=['add_question'])
def add_question(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton( "Телеграмм разработчика", url="t.me/fellkings"))
    bot.send_message(message.chat.id,'Если есть вопросы, которые нужно добавить, пишите мне.', reply_markup=keyboard)

@bot.message_handler(commands=['exit'])
def exit_user(message):
    keyboard = types.InlineKeyboardMarkup()
    mess = f"До скорых встреч, <b>{message.from_user.first_name}</b>!"
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=keyboard)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEcM9iVCrTwH3RjmmHy4Sfu0Hb4GA1egACEoIAAp7OCwABpWYdJ23BzUkjBA")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text == "1":
        bot.send_message(message.from_user.id, "Вопрос 1 - В чем разница между кортежем и списком в python?\nОтвет:\nСписок - аналог массивов в других языках программирования. И он изменяем, в отличии от кортежа. Кортеж нельзя отсортировать, однако можно преобразовать в список и отсортировать уже его.", reply_markup=keyboard)

    if message.text == "2":
        bot.send_message(message.from_user.id, "Вопрос 2 - Пример декоратора\nОтвет:\ndef hello():\n    return \"hello world\"", reply_markup=keyboard)

    if message.text == "3":
        bot.send_message(message.from_user.id, "Вопрос 3 - Какие есть типы в Python?\nОтвет:\nВ Python есть изменяемые и неизменяемые встроенные типы. К изменяемым относятся: списки, множества, словари. Представителями неизменяемых типов являются: строки, кортежи, числа.", reply_markup=keyboard)

    if message.text == "4":
        bot.send_message(message.from_user.id, "Вопрос 4 - Какие есть операторы цикла?\nОтвет:\nfor и while", reply_markup=keyboard)

    if message.text == "5":
        bot.send_message(message.from_user.id, "Вопрос 5 - Как преобразовать число в строку?\nОтвет:\nНадо использовать встроенную функцию str(). Для восьмеричного или шестнадцатеричного представления числа можем использовать другие встроенные функции, такие как oct() или hex().", reply_markup=keyboard)

    if message.text == "6":
        bot.send_message(message.from_user.id, "Вопрос 6 - Как используется оператор // в Python?\nОтвет:\nИспользование оператора // между двумя числами дает частное при делении числителя на знаменатель. Он также называется оператором деления без остатка.", reply_markup=keyboard)

    if message.text == "7":
        bot.send_message(message.from_user.id, "Вопрос 7 - Как изменить тип данных списка?\nОтвет:\nЧтобы преобразовать список в кортеж, мы используем функцию tuple().\nЧтобы превратить его в множество — функцию set().\nДля преобразования в словарь — dict().\nДля превращения в строку — join().", reply_markup=keyboard)

    if message.text == "8":
        bot.send_message(message.from_user.id, "Вопрос 8 - Как можно обратить порядок элементов в списке?\nОтвет:\nДля этого есть метод reverse():\n \n>>> a.reverse()\n>>> a\n[4, 3, 2, 1]", reply_markup=keyboard)

    if message.text == "9":
        bot.send_message(message.from_user.id, "Вопрос 9 - Что такое модульное программирование?\nОтвет:\nМо́дульное программи́рование — это организация программы как совокупности небольших независимых блоков, называемых модулями, структура и поведение которых подчиняются определённым правилам.", reply_markup=keyboard)

    if message.text == "10":
        bot.send_message(message.from_user.id, "Вопрос 10 - В каких областях питон имеет преимущество?\nОтвет:\nЛучше всего питон использовать в следующих областях:\n- веб-приложения\n- графические интерфейсы пользователя для настольных ПКn- научные и арифметические приложения\n- разработка ПО\n- разработка программ обучения\n- приложения для бизнеса\n- сетевые приложения\n- игры, 3D-графика", reply_markup=keyboard)

    if message.text == "Связь с разработчиком":
        bot.send_message(message.from_user.id, "Используй команду /add_question для связи.", reply_markup=keyboard)

    if message.text == 'Рандомный вопрос':
        random_question = random.choice(random_f)
        bot.send_message(message.chat.id, random_question)

bot.polling(none_stop=True)

