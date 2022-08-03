from aiogram import types
from aiogram_dialog import DialogManager, StartMode

from keybords.inline.callback_data import pass_callback
from keybords.inline.inline_buttons import inlineb
from loader import dp
from states.aiogram_dialog import DialogSG


@dp.callback_query_handler(pass_callback.filter(mode="create_password"))
@dp.message_handler(commands="create")
async def show_inlineb(message: types.Message):
    await message.answer("Выберите случайный пароль или парольную фразу", reply_markup=inlineb)


@dp.callback_query_handler(pass_callback.filter(mode="random"))
async def generate_pass(call: types.CallbackQuery, dialog_manager: DialogManager):
    await dialog_manager.start(DialogSG.len_pass, mode=StartMode.RESET_STACK)
