from aiogram import Bot
from handlers.handler import DataBase
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")
chat_id_operator = int(os.getenv("chat_id_operator"))
db_name = "database.sqlite"
start_gif_file_id = (
    "CgACAgIAAxkBAAIBOWbyxaCmRgwgRoZ8ElmdNmW7YZonAAJOWAACSCKRS1GAWcST-ksUNgQ"
)
Polozhenie_Novoe_pdf_id = (
    "BQACAgIAAxkBAANmZvGwkEpjX6p0k0WjbXirsoStNS0AAhldAALpjpFLVN9xT09VDn02BA"
)
nominations_photo = "AgACAgIAAxkBAAN9ZvGz5J59jOqi2pHMv2L0AAFqcHOnAAJu4DEbYs6QSwEzjOyNu5BCAQADAgADeQADNgQ"
url_on_your_post_photo = (
    "AgACAgIAAxkBAAOIZvG1hH6tv1fFahhBJMuzQ80ro80AAhviMRvpjpFLd9nkczols8ABAAMCAAN5AAM2BA"
)


def get_bot_and_db():
    bot = Bot(TOKEN)
    db = DataBase(db_name)
    return bot, db
