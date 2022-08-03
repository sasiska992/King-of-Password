from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keybords.inline.callback_data import pass_callback

inlineb = InlineKeyboardMarkup(row_width=2,
                               inline_keyboard=[
                                   [InlineKeyboardButton(text="Случайный пароль",
                                                         callback_data=pass_callback.new("random", 0)),
                                    InlineKeyboardButton(text="Парольная фраза",
                                                         callback_data=pass_callback.new("phrase", 0))],
                                   [InlineKeyboardButton(text="Вернуться к выбору команд",
                                                         callback_data="help")]
                               ])


def get_relink(relink):
    inlineb2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Поделиться",
                                  switch_inline_query=f"\nПривет, меня тут попросили с тобой ссылкой "
                                                      f"поделиться\n"
                                                      f"Заглядывай ко мне!\n{relink}")]
        ])
    return inlineb2


password_type_numbers = InlineKeyboardMarkup(row_width=1,
                                             inline_keyboard=[
                                                 [InlineKeyboardButton(text="Да!",
                                                                       callback_data=pass_callback.new("yes", 1)),
                                                  InlineKeyboardButton(text="Нет",
                                                                       callback_data=pass_callback.new("no", 3))]
                                             ])

check_password_back = InlineKeyboardMarkup(row_width=1,
                                           inline_keyboard=[
                                               [InlineKeyboardButton(text="Вернуться к выбору команд",
                                                                     callback_data="help")]
                                           ])
