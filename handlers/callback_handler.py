from aiogram.types import CallbackQuery
from aiogram.dispatcher.dispatcher import FSMContext
from config import get_bot_and_db
from big_text import caption_for_position, caption_for_command_start
from inline_markups import position_keyboard, start_keyboard


async def callback_handler(call: CallbackQuery, state: FSMContext):
    bot, db = get_bot_and_db()
    callback = call.data
    chat_id = call.from_user.id

    if callback == "position":
        await call.message.delete()
        await bot.send_message(
            chat_id=chat_id,
            text=caption_for_position,
            reply_markup=position_keyboard(),
        )
