from aiogram.types import Update
from loader import dp
from aiogram.utils.exceptions import CantParseEntities, ChatNotFound


@dp.errors_handler()
async def error_handler(update: Update, exception):
    if isinstance(exception, ChatNotFound):
        # Так можно добраться до забаненного пользователя
        await update.get_current().message.answer("Эта ошибка обработалась в error")
    return True


@dp.errors_handler()
async def error_handler(update: Update, exception):
    if isinstance(exception, CantParseEntities):
        # Так можно добраться до забаненного пользователя
        await update.get_current().message.answer("Что-то не так с текстом")
    return True
