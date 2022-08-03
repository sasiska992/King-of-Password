from aiogram import types
from aiogram.utils.markdown import hcode

from loader import dp


@dp.message_handler(commands=["show_id"])
async def show_ID(message: types.Message):
    await message.answer(f"Ваш уникальный Telegram ID: {hcode(message.from_user.id)}\n"
                         f"Нажмите на него, чтобы скопировать!", parse_mode=types.ParseMode.HTML)
