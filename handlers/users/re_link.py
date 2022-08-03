from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.deep_linking import get_start_link

from keybords.inline.inline_buttons import get_relink
from loader import dp


@dp.message_handler(commands="relink")
async def bot_relink(message: types.Message):
    deep_link = await get_start_link(payload=f"{message.from_user.id}")
    await message.answer(text="Ссылка для друга:")
    await message.answer(f"`{deep_link}`\nНажми, чтобы скопировать!",
                         parse_mode=ParseMode.MARKDOWN, reply_markup=get_relink(deep_link))
