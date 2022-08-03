from aiogram import types

from loader import dp, db


@dp.my_chat_member_handler()
async def asd(message: types.chat_member_updated.ChatMemberUpdated):
    if message.new_chat_member.status == "kicked":
        await db.status_deleted_true(telegram_id=message.from_user.id)

    elif message.new_chat_member.status == "member" and message.old_chat_member.status == "kicked":
        await db.status_deleted_false(telegram_id=message.from_user.id)

    elif message.new_chat_member.status == "administrator":
        print(f"Пользователь с ID:{message.from_user.id} дал боту админку")

    elif message.new_chat_member.status == "member" and message.old_chat_member.status == "administrator":
        print(f"Пользователь с ID:{message.from_user.id} отобрал у бота админку")

    elif message.new_chat_member.status == "left":
        print(f"Пользователь с ID:{message.from_user.id} удалил бота из группы")

    elif message.new_chat_member.status == "member" and message.old_chat_member.status == "left":
        print(f"Пользователь с ID:{message.from_user.id} добавил бота в группу")

    else:
        print(f"Пользователь с ID:{message.from_user.id} что-то сделал с ботом")