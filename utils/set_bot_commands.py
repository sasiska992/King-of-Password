from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", "Список моих команд"),
            types.BotCommand("create", "Придумать пароль"),
            types.BotCommand("check", "Исследовать пароль"),
            types.BotCommand("recommendations", "Рекомендации по безопасности"),
            types.BotCommand("cat", "КОТИКИ!"),
            types.BotCommand("feedback", "Отзыв"),
            types.BotCommand("relink", "Пригласить друга"),
            types.BotCommand("donate", "Отблагодарить моего хозяина"),
            types.BotCommand("show_id", "Мой Telegram ID"),
            types.BotCommand("try_luck", "Испытать удачу"),
            types.BotCommand("invitations", "Сколько людей я пригласил?"),
        ]
    )
