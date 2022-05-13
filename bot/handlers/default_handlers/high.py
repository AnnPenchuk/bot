from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["high"])
def bot_high(message: Message):
    bot.reply_to(message, f"Выполнить команду high")
