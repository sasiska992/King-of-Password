from aiogram import types
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.models import User


class PostACL(BaseMiddleware):
    allowed_update = ["callback_query", "message"]

    async def trigger(self, action, arg: tuple):
        obj, *args, data = arg
        if not any(update in action for update in self.allowed_update):
            return
        if not action.startswith("process_"):
            return

        handler = current_handler.get()
        if not handler:
            return

        allow = getattr(handler, "allow", False)

        if allow:
            return

        user: User = data.get("user")

        if not user.allowed:
            message = obj.message if isinstance(obj, types.CallbackQuery) else obj
            await message.reply("Доступ запрещен, иди гуляй")
            raise CancelHandler()
