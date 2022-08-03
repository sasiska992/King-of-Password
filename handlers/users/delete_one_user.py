from aiogram import types

from loader import dp, db


@dp.message_handler(commands="del_user")
async def get_lastname(message: types.Message):
    if message.from_user.id == 700186952:
        await db.delete_user(telegram_id=700186952)
        await message.answer("Пользователь удалён")
    else:
        await message.answer("У вас недостаточно прав")
