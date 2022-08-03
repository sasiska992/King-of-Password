import logging

from aiogram import types
from aiogram.dispatcher.handler import ctx_data

from aiogram.dispatcher.filters import BoundFilter


class someFilter(BoundFilter):
    async def check(self, message: types.Message):
        data = ctx_data.get()
        logging.info(f"4. Filter, {data=}")
        logging.info("Слудующая точка Process Message")
        my_dict = {"from_filter": "Какие-то данные из фильтра"}
        return my_dict
