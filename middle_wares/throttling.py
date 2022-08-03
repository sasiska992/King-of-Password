import asyncio
from typing import Union

from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import current_handler, CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


class TrottlingMiddleWare(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix="antiflood"):
        self.limit = limit
        self.prefix = key_prefix

        super(TrottlingMiddleWare, self).__init__()

    # 1.20 трансляция, метод, который выполняется при попадании в него message или сол бек
    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        if not handler:
            return
        dp = Dispatcher.get_current()
        limit = getattr(handler, "throttling_rate_limit", self.limit)
        key = getattr(handler, "throttling_key", f"{self.prefix}_{handler.__name__}")
        try:
            await dp.throttle(key, rate=limit)
        except Throttled as thr:
            await self.target_throttled(target, thr, dp, key)
            raise CancelHandler()

    async def target_throttled(self, target: Union[types.Message, types.CallbackQuery], throttled: Throttled,
                               dispatcher: Dispatcher, key: str):

        if isinstance(target, types.CallbackQuery):
            message = target.message
        else:
            message = target
        delta = round(throttled.rate - throttled.delta)
        if throttled.exceeded_count == 5:
            await message.reply("Ненада спамить!")
            return

        elif throttled.exceeded_count > 5:
            await message.reply(f"Я говорю ненада! узбогойся а, тeбе осталось ждать всего {delta} секунд")
            return
        await asyncio.sleep(delta)

    async def on_process_message(self, message: types.Message, data: dict):
        await self.throttle(message)

    async def on_process_callback_message(self, query: types.CallbackQuery, data: dict):
        await self.throttle(query)
