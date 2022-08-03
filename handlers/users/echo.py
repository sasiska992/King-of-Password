import random
import time
import asyncio
from aiogram import types

from loader import dp
from utils.choose_sticker import get_sticker, knowing_stickers
from utils.texts import interesting_facts


@dp.message_handler()
async def echo_bot(message: types.Message):
    sticker = await get_sticker(dp, message)

    del_message = await message.answer(
        f"Если честно, я не знаю, что можно ответить на \"<code>{message.text}</code>\"...\n"
        f"Подожди пару секунд, я что-то придумаю")
    del_message_2 = await message.answer_sticker(sticker=random.choice(knowing_stickers))

    await asyncio.sleep(4)

    await del_message.delete()
    await del_message_2.delete()

    await message.answer("Ничего кроме того, чтобы скинуть тебе котика, я не придумал, поэтому наслаждайся им ღ\n\n"
                         "А вообще, ты можешь написать \"<code>/</code>\" и посмотреть, что я умею")
    await message.answer_sticker(sticker=sticker)
    await asyncio.sleep(2)
    del_message = await message.answer("Хотя...")
    await asyncio.sleep(1)
    await del_message.delete()
    del_message_2 = await message.answer("Дай 4 секунды, мне в процессор пришла отличная идея, что можно ответить")
    await asyncio.sleep(4)
    facts = random.choice(interesting_facts)
    await del_message_2.delete()
    await message.answer(facts)
