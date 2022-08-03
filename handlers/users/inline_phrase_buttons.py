from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from keybords.inline.callback_data import pass_callback
from keybords.inline.inline_buttons import check_password_back
from keybords.inline.save_pass import yes_or_not
from keybords.inline.send_password import send_phrase_password
from loader import dp, db
from states.deleted_messages import Del
from utils.funny_password import translating
from utils.generate_prosess import generating_process


@dp.callback_query_handler(pass_callback.filter(mode="phrase"))
async def generate_pass(call: types.CallbackQuery, state: FSMContext):
    try:
        generating_message = await generating_process(call)
        await generating_message.delete()
        password = translating()
        sent_message = f"Итак, вот твой пароль:\n`{password[0]}` - полная фраза\n" \
                       f"`{password[1]}` - Пароль, который тебе надо ввести на английской раскладке " \
                       f"русскими буквами\n" \
                       f"`{password[2]}` - Твой окончательный пароль\n" \
                       f"Для того, чтобы скопировать, просто нажми на него\n"
        await call.message.answer(sent_message,
                                  parse_mode=ParseMode.MARKDOWN,
                                  reply_markup=send_phrase_password(sent_message))

        user = await db.select_user(telegram_id=call.from_user.id)
        await db.update_generated_passwords(telegram_id=call.from_user.id,
                                            generated_password=user.get("generated_passwords") + 1)
        await call.message.answer("Хотите ли вы сохранить его?", reply_markup=yes_or_not)
    except:
        await call.message.answer("Произошла ошибка, попробуйте позже",
                                  reply_markup=check_password_back)


@dp.callback_query_handler(text="not_to_save")
async def pin_message_yes(call: types.CallbackQuery):
    await call.message.answer("Без проблем, ты можешь продолжить создание в любое время",
                              reply_markup=check_password_back)


@dp.callback_query_handler(text="save")
async def pin_message_yes(call: types.CallbackQuery, state: FSMContext):
    message = await call.message.answer("Для чего вам нужен этот пароль?\n"
                                        "Пример: \"Пароль для казино\"\n\n"
                                        "<b>Совет</b>:\n"
                                        "Пиши по примеру, потому что скоро пароль будет закреплён,"
                                        "так будет легче его искать"
                                        )
    d_message = message
    await Del.first()
    await state.update_data(del_message=d_message)


@dp.message_handler(state=Del.D1)
async def add_pin(message: types.Message, state: FSMContext):
    data = await state.get_data()
    message_id = data["del_message"]
    message_id = message_id.message_id
    await dp.bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await dp.bot.pin_chat_message(chat_id=message.from_user.id, message_id=message.message_id)
    await message.answer("Отлично, ваш пароль закреплён!\n", reply_markup=check_password_back)
    await state.finish()
