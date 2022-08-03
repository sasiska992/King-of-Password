from aiogram import types

from keybords.inline.inline_buttons import check_password_back
from loader import dp


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Слушай, у меня интернет плохой, стикер не грузится, "
        "отправь лучше текстовое сообщение или выбери команду из списка", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Слушай, у меня интернет плохой, видео вообще не грузится, "
        "отправь лучше текстовое сообщение или выбери команду из списка", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Слушай, у меня интернет плохой, фотка не может загрузится, "
        "отправь лучше текстовое сообщение или выбери команду из списка", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Слушай, у меня интернет плохой, голосовое никак не может загрузиться, "
        "отправь лучше текстовое сообщение или выбери команду из списка", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Мне показалось, или ты пытаешься меня спамить своими документами? -_-\n\n"
        "Лучше выбери команду из списка -_-", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def echo_any_bot(message: types.Message):
    await message.answer(
        "Пфф, думаешь я раньше не знал, где ты находишься?)"
        "\n\nЛучше выбери команду из списка!", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def echo_any_bot(message: types.Message):
    await message.answer(
        f"Опа, теперь у меня есть номер {message.contact.full_name}\n\n"
        f"А вообще выбери команду из списка, тогда и поговорим -_-", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.VIDEO_NOTE)
async def echo_any_bot(message: types.Message):
    await message.answer("Ничоси, вот мы с тобой и познакомились вживую\n\n"
                         "Для закрепления нашего знакомства выбери одну из команд", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.POLL)
async def echo_any_bot(message: types.Message):
    await message.answer("Я тебе по секрету скажу, я робот и голосовать не для меня\n"
                         "Это вам кожаным надо голосовать, а не мне  ╚(ಠ_ಠ)=┐", reply_markup=check_password_back)


@dp.message_handler(content_types=types.ContentTypes.DICE)
async def echo_any_bot(message: types.Message):
    await message.answer("Я смотрю ты в казино решил поиграть -_- \n"
                         "Лучше напиши /try_luck и поиграем вместе!", reply_markup=check_password_back)
