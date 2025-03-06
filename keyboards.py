from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.filters.callback_data import CallbackData


BUTTON_LIST_MENU = "Меню"

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="меню")]],resize_keyboard=True)

menu = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Напої", callback_data="Drinks")],
                                             [InlineKeyboardButton(text="холодні закуски", callback_data="Delicacy")],
[InlineKeyboardButton(text="гарячі страви", callback_data="Hot dishes")],
[InlineKeyboardButton(text="десерти", callback_data="desert")],
[InlineKeyboardButton(text="супи", callback_data="Soup")],
[InlineKeyboardButton(text="бутерброди та сендвічі", callback_data="Sandwiches")],
[InlineKeyboardButton(text="сет-меню", callback_data="Set menu")],
[InlineKeyboardButton(text="вегетаріанське меню", callback_data="Vegetarian menu")],
[InlineKeyboardButton(text="для дітей", callback_data="For kids")],


                                             ])

def menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=BUTTON_LIST_MENU)

    markup = builder.as_markup()
    markup.resize_keyboard = True

    return markup