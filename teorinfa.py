# -*- coding: utf-8 -*-
import telebot
import math
from telebot import types

token = '1415377315:AAHqxWDrahpafVcG3BEwAzkwdxiw7gS1Pxc'

bot = telebot.TeleBot(token)

# переменные

razmer = 0
kolvo = 0
kodir = 0
m = 0
kanals = 0
dlina = 0
f = 0
v = 0
zaderzhka = 0


# коэффициенты
gb = 1
sek = 1
gerz = 1
speed = 1

number = 0

# клавиатура для выбора того, что кодируется
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item1 = types.KeyboardButton("Звук")
item2 = types.KeyboardButton("Графика")
item3 = types.KeyboardButton("Текст")
item4 = types.KeyboardButton("Передача данных")
markup.add(item1, item2, item3, item4)

# клавиатура для текстов
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item11 = types.KeyboardButton("Количество символов")
item12 = types.KeyboardButton("Размер файла")
item13 = types.KeyboardButton("Кодировку")
markup1.add(item11, item12, item13)

# клавиатура для аудио
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item21 = types.KeyboardButton("Размер файла")
item22 = types.KeyboardButton("Количество каналов")
item23 = types.KeyboardButton("Длину записи")
item24 = types.KeyboardButton("Частоту дискретизации")
item25 = types.KeyboardButton("Глубину кодирования")
markup2.add(item21, item22, item23, item24, item25)

# клавиатура для графики
markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item32 = types.KeyboardButton("Размер файла")
item33 = types.KeyboardButton("Глубину цвета")
item35 = types.KeyboardButton("Разрешение")
markup3.add(item32, item33, item35)

# клавиатура для передачи
markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item41 = types.KeyboardButton("Пропускную способность")
item42 = types.KeyboardButton("Размер файла")
item43 = types.KeyboardButton("Время передачи")
item44 = types.KeyboardButton("Время задержки")
markup4.add(item41, item42, item43, item44)

# клавиатуры для единиц измерения

markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item51 = types.KeyboardButton("Биты")
item52 = types.KeyboardButton("Кб")
item53 = types.KeyboardButton("Байты")
markup5.add(item51, item52, item53)

markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item61 = types.KeyboardButton("мин")
item62 = types.KeyboardButton("сек")
markup6.add(item61, item62)

markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item71 = types.KeyboardButton("Гц")
item72 = types.KeyboardButton("КГц")
markup7.add(item71, item72)

markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item81 = types.KeyboardButton("бит")
item82 = types.KeyboardButton("байт")
markup8.add(item81, item82)

markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item91 = types.KeyboardButton("бит/с")
item92 = types.KeyboardButton("Кбит/с")
markup9.add(item91, item92)

markup0 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
item01 = types.KeyboardButton("Да")
markup0.add(item01)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>\nВыберите, что нужно кодировать.".format(message.from_user,
                                                                                                    bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def ans(message):
    textus = message.text
    if textus == 'Звук':
        msg = bot.send_message(message.chat.id, "Выберите искомое", parse_mode='html', reply_markup=markup2)
        bot.register_next_step_handler(msg, zvuk)
    if textus == 'Текст':
        msg = bot.send_message(message.chat.id, "Выберите искомое", parse_mode='html', reply_markup=markup1)
        bot.register_next_step_handler(msg, tekst)
    if textus == 'Графика':
        msg = bot.send_message(message.chat.id, "Выберите искомое", parse_mode='html', reply_markup=markup3)
        bot.register_next_step_handler(msg, grafika)
    if textus == 'Передача данных':
        msg = bot.send_message(message.chat.id, "Выберите искомое", parse_mode='html', reply_markup=markup4)
        bot.register_next_step_handler(msg, peredacha)

# общие функции

def razm(message):
    global gb
    textus = message.text
    if textus == "Кб":
        gb = 8192
    elif textus == "Биты":
        gb = 1
    elif textus == "Байты":
        gb = 8

    if number == 13:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите количество символов в файле"), n11)
    elif number == 21:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите количество каналов в записи"), n22)
    elif number == 32:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите глубину цвета в битах (единицы измерения прописывать не надо)"), n33)
    elif number == 42:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите пропускную способность канала в бит/с(единицы измерения прописывать не надо)"), n41)
    elif number == 12:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите размер файла в битах (единицы измерения прописывать не надо)"), n13)
    elif number == 25:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)"), n21)
    elif number == 33:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)"), n32)


def vremya(message):
    global sek
    textus = message.text
    if textus == "мин":
        sek = 60
    elif textus == "сек":
        sek = 1

    if number == 23:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)"), n21)
    elif number == 43:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)"), n42)
    elif number == 44:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Введите полное время передачи файла в секундах(единицы измерения прописывать не надо)"), n43)


def gerzy(message):
    global gerz
    textus = message.text
    if textus == "КГц":
        gerz = 1000
    elif textus == "Гц":
        gerz = 1
    msg = bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)")
    bot.register_next_step_handler(msg, n21)


