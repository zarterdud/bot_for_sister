from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.dispatcher.dispatcher import FSMContext
from FSM import TakeQuestion, SendUrl
from config import (
    get_bot_and_db,
    start_gif_file_id,
    Polozhenie_Novoe_pdf_id,
    nominations_photo,
    url_on_your_post_photo,
)
from big_text import (
    caption_for_position,
    caption_for_command_start,
    caption_for_dates_of_the_event,
    caption_for_nominations,
    caption_for_our_partners_in_social_media,
    caption_for_questions_to_operator,
)
from inline_markups import position_keyboard, start_keyboard, mailing_to_orgs_keyboard


async def callback_handler(call: CallbackQuery, state: FSMContext):
    bot, db = get_bot_and_db()
    callback = call.data
    chat_id = call.from_user.id

    if callback == "position":
        await call.message.delete()
        await bot.send_message(
            chat_id=chat_id, text=caption_for_position, reply_markup=position_keyboard()
        )

    elif callback == "mailing_to_orgs":
        try:
            state.finish()
        except BaseException:
            pass
        await call.message.delete()
        await bot.send_message(
            chat_id=chat_id,
            text="Вы можете задать вопрос оператору для получения обратной связи.",
            reply_markup=mailing_to_orgs_keyboard(),
        )

    elif callback == "chat_with_operator":
        button_back = InlineKeyboardMarkup()
        button_back.add(
            InlineKeyboardButton("Отказаться", callback_data="mailing_to_orgs")
        )
        await call.message.edit_text(
            text=caption_for_questions_to_operator,
            reply_markup=button_back,
            parse_mode="HTML",
        )
        await TakeQuestion.question.set()

    elif callback == "url_on_your_post":
        button_back = InlineKeyboardMarkup()
        button_back.add(InlineKeyboardButton("Отказаться", callback_data="to_start"))
        await call.message.delete()
        await bot.send_message(
            chat_id=chat_id, text="Отправьте ссылку", reply_markup=button_back
        )
        await SendUrl.url.set()

    elif callback == "our_partners_in_social_media":
        button_back = InlineKeyboardMarkup()
        button_back.add(InlineKeyboardButton("Назад", callback_data="to_start"))
        await call.message.delete()
        await bot.send_photo(
            chat_id=chat_id,
            photo=url_on_your_post_photo,
            caption=caption_for_our_partners_in_social_media,
            reply_markup=button_back,
            parse_mode="HTML",
        )

    elif callback == "general_position":
        buttons_back = InlineKeyboardMarkup()
        buttons_back.add(InlineKeyboardButton("Назад", callback_data="position")).add(
            InlineKeyboardButton("В начало", callback_data="to_start")
        )
        await call.message.delete()
        await bot.send_document(
            chat_id=chat_id,
            document=Polozhenie_Novoe_pdf_id,
            caption="Здесь вы найдете ответы на все вопросы",
            reply_markup=buttons_back,
        )

    elif callback == "nominations":
        buttons_back = InlineKeyboardMarkup()
        buttons_back.add(InlineKeyboardButton("Назад", callback_data="position")).add(
            InlineKeyboardButton("В начало", callback_data="to_start")
        )
        await call.message.delete()
        await bot.send_photo(
            chat_id=chat_id,
            photo=nominations_photo,
            caption=caption_for_nominations,
            reply_markup=buttons_back,
            parse_mode="HTML",
        )

    elif callback == "dates_of_the_event":
        buttons_back = InlineKeyboardMarkup()
        buttons_back.add(
            InlineKeyboardButton("Назад", callback_data="to_position")
        ).add(InlineKeyboardButton("В начало", callback_data="to_start"))
        await call.message.edit_text(
            text=caption_for_dates_of_the_event,
            parse_mode="HTML",
            reply_markup=buttons_back,
        )

    elif callback == "to_position":
        await call.message.edit_text(
            text=caption_for_position, reply_markup=position_keyboard()
        )

    elif callback == "to_start":
        try:
            state.finish()
        except BaseException:
            pass
        await call.message.delete()
        await bot.send_document(
            chat_id=chat_id,
            document=start_gif_file_id,
            caption=caption_for_command_start,
            reply_markup=start_keyboard(),
            parse_mode="HTML",
        )
