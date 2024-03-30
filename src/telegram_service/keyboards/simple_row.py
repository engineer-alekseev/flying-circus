from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

    # return keyboard

def make_row_keyboard(items: list[str], n = 0):
    if not n: n = len(items)
    builder = InlineKeyboardBuilder()
    builder.row(*list(map(lambda index:InlineKeyboardButton(text=index, callback_data = index),items)), width=n)
    return builder.as_markup()

def make_yn_keyboard():
    return make_row_keyboard(["Да","Нет"])
