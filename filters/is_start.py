from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsStart(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text == "/start"
