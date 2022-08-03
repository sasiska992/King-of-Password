from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keybords.inline.callback_data import pass_callback

len_password_first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<<<", callback_data=pass_callback.new("the_first", 0)),
            InlineKeyboardButton(text="4", callback_data=pass_callback.new("number_add", 4)),
            InlineKeyboardButton(text="5", callback_data=pass_callback.new("number_add", 5)),
            InlineKeyboardButton(text="6", callback_data=pass_callback.new("number_add", 6)),
            InlineKeyboardButton(text=">>>", callback_data=pass_callback.new("next_first", 0))]
    ])

len_password_second = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<<<", callback_data=pass_callback.new("last_first", 4)),
            InlineKeyboardButton(text="7", callback_data=pass_callback.new("number_add", 7)),
            InlineKeyboardButton(text="8", callback_data=pass_callback.new("number_add", 8)),
            InlineKeyboardButton(text="9", callback_data=pass_callback.new("number_add", 9)),
            InlineKeyboardButton(text=">>>", callback_data=pass_callback.new("next_second", 0))]
    ])

len_password_third = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="<<<", callback_data=pass_callback.new("last_second", 0)),
            InlineKeyboardButton(text="10", callback_data=pass_callback.new("numbers_add", 10)),
            InlineKeyboardButton(text="11", callback_data=pass_callback.new("numbers_add", 11)),
            InlineKeyboardButton(text="12", callback_data=pass_callback.new("numbers_add", 12))
        ]
    ])
