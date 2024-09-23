from aiogram import Bot
from handlers.handler import DataBase
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")

# TOKEN = TOKEN
db_name = "database.sqlite"


def get_bot_and_db():
    bot = Bot(TOKEN)
    db = DataBase(db_name)
    return bot, db
