from aiogram import Dispatcher


async def on_startup_admins(dp: Dispatcher):
    await dp.bot.send_message(chat_id=700186952, text="Бот запущен успешно!")


async def on_shutduwn_admins(dp: Dispatcher):
    await dp.bot.send_message(chat_id=700186952, text="Бот выключен")
