from aiogram import types
from aiogram.dispatcher.filters import Text
from keybords.inline.donate import donate_count, get_hundred, get_next_or_last_hundred, get_last_donate
from loader import dp


@dp.callback_query_handler(Text(startswith="thousand"))
async def get_donate(call: types.CallbackQuery):
    thousand = call.data.split(":")[1]
    markup = await get_hundred(thousand)
    await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(Text(startswith="next_hundred"))
@dp.callback_query_handler(Text(startswith="back_hundred"))
async def get_back_hundred(call: types.CallbackQuery):
    hundred = call.data.split(":")[1]
    if int(hundred) < 0:
        await call.message.edit_reply_markup(reply_markup=donate_count("1000-2000"))
    else:
        markup = get_next_or_last_hundred(int(hundred))
        await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(Text(startswith="hundred"))
async def get_last_donate_handler(call: types.CallbackQuery):
    hundred = call.data.split(":")[1]
    markup = get_last_donate(int(hundred))
    await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(Text(startswith="next_quarter"))
@dp.callback_query_handler(Text(startswith="back_quarter"))
async def get_last_donate_handler(call: types.CallbackQuery):
    hundred = call.data.split(":")[1]
    if int(hundred) < 0:
        await call.message.edit_reply_markup(reply_markup=donate_count("1000-2000"))
    else:
        markup = get_last_donate(int(hundred))
        await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(text="get_thousand")
async def get_donate(call: types.CallbackQuery):
    await call.message.edit_text("Сколько ты хочешь перевести?", reply_markup=donate_count("1000-2000"))


@dp.callback_query_handler(text="get_hundreds")
async def get_donate(call: types.CallbackQuery):
    markup = get_next_or_last_hundred(0)
    await call.message.edit_reply_markup(reply_markup=markup)


@dp.callback_query_handler(Text(startswith="next_thousand"))
@dp.callback_query_handler(Text(startswith="back_thousand"))
async def get_thousand(call: types.CallbackQuery):
    thousand = call.data.split(":")
    if thousand[1] == "0-1000":
        pass
    else:
        markup = donate_count(thousand[1])
        await call.message.edit_reply_markup(reply_markup=markup)
