from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def donate_count(thousand):
    thousand = thousand.split("-")
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="<",
                              callback_data=f"back_thousand:{int(thousand[0]) - 1000}-{int(thousand[1]) - 1000}"),
         InlineKeyboardButton(text=f"{int(thousand[0]) - 1000}-{int(thousand[1]) - 1000}",
                              callback_data=f"thousand:{int(thousand[0]) - 1000}-{int(thousand[1]) - 1000}"),
         InlineKeyboardButton(text=">",
                              callback_data=f"next_thousand:{int(thousand[0]) + 1000}-{int(thousand[1]) + 1000}")
         ]
    ])

    return markup


async def get_hundred(thousand):
    hundreds = thousand.split("-")
    hundreds_keyboard = InlineKeyboardMarkup(row_width=3)
    count_buttons = 0
    hundred = int(hundreds[0])
    for i in range(3):
        if count_buttons != 3:
            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 100, 100):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}-{money_hundreds + 150}",
                    callback_data=f"hundred:{hundred}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 150

            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

        else:
            button = InlineKeyboardButton(
                text="<<<",
                callback_data=f"back_hundred:{hundred - 300}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 100, 100):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}-{money_hundreds + 150}",
                    callback_data=f"hundred:{hundred}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 150
            button = InlineKeyboardButton(
                text=">>>",
                callback_data=f"next_hundred:{hundred + 150}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1
    button = InlineKeyboardButton(
        text="К выбору тысяч",
        callback_data="get_thousand"
    )
    hundreds_keyboard.insert(button)
    return hundreds_keyboard


def get_next_or_last_hundred(hundred):
    hundreds_keyboard = InlineKeyboardMarkup(row_width=3)
    count_buttons = 0
    for i in range(3):
        if count_buttons != 3:
            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 100, 100):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}-{money_hundreds + 150}",
                    callback_data=f"hundred:{hundred}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 150
            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

        else:
            button = InlineKeyboardButton(
                text="<<<",
                callback_data=f"back_hundred:{hundred - 600}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 100, 100):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}-{money_hundreds + 150}",
                    callback_data=f"hundred:{hundred}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 150

            button = InlineKeyboardButton(
                text=">>>",
                callback_data=f"next_hundred:{hundred + 150}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1
    button = InlineKeyboardButton(
        text="К выбору тысяч",
        callback_data="get_thousand"
    )
    hundreds_keyboard.insert(button)
    return hundreds_keyboard


def get_last_donate(hundred):
    hundreds_keyboard = InlineKeyboardMarkup(row_width=4)
    count_buttons = 0
    for i in range(3):
        if count_buttons != 4:
            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 50, 25):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}₽",
                    callback_data=f"donate:{hundred + 25}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 25

            button = InlineKeyboardButton(
                text=" ",
                callback_data=f"IGNORE"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

        else:
            button = InlineKeyboardButton(
                text="<<<",
                callback_data=f"back_quarter:{hundred - 200}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1

            for money_hundreds in range(hundred, hundred + 50, 25):
                count_buttons += 1
                button = InlineKeyboardButton(
                    text=f"{money_hundreds + 25}₽",
                    callback_data=f"donate:{hundred + 25}"
                )
                hundreds_keyboard.insert(button)
                hundred = money_hundreds + 25

            button = InlineKeyboardButton(
                text=">>>",
                callback_data=f"next_quarter:{hundred + 50}"
            )
            hundreds_keyboard.insert(button)
            count_buttons += 1
    button = InlineKeyboardButton(
        text="К выбору сотен",
        callback_data="get_hundreds"
    )
    hundreds_keyboard.insert(button)
    return hundreds_keyboard
