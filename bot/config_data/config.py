import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("token")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Выполнить команду low"),
    ("high", "Выполнить команду high"),
    ("custom", "Выполнить команду custom"),
    ("history", "Выполнить команду history"),
    ("survey", "Опрос")
)
