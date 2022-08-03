from aiogram.dispatcher.filters.state import State, StatesGroup


class Feedback(StatesGroup):
    F1 = State()
    F2 = State()
    F3 = State()
    Good_feedback = State()
