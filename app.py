from aiogram import executor
from loader import dp, db
import middle_wares, filters, handlers
from utils.notify_admins import on_startup_admins, on_shutduwn_admins
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await db.create()
    await db.create_table_users()
    await set_default_commands(dp)
    await on_startup_admins(dp)


async def on_shutdown(dp):
    await on_shutduwn_admins(dp)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown)
