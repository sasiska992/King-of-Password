from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

feedback = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1",
                          callback_data="feedback_bad1"),
     InlineKeyboardButton(text="2",
                          callback_data="feedback_bad2"),
     InlineKeyboardButton(text="3",
                          callback_data="feedback_bad3"),
     InlineKeyboardButton(text="4",
                          callback_data="feedback_good4"),
     InlineKeyboardButton(text="5",
                          callback_data="feedback_good5"),
     ]
])

get_feedback = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Да",
                          callback_data="add_feedback"),
     InlineKeyboardButton(text="Нет",
                          callback_data="not_to_add_feedback")]])

confirm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Отправить",
                          callback_data="send_feedback"),
     InlineKeyboardButton(text="Изменить",
                          callback_data="change_feedback")]])
