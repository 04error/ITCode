import string
import telebot
import config

bot = telebot.TeleBot(config.token)


def caesar(text: str, shift: int):
    LETTERS = string.ascii_letters + "абвгдеёжзийклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ012356789"
    new_text = ""
    for i in text:
        if LETTERS.find(i) + shift + 1 > len(LETTERS):
            new_text += LETTERS[shift - len(LETTERS[LETTERS.find(i):])]
        elif LETTERS.find(i) + shift + 1 < -len(LETTERS):
            new_text += LETTERS[shift - len(LETTERS[:LETTERS.find(i)])]
        else:
            new_text += LETTERS[LETTERS.find(i) + shift]
    return new_text


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\n"
                                      f"Пришли сообщение, а я его зашифрую шифром Цезаря!")


@bot.message_handler()
def encode_message_handler(message, text=None):
    msg = bot.send_message(message.chat.id, "Укажи сдвиг:")
    if text is None:
        text = message.text
    bot.register_next_step_handler(msg, encode_message, text)


def encode_message(message, text: str):
    try:
        shift = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Пришли целое число!")
        encode_message_handler(message, text)
        return
    bot.send_message(message.chat.id, f"Зашифрованное сообщение: {caesar(text, shift)}")


bot.infinity_polling()
