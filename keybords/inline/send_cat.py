from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

send_cat = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Котики!",
                              callback_data="cats"),
         InlineKeyboardButton(text="Не котики :(",
                              callback_data="help")]
    ])
