from aiogram import types

from loader import dp
from utils.texts import help_text


@dp.message_handler(commands="help")
async def bot_relink(message: types.Message):
    await message.answer(help_text)


@dp.callback_query_handler(text="help")
async def cancel(call: types.CallbackQuery):
    await call.message.edit_text(help_text)
