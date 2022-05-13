from loader import bot
from states.contact_info import UserInfoState
from telebot.types import Message

@bot.message_handler(commands=["survey"])
def survey(message: Message)-> None:
    bot.set_state(message.from_user.id, UserInfoState.name,message.chat.id)
    bot.send_message(message.from_user.id, f'{message.from_user.username} Введи свое имя')

