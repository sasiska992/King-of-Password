from aiogram import types

from keybords.inline.dice import dice
from loader import dp
import asyncio
import random

from utils.choose_sticker import happy_stickers


@dp.callback_query_handler(text="try_luck")
async def try_luck(call: types.CallbackQuery):
    emoji = ["🎲", "🎯", "⚽", "🎰", "🏀", "🎳"]
    message = call.message
    message = await message.answer_dice(emoji=random.choice(emoji))
    value = message.dice.value
    happy_emoji = random.choice(happy_stickers)
    emoji = message.dice.emoji
    if (emoji == "🏀") and value < 4:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)

    elif emoji == "⚽" and value > 2:
        await asyncio.sleep(3.5)
        await message.answer_sticker(sticker=happy_emoji)
        await message.answer("УРА, ТЫ ЗАБИЛ!!!\n"
                             "Вот твой билетик в казино 🎟\n"
                             "Только ключи от квартиры не забудь оставить дома...🤭",
                             reply_markup=dice)

    elif emoji == "⚽" and value < 3:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)

    elif emoji == "🎰" and value < 64 and value != 1 and value != 43 and value != 22:
        await asyncio.sleep(2)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)

    elif (emoji == "🎲" or emoji == "🎳" or emoji == "🎯") and value < 6:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)

    else:
        await asyncio.sleep(3.5)
        await message.answer_sticker(sticker=happy_emoji)
        await message.answer("УРА, ТЫ ПОБЕДИЛ!!!\n"
                             "Вот твой билетик в казино 🎟\n"
                             "Только ключи от квартиры не забудь оставить дома...🤭",
                             reply_markup=dice)


@dp.message_handler(commands=["try_luck"])
async def try_luck(message: types.Message):
    emoji = ["🎲", "🎯", "⚽", "🎰", "🏀", "🎳"]
    happy_emoji = random.choice(happy_stickers)
    message = await message.answer_dice(emoji=random.choice(emoji))
    value = message.dice.value
    emoji = message.dice.emoji
    if (emoji == "🏀") and value < 4:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)
    elif emoji == "⚽" and value > 2:
        await asyncio.sleep(3.5)
        await message.answer_sticker(sticker=happy_emoji)
        await message.answer("УРА, ТЫ ЗАБИЛ!!!\n"
                             "Вот твой билетик в казино 🎟\n"
                             "Только ключи от квартиры не забудь оставить дома...🤭",
                             reply_markup=dice)
    elif emoji == "⚽" and value < 3:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)
    elif emoji == "🎰" and value < 64 and value != 1 and value != 43 and value != 22:
        await asyncio.sleep(2)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)
    elif (emoji == "🎲" or emoji == "🎳" or emoji == "🎯") and value < 6:
        await asyncio.sleep(3.5)
        await message.answer("Ну ничего, в другой раз точно получится!",
                             reply_markup=dice)
    else:
        await asyncio.sleep(3.5)
        await message.answer_sticker(sticker=happy_emoji)
        await message.answer("УРА, ТЫ ПОБЕДИЛ!!!\n"
                             "Вот твой билетик в казино 🎟\n"
                             "Только ключи от квартиры не забудь оставить дома...🤭",
                             reply_markup=dice)
