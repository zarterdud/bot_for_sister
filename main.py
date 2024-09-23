from aiogram import Bot, Dispatcher, executor
from handlers.handler import DataBase
from handlers.callback_handler import callback_handler
from aiogram.types import Message
from big_text import caption_for_command_start
from inline_markups import start_keyboard


class MyBot:
    def __init__(self, bot: Bot, dp: Dispatcher, db: DataBase):
        self.bot = bot
        self.dp = dp
        self.db = db

    # async def take_mess(self, message: Message):
    #     await message.answer(text=message)

    async def start(self, message: Message):
        chat_id = message.from_user.id
        file_id = (
            "BQACAgIAAxkBAAMmZvGQIIHoLJ-9RZgoX3x2XEdsecMAAo5aAALpjpFLtPeClrdKMrY2BA"
        )
        await message.answer_document(
            document=file_id,
            caption=caption_for_command_start,
            reply_markup=start_keyboard(),
            parse_mode="HTML",
        )

    def register_handlers(self):
        self.dp.register_message_handler(callback=self.start, commands=["start"])
        self.dp.register_callback_query_handler(callback=callback_handler, state="*")

    def run(self):
        self.register_handlers()
        executor.start_polling(dispatcher=self.dp, skip_updates=True)
