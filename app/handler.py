from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from app import keyboards as kb
from app.database import get_data
from seting import DATABASE

router = Router()

@router.message(CommandStart())
async def cmd_start_handler(message: Message) -> None:
    await message.answer(
        f"Вітаю, раді бачити вас у нашому кафе, {message.from_user.full_name}.", reply_markup= kb.main)


@router.message(F.text== "меню")
async def menu(message: Message):
    await message.answer("Виберіть категорію меню", reply_markup= kb.menu)


@router.callback_query(F.data.startswith("menu_"))
async def drinks(callback: CallbackQuery):
    type_menu = callback.data.split("_")[1]

    data_menu = get_data(DATABASE)
    await callback.answer(f"Ви вибрали категорію {type_menu}")

    if type_menu == "drinks":
        drink = data_menu["menu"]["drinks"]
        await callback.message.answer(f"{drink}", reply_markup= kb.menu)

    elif type_menu == "delicacy":
        delicacy= data_menu["menu"]["delicacy"]
        await callback.message.answer(f"{delicacy}", reply_markup= kb.menu)

    elif type_menu == "hot":
        dishes = data_menu["menu"]["hot"]
        await callback.message.answer(f"{dishes}", reply_markup= kb.menu)

    elif type_menu == "desert":
        desert  = data_menu["menu"]["desert"]
        await callback.message.answer(f"{desert}", reply_markup= kb.menu)

    elif type_menu == "soup":
        soup = data_menu["menu"]["soups"]
        await callback.message.answer(f"{soup}", reply_markup= kb.menu)

    elif type_menu == "sandwiches":
        sandwiches = data_menu["menu"]["sandwiches"]
        await callback.message.answer(f"{sandwiches}", reply_markup= kb.menu)

    elif type_menu == "sets":
        sets= data_menu["menu"]["sets"]
        await callback.message.answer(f"{sets}", reply_markup= kb.menu)

    elif type_menu == "vegetarians":
        vegetarians= data_menu["menu"]["vegetarians"]
        await callback.message.answer(f"{vegetarians}", reply_markup= kb.menu)