def skorost(message):
    global speed
    textus = message.text
    if textus == "бит/с":
        speed = 1
    elif textus == "Кбит/с":
        speed = 1000
    msg = bot.send_message(message.chat.id, "Введите размер файла в битах(единицы измерения прописывать не надо)")
    bot.register_next_step_handler(msg, n42)


# функции для звука


def zvuk(message):
    global number
    textus = message.text
    if textus == 'Размер файла':
        number = 21
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup5)
        bot.register_next_step_handler(msg, gb)
    if textus == 'Количество каналов':
        number = 22
        msg = bot.send_message(message.chat.id, 'Введите размер файла в битах(единицы измерения прописывать не надо)')
        bot.register_next_step_handler(msg, n21)
    if textus == 'Длину записи':
        number = 23
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup6)
        bot.register_next_step_handler(msg, vremya)
    if textus == 'Частоту дискретизации':
        number = 24
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup7)
        bot.register_next_step_handler(msg, gerzy)
    if textus == 'Глубину кодирования':
        number = 25
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup8)
        bot.register_next_step_handler(msg, razm)


# все функции для текста


def tekst(message):
    global number
    textus = message.text
    if textus == 'Количество символов':
        number = 11
        msg = bot.send_message(message.chat.id, 'Введите размер файла в битах(единицы измерения прописывать не надо)')
        bot.register_next_step_handler(msg, n13)
    if textus == 'Размер файла':
        number = 13
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup5)
        bot.register_next_step_handler(msg, gb)
    if textus == 'Кодировку':
        number = 12
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup8)
        bot.register_next_step_handler(msg, razm)


# все функции для передачи
def peredacha(message):
    global number
    textus = message.text
    if textus == 'Пропускную способность':
        number = 41
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup9)
        bot.register_next_step_handler(msg, skorost)
    if textus == 'Размер файла':
        number = 42
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup5)
        bot.register_next_step_handler(msg, gb)
    if textus == 'Время передачи':
        number = 43
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup6)
        bot.register_next_step_handler(msg, vremya)
    if textus == 'Время задержки':
        number = 44
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup6)
        bot.register_next_step_handler(msg, vremya)


# все функции для графики


def grafika(message):
    global number
    textus = message.text
    if textus == 'Размер файла':
        number = 32
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup5)
        bot.register_next_step_handler(msg, razm)
    if textus == 'Глубину цвета':
        number = 33
        msg = bot.send_message(message.chat.id, 'Выберите единицы измерения искомых данных', reply_markup=markup8)
        bot.register_next_step_handler(msg, razm)
    if textus == 'Разрешение':
        number = 35
        msg = bot.send_message(message.chat.id, 'Введите размер файла в битах(единицы измерения прописывать не надо)')
        bot.register_next_step_handler(msg, n32)


def n11(message):
    global kolvo
    textus = message.text
    kolvo = float(textus)
    if number == 12:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 13:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)



