from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db


@dp.message_handler(commands=["stat"])
async def change_username(message: types.Message):
    invited_users = await db.count_invited_users()
    count_all_users = await db.count_all_users()
    count_deleted_users = await db.count_deleted_users()
    generated_passwords = list(await db.get_generated_passwords())
    all_passwords = 0
    for i in generated_passwords:
        passwords = int(''.join(map(str, i)))
        all_passwords += passwords
    await message.answer(
        f"За всё время было отправлено и получено {message.message_id} сообщений "
        f"и создано {all_passwords} паролей\n"
        f"Сейчас в боте зарегистрировано {count_all_users} человек из них:\n"
        f"{invited_users} приглашены\n{count_deleted_users} удалили бота"
    )
