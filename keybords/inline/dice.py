from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

dice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Испытать удачу",
                          callback_data="try_luck"),
     InlineKeyboardButton(text="К списку команд",
                          callback_data="help")]
])