def n12(message):
    global kodir
    textus = message.text
    kodir = float(textus)
    if number == 13:
        msg = bot.send_message(message.chat.id, 'Введите количество символов в файле')
        bot.register_next_step_handler(msg, n11)
    elif number == 11:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n13(message):
    global razmer
    textus = message.text
    razmer = float(textus)
    if number == 12:
        msg = bot.send_message(message.chat.id, 'Введите количество символов в файле')
        bot.register_next_step_handler(msg, n11)
    elif number == 11:
        msg = bot.send_message(message.chat.id, 'Введите кодировку в битах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n12)


def n21(message):
    global razmer
    textus = message.text
    razmer = float(textus)
    if number == 22:
        msg = bot.send_message(message.chat.id, 'Введите длину записи в секундах (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n23)
    elif number == 23:
        msg = bot.send_message(message.chat.id, 'Введите количество каналов в записи')
        bot.register_next_step_handler(msg, n22)
    elif number == 24:
        msg = bot.send_message(message.chat.id, 'Введите количество каналов в записи')
        bot.register_next_step_handler(msg, n22)
    elif number == 25:
        msg = bot.send_message(message.chat.id, 'Введите количество каналов в записи')
        bot.register_next_step_handler(msg, n22)


def n22(message):
    global kanals
    textus = message.text
    kanals = float(textus)
    if number == 21:
        msg = bot.send_message(message.chat.id, 'Введите длину записи в секундах (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n23)
    elif number == 23:
        msg = bot.send_message(message.chat.id, 'Введите частоту дискретизации в Гц (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n24)
    elif number == 24:
        msg = bot.send_message(message.chat.id, 'Введите длину записи в секундах (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n23)
    elif number == 25:
        msg = bot.send_message(message.chat.id, 'Введите длину записи в секундах (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n23)



def n23(message):
    global dlina
    textus = message.text
    dlina = float(textus)
    if number == 21:
        msg = bot.send_message(message.chat.id, 'Введите частоту дискретизации в Гц (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n24)
    elif number == 22:
        msg = bot.send_message(message.chat.id, 'Введите частоту дискретизации в Гц (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n24)
    elif number == 24:
        msg = bot.send_message(message.chat.id, 'Введите глубину кодирования в битах (единицы измерения указывать не нужно ')
        bot.register_next_step_handler(msg, n25)
    elif number == 25:
        msg = bot.send_message(message.chat.id, 'Введите частоту дискретизации в Гц (единицы измерения указывать не нужно)')
        bot.register_next_step_handler(msg, n24)


def n24(message):
    global f
    textus = message.text
    f = float(textus)
    if number == 21:
        msg = bot.send_message(message.chat.id, 'Введите глубину кодирования в битах (единицы измерения указывать не нужно ')
        bot.register_next_step_handler(msg, n25)
    elif number == 22:
        msg = bot.send_message(message.chat.id, 'Введите глубину кодирования в битах (единицы измерения указывать не нужно ')
        bot.register_next_step_handler(msg, n25)
    elif number == 23:
        msg = bot.send_message(message.chat.id, 'Введите глубину кодирования в битах (единицы измерения указывать не нужно ')
        bot.register_next_step_handler(msg, n25)
    elif number == 25:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n25(message):
    global kodir
    textus = message.text
    kodir = float(textus)
    if number == 21:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 22:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 23:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 24:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n35(message):
    global m
    textus = message.text
    m = float(textus)
    if number == 32:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 33:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n32(message):
    global razmer
    textus = message.text
    razmer = float(textus)
    if number == 33:
        msg = bot.send_message(message.chat.id, 'Введите  разрешение в dpi (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n35)
    elif number == 35:
        msg = bot.send_message(message.chat.id, 'Введите глубину цвета в битах (единицы измерения указывать не надо')
        bot.register_next_step_handler(msg, n33)


def n33(message):
    global kodir
    textus = message.text
    kodir = float(textus)
    if number == 32:
        msg = bot.send_message(message.chat.id, 'Введите  разрешение в dpi (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n35)
    elif number == 35:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n41(message):
    global v
    textus = message.text
    v = float(textus)
    if number == 42:
        msg = bot.send_message(message.chat.id, 'Введите время передачи в секундах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n43)
    elif number == 43:
        msg = bot.send_message(message.chat.id, 'Введите время задержки в секундах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n44)
    elif number == 44:
        msg = bot.send_message(message.chat.id, 'Введите размер файла в битах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n42)


def n42(message):
    global razmer
    textus = message.text
    razmer = float(textus)
    if number == 41:
        msg = bot.send_message(message.chat.id, 'Введите время передачи в секундах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n43)
    elif number == 43:
        msg = bot.send_message(message.chat.id, 'Введите пропускную способность в бит/с (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n41)
    elif number == 44:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def n43(message):
    global dlina
    textus = message.text
    dlina = float(textus)
    if number == 41:
        msg = bot.send_message(message.chat.id, 'Введите время задержки в секундах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n44)
    elif number == 42:
        msg = bot.send_message(message.chat.id, 'Введите время задержки в секундах (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n44)
    elif number == 44:
        msg = bot.send_message(message.chat.id, 'Введите пропускную способность в бит/с (единицы измерения указывать не надо)')
        bot.register_next_step_handler(msg, n41)


def n44(message):
    global zaderzhka
    textus = message.text
    zaderzhka = float(textus)
    if number == 41:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 42:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)
    elif number == 43:
        msg = bot.send_message(message.chat.id, 'Готовы получить ответ?', reply_markup=markup0)
        bot.register_next_step_handler(msg, otvet)


def otvet(message):
    global razmer
    global kolvo
    global kodir
    global m
    global kanals
    global dlina
    global f
    global v
    global zaderzhka
    global gb
    global sek
    global gerz
    global speed
    global number
    if number == 11:
        finish = razmer/kodir
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 12:
        finish = razmer/(kolvo*gb)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 13:
        finish = kolvo*kodir/gb
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 21:
        finish = kanals*dlina*f*kodir/gb
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 22:
        finish = razmer/(kodir*f*dlina)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 23:
        finish =razmer/(kodir*kanals*f*sek)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 24:
        finish = razmer/(kodir*kanals*dlina)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 25:
        finish = razmer/(f*dlina*kanals*gb)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 32:
        finish = kodir*m*m/gb
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 33:
        finish = razmer/(m*m*gb)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 35:
        finish = math.sqrt(razmer/kodir)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 41:
        finish = razmer/(dlina-zaderzhka)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 42:
        finish = v*(dlina-zaderzhka)
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 43:
        finish = razmer/v + zaderzhka
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))
    elif number == 44:
        finish = dlina - razmer/v
        bot.send_message(message.chat.id, "Ваш ответ: " + str(finish))

    razmer = 0
    kolvo = 0
    kodir = 0
    m = 0
    kanals = 0
    dlina = 0
    f = 0
    v = 0
    zaderzhka = 0
    gb = 1
    sek = 0
    gerz = 0
    speed = 0
    number = 0

if __name__ == '__main__':
     bot.infinity_polling()
