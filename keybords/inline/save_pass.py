from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

yes_or_not = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [InlineKeyboardButton(text="Да",
                                                            callback_data="save"),
                                       InlineKeyboardButton(text="Нет",
                                                            callback_data="not_to_save")]
                                  ])