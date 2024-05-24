import telebot
import time
import pyautogui
from random import randint
from telebot import types




bot = telebot.TeleBot('7119778306:AAFT2Eas-wb-zgexhbQIr48UJcQyaAGXr3g')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):


    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет это телеграм-бот , он знает такие команды, как Привет, Как дела? Что делаешь? Пока, Алиса, Кто ты? Комар, Как прошел день? Ты поэт? :)")
        bot.send_photo(message.from_user.id, photo=open('Banner-1.0.jpg', 'rb'))

    elif message.text == "Гриша":
        bot.send_message(message.from_user.id, "да я Гриша твой бот напиши /start")


    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет :)")
        bot.send_photo(message.from_user.id, photo=open('kot.jpg', 'rb'))
    elif message.text == "Как дела?":
        bot.send_message(message.from_user.id, "хорошо)")
        bot.send_photo(message.from_user.id, photo=open('kot1.webp', 'rb'))
    elif message.text == "Что делаешь?":
        bot.send_message(message.from_user.id, "разговариваю с вами)")
    elif message.text == "Как день прошел?":
        bot.send_message(message.from_user.id, "Хорошо")
    elif message.text == "Ты поэт?":
        bot.send_message(message.from_user.id, "Конечно)))")
        bot.send_photo(message.from_user.id, photo=open('k.png', 'rb'))


    elif message.text == "Пока":
        bot.send_photo(message.from_user.id, photo=open('s.jpg', 'rb'))
    elif message.text == "Алиса":
        bot.send_message(message.from_user.id, "https://alice.yandex.ru/ - это чат с Алсой ")
    elif message.text == "Кто ты?":
        bot.send_message(message.from_user.id, "Я Гриша бот, моя задача вас веселить )))")
        bot.send_photo(message.from_user.id, photo=open('d.jpg', 'rb'))
    elif message.text == "Комар":
        bot.send_message(message.from_user.id, "https://www.youtube.com/watch?v=IHJIs56IJa8")
    elif message.text == 'Play':
        bot.register_next_step_handler(message, play_command)

        bot.send_message(message.from_user.id, "Начнем игру! Я загадал игру от 1 до 10.Угадай его! (пиши от 1 до 10)")



    else:
        bot.send_message(message.from_user.id, "Что-то пошло не так :(")


@bot.message_handler(func=lambda message: message.text == 'Play')

def play_command(message):

    a = randint(1, 10)


    if message.text.isdigit() and int(message.text) in range(1, 11):
        if int(message.text) == a:
            bot.send_message(message.from_user.id, f"Ура, вы угадали! Я загадал число {a}.")
        else:
            bot.send_message(message.from_user.id, f"К сожалению, вы не угадали. Я загадал число {a}. Попробуй еще! (Пиши Play)")
    else:
        bot.send_message(message.from_user.id, "Пожалуйста, введите число от 1 до 10.")


bot.polling(none_stop=True, interval=0)