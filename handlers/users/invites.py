from aiogram import types

from keybords.inline.inline_buttons import check_password_back
from loader import dp, db


@dp.message_handler(commands=["invitations"])
async def inviting_users(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    int_invited_users = user.get("invited_users")
    str_invited_users = str(user.get("invited_users"))
    if int_invited_users > 0:
        if str_invited_users[-1] == 1:
            await message.answer("Спасибо тебе, что позволяешь мне знакомиться с новыми людьми!\n"
                                 f"Ты познакомил меня с {str_invited_users} пользователем! "
                                 f"Продолжай в том же духе!\n"
                                 f"Для приглашения друзей используй команду /relink",
                                 reply_markup=check_password_back)
        else:
            await message.answer("Спасибо тебе, что позволяешь мне знакомиться с новыми людьми!\n"
                                 f"Ты познакомил меня с {str_invited_users} пользователями! "
                                 f"Продолжай в том же духе!\n"
                                 f"Для приглашения друзей используй команду /relink",
                                 reply_markup=check_password_back)
    else:
        await message.answer("К сожалению, ты ещё никому не рассказал обо мне, "
                             "а ведь я люблю знакомиться :(\n"
                             "Для приглашения друзей используй команду /relink\n"
                             "Я уверен, что у тебя всё получится!  ♥️ ",
                             reply_markup=check_password_back)
