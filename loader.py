from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_dialog import DialogRegistry

from data import settings
from keybords.inline.aiogram_end import db
from keybords.inline.aiogram_end import dialog

bot = Bot(token=settings.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
db = db

registry = DialogRegistry(dp)  # this is required to use `aiogram_dialog`
registry.register(dialog)  # register a dialog
