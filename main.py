from aiogram import Bot, Dispatcher, executor
from handlers.handler import DataBase
from handlers.callback_handler import callback_handler
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from big_text import caption_for_command_start
from inline_markups import start_keyboard
from config import start_gif_file_id, chat_id_operator
from FSM import SendUrl, TakeQuestion
from aiogram.dispatcher import FSMContext


class MyBot:
    def __init__(self, bot: Bot, dp: Dispatcher, db: DataBase):
        self.bot = bot
        self.dp = dp
        self.db = db

    # async def take_mess(self, message: Message):
    #     await message.answer(text=message)

    async def start(self, message: Message):
        await message.answer_animation(
            animation=start_gif_file_id,
            caption=caption_for_command_start,
            reply_markup=start_keyboard(),
            parse_mode="HTML",
        )

    async def question(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            question_text = message.text
            data["add_question"] = question_text
        await message.answer(
            text="Прикрепите фотографию, при отсутствии напишите «нет»"
        )
        await TakeQuestion.next()

    async def photo(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            try:
                photo_id = message.photo[-1].file_id
            except BaseException:
                photo_id = "нет"
            data["add_photo_id"] = photo_id
        await message.answer(text="Прикрепите документ, при отсутствии напишите «нет»")
        await TakeQuestion.next()

    async def document(self, message: Message, state: FSMContext):
        async with state.proxy() as data:
            try:
                document_id = message.document.file_id
            except BaseException:
                document_id = "нет"
            data["add_document_id"] = document_id
            await self.bot.send_message(
                chat_id=chat_id_operator,
                text=f"Вопрос от @{message.from_user.username}:",
            )
            for name, id_question in data.items():
                if name == "add_question":
                    await self.bot.send_message(
                        chat_id=chat_id_operator, text=id_question
                    )
                elif name == "add_photo_id":
                    if id_question != "нет":
                        await self.bot.send_photo(
                            chat_id=chat_id_operator, photo=id_question
                        )
                    else:
                        await self.bot.send_message(
                            chat_id=chat_id_operator, text="Фото не прикреплено"
                        )
                elif name == "add_document_id":
                    if id_question != "нет":
                        await self.bot.send_document(
                            chat_id=chat_id_operator, document=id_question
                        )
                    else:
                        await self.bot.send_message(
                            chat_id=chat_id_operator, text="Документ не прикреплен"
                        )
        await message.answer(text="Вопрос отправлен оператору!")
        await state.finish()
        await message.answer_document(
            document=start_gif_file_id,
            caption=caption_for_command_start,
            reply_markup=start_keyboard(),
            parse_mode="HTML",
        )

    async def send_url(self, message: Message, state: FSMContext):
        await self.bot.send_message(
            chat_id=chat_id_operator,
            text=f"Вопрос от @{message.from_user.username}:",
        )
        await self.bot.send_message(chat_id=chat_id_operator, text=message.text)
        await message.answer("Ссылка отправлена!")
        await state.finish()
        await message.answer_document(
            document=start_gif_file_id,
            caption=caption_for_command_start,
            reply_markup=start_keyboard(),
            parse_mode="HTML",
        )

    def register_handlers(self):
        # self.dp.register_message_handler(callback=self.take_mess, content_types=["any"])
        self.dp.register_message_handler(callback=self.start, commands=["start"])
        self.dp.register_message_handler(
            callback=self.question, content_types=["any"], state=TakeQuestion.question
        )
        self.dp.register_message_handler(
            callback=self.photo, content_types=["any"], state=TakeQuestion.photo
        )
        self.dp.register_message_handler(
            callback=self.document, content_types=["any"], state=TakeQuestion.document
        )
        self.dp.register_message_handler(
            callback=self.send_url, content_types=["any"], state=SendUrl.url
        )
        self.dp.register_callback_query_handler(callback=callback_handler, state="*")

    def run(self):
        self.register_handlers()
        executor.start_polling(dispatcher=self.dp, skip_updates=True)
