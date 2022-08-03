import re

import asyncpg
from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, db
from utils.texts import start_text


@dp.message_handler(CommandStart(deep_link=re.compile(r"^[0-9]{8,11}$")))
async def ref_start(message: types.Message):
    try:
        await db.add_user(
            username=message.from_user.username,
            telegram_id=message.from_user.id,
        )
        await db.is_invited(telegram_id=message.from_user.id)
        args = message.get_args()
        first_user = dict(await db.select_user(telegram_id=int(args)))
        invited_users = first_user.get("invited_users")
        await db.update_invited_users(inveted_users=invited_users + 1, telegram_id=int(args))
        await message.answer(text="Приветствую вас!\n"
                                  f"Нас познакомил <code>{first_user.get('username')}</code>\n"
                                  f"Для продолжения работы с ботом напишите \"/help\"")

    except asyncpg.exceptions.UniqueViolationError:
        args = message.get_args()
        first_user = dict(await db.select_user(telegram_id=int(args)))
        second_user = dict(await db.select_user(telegram_id=message.from_user.id))
        if int(args) == int(message.from_user.id):
            await message.answer("Меня не обмануть, я вижу, что ты пытаешься пригласить самого себя\n\n"
                                 "Лучше выбери команду из списка, написав \"<code>/</code>\"")

        elif second_user.get("is_invited") == True:
            await message.answer("Я записал, что вы уже были приглашены, второй раз не получится\n\n"
                                 "Лучше выбери команду из списка, написав \"<code>/</code>\"")

        else:
            await message.answer(text=start_text)


@dp.message_handler(text="привет")
@dp.message_handler(text="Привет")
@dp.message_handler(CommandStart())
async def dif_start(message: types.Message):
    try:
        await db.add_user(
            username=message.from_user.username,
            telegram_id=message.from_user.id,
        )

    except asyncpg.exceptions.UniqueViolationError:
        pass
    await message.answer(text=start_text)
