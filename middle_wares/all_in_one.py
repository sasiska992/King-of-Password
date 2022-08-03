import logging

from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.handler import SkipHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

logging.basicConfig(level=logging.INFO)


class AllIn(BaseMiddleware):
    # 1
    async def on_pre_process_update(self, update: types.Update, data: dict):

        data["data_on_pre_process_update"] = "Эта информация дойдет до самого конца цепочки :)"
        if update.message:
            user = update.message.from_user.id
        else:
            return

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        pass

    # 3 здесь другая дата
    async def on_pre_process_message(self, update: types.Message, data: dict):

        data["data_on_pre_process_message"] = "Это пойдет в on_process_message и в filter"

    # 4 filter

    # 5
    async def on_process_message(self, update: types.Message, data: dict):

        data["data_on_process_message"] = "Это пойдет в Handler"

    # 6 хендлер

    # 7
    async def on_post_process_message(self, update: types.Message, data_from_handler: list, data: dict):
        pass

    # 8
    async def on_post_process_update(self, update: types.Update, data_from_handler: list, data: dict):
        pass

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await query.answer()
