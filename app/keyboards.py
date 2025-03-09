from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import (InlineKeyboardButton, InlineKeyboardMarkup,
                                    ReplyKeyboardBuilder)

BUTTON_LIST_MENU = "Меню"

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="меню")]],
                           resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="drinks", callback_data="menu_drinks")],
    [InlineKeyboardButton(text="delicacy`s", callback_data="menu_delicacy")],
[InlineKeyboardButton(text="hot", callback_data="menu_hot_dishes")],
[InlineKeyboardButton(text="desert", callback_data="menu_desert")],
[InlineKeyboardButton(text="soups", callback_data="menu_soup")],
[InlineKeyboardButton(text="sandwiches", callback_data="menu_sandwiches")],
[InlineKeyboardButton(text="sets", callback_data="menu_sets_menu")],
[InlineKeyboardButton(text="vegetarians", callback_data="menu_vegetarians_menu")]

                                             ])

def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=BUTTON_LIST_MENU)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup