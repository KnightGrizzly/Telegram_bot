from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram import Router,F

from keyboards import main
from comand import SHOW_MENU


router = Router()
DATABASE = "data.json"

@router.message(CommandStart())
async def cmd_start_handler(message: Message) -> None:
    await message.answer(
        f"Вітаю, раді бачити вас у нашому кафе, {message.from_user.full_name}.", reply_markup=main)
