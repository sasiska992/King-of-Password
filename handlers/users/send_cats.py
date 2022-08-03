from aiogram import types

from keybords.inline.send_cat import send_cat
from loader import dp
from utils.choose_sticker import get_sticker


@dp.callback_query_handler(text="cats")
async def cats(call: types.callback_query):
    sticker = await get_sticker(dp, call.message)
    await call.message.answer_sticker(sticker=sticker)
    await call.message.answer("Лови котика!",
                              reply_markup=send_cat)


@dp.message_handler(commands="cat")
async def cats(message: types.Message):
    sticker = await get_sticker(dp, message)
    await message.answer_sticker(sticker=sticker)
    await message.answer("Лови котика!",
                         reply_markup=send_cat)
