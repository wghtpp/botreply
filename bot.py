import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=["start"])
def welcome():
    sti = open("static.webp, "rb')
    bot.send_sticker(message.chat.id, sti)()

    bot.send_message(message.chat.id,
                     "Будь как дома,путник, я тя сразу пошлю,  {0.first_name}!\nЯ - <b> {1.first_name}</b>, а ведь я всего пешка в чьих-то руках...".format(
                         message.from_user,
                         bot.get_me()), parse_mode="html")


@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
