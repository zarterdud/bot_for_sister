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
                    callback_data="General_position",
                )
            ],
            [InlineKeyboardButton("Назад", callback_data="to_start")],
        ]
    )
    return position_kb
