from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keybords.inline.feedback import feedback, get_feedback, confirm
from keybords.inline.inline_buttons import check_password_back
from loader import dp, db
from states.feedback import Feedback


@dp.message_handler(commands="feedback")
async def ask_feedback(message: types.Message):
    await message.answer("Какую оценку вы поставите моей работе?",
                         reply_markup=feedback)


@dp.callback_query_handler(Text(startswith="feedback_bad"))
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Прошу прощение за предоставленные неудобства\n"
                                 "Желаете ли Вы оставить отзыв?",
                                 reply_markup=get_feedback)
    await state.set_state(Feedback.F1)
    await state.update_data(mark=call.data[-1])


@dp.callback_query_handler(Text(startswith="feedback_good"))
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("Я очень рад, что понравился Вам =)\n"
                                 "Желаете ли Вы оставить отзыв?",
                                 reply_markup=get_feedback)
    await state.set_state(Feedback.Good_feedback)
    await state.update_data(mark=call.data[-1])


@dp.callback_query_handler(state=Feedback.Good_feedback, text="add_feedback")
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    del_message = await call.message.edit_text("Опишите Ваш восторг от общения со мной ниже  ❦")
    await state.set_state(Feedback.F2)
    await state.update_data(del_message=del_message)


@dp.callback_query_handler(state=Feedback.F1, text="add_feedback")
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    del_message = await call.message.edit_text("Опишите Вашу проблему ниже")
    await Feedback.next()
    await state.update_data(del_message=del_message)


@dp.callback_query_handler(state=Feedback.F1, text="not_to_add_feedback")
@dp.callback_query_handler(state=Feedback.Good_feedback, text="not_to_add_feedback")
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await call.message.edit_text("Администратор получил Ваш отзыв!\n"
                                 "Спасибо, что помогаете становиться лучше!\n\n"
                                 "/help для просмотра команд",
                                 )
    user = await db.select_user(telegram_id=call.from_user.id)
    await dp.bot.send_message(chat_id=700186952, text=f"@{user['username']} оставил оценку {data['mark']} без описания")
    await state.finish()


@dp.message_handler(state=Feedback.F2)
async def get_mark(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await data["del_message"].delete()
    feedback_text = f"<code>{message.text}</code>\n" \
                    f"Оценка <code>{data['mark']}</code>"
    await message.answer(f"Ваш отзыв:\n<b>{message.text}</b>\n"
                         f"Ваша оценка: \"<code>{data['mark']}</code>\"",
                         reply_markup=confirm)
    await state.update_data(feedback=feedback_text)
    await Feedback.next()


@dp.callback_query_handler(state=Feedback.F3, text="change_feedback")
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    try:
        await call.message.edit_text("Какую оценку вы поставите моей работе?",
                                     reply_markup=feedback)
    except:
        await call.message.answer("Какую оценку вы поставите моей работе?",
                                  reply_markup=feedback)
    await state.finish()


@dp.callback_query_handler(text="send_feedback", state=Feedback.F3)
async def get_mark(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Администратор получил ваш отзыв", reply_markup=check_password_back)
    data = await state.get_data()
    user = await db.select_user(telegram_id=call.from_user.id)
    feedback_text = data["feedback"]
    await dp.bot.send_message(chat_id=700186952, text=f"@{user['username']} оставил отзыв:\n"
                                                      f"{feedback_text}")
    await state.finish()
