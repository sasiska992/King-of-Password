from aiogram import types
from aiogram.dispatcher import FSMContext

from keybords.inline.callback_data import pass_callback
from keybords.inline.inline_buttons import check_password_back
from loader import dp
from states.check_password import Check
from utils.texts import help_text
from utils.two_ip import two_ip


@dp.message_handler(commands=["check"])
async def check_password_command(message: types.Message):
    await message.answer("Итак, попробуй ввести свой пароль, а я гляну, "
                         "засветился он где-то уже или нет\n\n"
                         "Не обращай внимания на кнопку снизу, ты спокойно можешь вводить пароль! :)",
                         reply_markup=check_password_back)
    await Check.first()


@dp.callback_query_handler(state=Check.C1)
@dp.callback_query_handler(pass_callback.filter(mode="help"))
async def check_password_command_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(help_text)
    await state.finish()


@dp.message_handler(state=Check.C1)
async def answer_password(message: types.Message, state: FSMContext):
    try:
        dif_pass = await two_ip(password=message.text, message=message)
        await dif_pass[2].delete()
        await message.answer("Вот что я узнал:\n\n"
                             f"{dif_pass[0]}\n"
                             f"{dif_pass[1]}", reply_markup=check_password_back)
    except:
        await message.answer("Произошла ошибка, попробуйте позже",
                                  reply_markup=check_password_back)

    await state.finish()
