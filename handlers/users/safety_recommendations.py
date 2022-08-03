from aiogram import types

from keybords.inline.inline_buttons import check_password_back
from loader import dp
from utils.texts import rec_text


@dp.message_handler(commands=["recommendations"])
async def recommendations(message: types.Message):
    await message.answer(rec_text,
                         reply_markup=check_password_back,
                         disable_web_page_preview=True)
