from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["custom"])
def bot_custom(message: Message):
    bot.reply_to(message, f"Выполнить команду custom")
