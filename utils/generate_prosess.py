import asyncio
import random

from keybords.inline.generating_buttons import generate1, generate2, generate3, generate4, generate5, generate6, \
    generate7, generate10, generate9, generate8


async def generating_process(call):
    random_times = [0.01, 1, 0.1, 0.5, 0.7, 0, 0.001, 0.1]
    message = await call.message.answer("⏳")
    await call.message.edit_text("Происходит создание пароля...  [○○○○○○○○○○] 0%", reply_markup=generate10)
    await call.message.edit_text("Происходит создание пароля...  [■○○○○○○○○○] 10%", reply_markup=generate1)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■○○○○○○○○] 20%", reply_markup=generate2)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■○○○○○○○] 30%", reply_markup=generate3)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■○○○○○○] 40%", reply_markup=generate4)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■■○○○○○] 50%", reply_markup=generate5)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■■■○○○○] 60%", reply_markup=generate6)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■■■■○○○] 70%", reply_markup=generate7)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■■■■■○○] 80%", reply_markup=generate8)
    await asyncio.sleep(random.choice(random_times))
    await call.message.edit_text("Происходит создание пароля...  [■■■■■■■■■○] 90%", reply_markup=generate9)
    await asyncio.sleep(random.choice(random_times))
    generating_message = await call.message.edit_text("Происходит создание пароля...  [■■■■■■■■■] 100%",
                                                      reply_markup=generate10)
    await message.delete()
    return generating_message
