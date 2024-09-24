from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard():
    start_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Положение", callback_data="position")],
            [
                InlineKeyboardButton(
                    "Задать вопрос организаторам", callback_data="mailing_to_orgs"
                )
            ],
            [
                InlineKeyboardButton(
                    "Наши партнеры в соцсетях",
                    callback_data="our_partners_in_social_media",
                )
            ],
            [
                InlineKeyboardButton(
                    "Ссылка на ваш пост", callback_data="url_on_your_post"
                )
            ],
        ]
    )
    return start_kb


def position_keyboard():
    position_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "Сроки проведения", callback_data="dates_of_the_event"
                )
            ],
            [InlineKeyboardButton("Номинации", callback_data="nominations")],
            [
                InlineKeyboardButton(
                    "Общее положение",
                    callback_data="general_position",
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="to_start")],
        ]
    )
    return position_kb


def mailing_to_orgs_keyboard():
    mailing_to_orgs_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    "Задать вопрос", callback_data="chat_with_operator"
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="to_start")],
        ]
    )
    return mailing_to_orgs_kb
