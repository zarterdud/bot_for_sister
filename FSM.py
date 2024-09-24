from aiogram.dispatcher.filters.state import StatesGroup, State


class TakeQuestion(StatesGroup):
    question = State()
    photo = State()
    document = State()


class SendUrl(StatesGroup):
    url = State()
