from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def send_password(password):
    password = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Поделиться",
                              switch_inline_query="\nПриветик, я тут пароль для тебя создал, "
                                                  "взгляни на него!\n\n"
                                                  f"{password} (он копируется при нажатии)\n"
                                                  f"Создавай пароли вместе со мной!",
                              )]])

    return password


def send_phrase_password(password):
    password = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Поделиться",
                              switch_inline_query="\nПриветик, я тут постарался для тебя, "
                                                  "взгляни!\n\n"
                                                  f"{password}\n"
                                                  f"Создавай пароли вместе со мной!"
                              )]])

    return password
