from aiogram.dispatcher.filters.state import StatesGroup, State


class MySG(StatesGroup):
    main = State()


class DialogSG(StatesGroup):
    len_pass = State()
    type = State()
    finish = State()
    first = State()
    second = State()
    third = State()
