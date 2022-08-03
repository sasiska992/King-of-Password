import operator
from typing import Any

from aiogram.types import CallbackQuery, ParseMode
from aiogram_dialog import Dialog, DialogManager, Window, ChatEvent, StartMode
from aiogram_dialog.widgets.kbd import Button, Select, Row, SwitchTo, Back, Multiselect
from aiogram_dialog.widgets.text import Const, Format, Multi

from keybords.inline.inline_buttons import check_password_back
from keybords.inline.save_pass import yes_or_not
from keybords.inline.send_password import send_password, send_phrase_password
from states.aiogram_dialog import DialogSG
from utils.data_base_api.postgresql import Database
from utils.funny_password import translating
from utils.generate_prosess import generating_process
from utils.pasgen import passgen
from utils.texts import help_text

db = Database()


async def get_data(dialog_manager: DialogManager, **kwargs):
    len_pass = dialog_manager.current_context().dialog_data.get("len_pass", None)
    return {
        "len_pass": len_pass,
        "type": dialog_manager.current_context().dialog_data.get("len_pass", None),
        "continue": len_pass in ["<<<", ">>>"],
    }


async def on_type_selected(c: CallbackQuery, widget, manager: DialogManager, selected_item: str):
    user = await db.select_user(telegram_id=c.from_user.id)
    selected_items = user.get("chosen_types")

    if selected_items == None:
        selected_items = ""
    if selected_item in selected_items:

        selected_items = selected_items.replace(selected_item, "")


    else:
        selected_items += selected_item

    await db.change_pass_type(chosen_types=selected_items, telegram_id=c.from_user.id)
    return selected_items


async def del_text(c: CallbackQuery, widget, manager: DialogManager, *args):
    try:
        user = await db.select_user(telegram_id=c.from_user.id)
        numbers_choose = user.get("chosen_types")
        pass_len = manager.current_context().dialog_data.get("len_pass", None)
        password = f"`{passgen(n=int(pass_len), numbers_choose=numbers_choose)}`"
        await c.message.answer(f"А вот и твой пароль, "
                               f"нажми на него, чтобы скопировать!",
                               parse_mode=ParseMode.MARKDOWN)
        await c.message.answer(f"➡️  `{password}`  ⬅️",
                               parse_mode=ParseMode.MARKDOWN,
                               reply_markup=send_password(
                                   f"`{password}`"))
        user = await db.select_user(telegram_id=c.from_user.id)
        await db.update_generated_passwords(telegram_id=c.from_user.id,
                                            generated_password=user.get("generated_passwords") + 1)
        await c.message.answer("Хотите ли вы сохранить его?", reply_markup=yes_or_not)
        await db.change_pass_type(chosen_types=None, telegram_id=c.from_user.id)
        await manager.done()
    except TypeError:
        await c.message.answer("Вы не выбрали тип пароля, попробуйте заново",
                               reply_markup=check_password_back)
        await manager.done()
    except:
        await c.message.answer("Произошла ошибка, попробуйте заново",
                               reply_markup=check_password_back)
        await manager.done()


async def get_phrase_pass(call: CallbackQuery, button: Button, manager: DialogManager):
    if manager.is_preview():
        await manager.done()
        return
    try:
        generating_message = await generating_process(call)
        await generating_message.delete()
        password = translating()
        sent_message = f"Итак, вот твой пароль:\n`{password[0]}` - полная фраза\n" \
                       f"`{password[1]}` - Пароль, который тебе надо ввести на английской раскладке " \
                       f"русскими буквами\n" \
                       f"`{password[2]}` - Твой окончательный пароль\n" \
                       f"Для того, чтобы скопировать, просто нажми на него\n"
        await call.message.answer(sent_message,
                                  parse_mode=ParseMode.MARKDOWN,
                                  reply_markup=send_phrase_password(sent_message))

        user = await db.select_user(telegram_id=call.from_user.id)
        await db.update_generated_passwords(telegram_id=call.from_user.id,
                                            generated_password=user.get("generated_passwords") + 1)
        await call.message.answer("Хотите ли вы сохранить его?", reply_markup=yes_or_not)
        await manager.done()
    except:
        await call.message.answer("Произошла ошибка, попробуйте позже",
                                  reply_markup=check_password_back)
        await manager.done()


async def on_finish(c: CallbackQuery, button: Button, manager: DialogManager):
    if manager.is_preview():
        await manager.done()
        return
    await c.message.answer(help_text)
    await manager.done()


async def start(c: CallbackQuery, button: Button, manager: DialogManager):
    await manager.done()
    await manager.start(DialogSG.len_pass, mode=StartMode.RESET_STACK)


async def on_len_changed(c: ChatEvent, select: Any, manager: DialogManager,
                         item_id: str):
    manager.current_context().dialog_data["len_pass"] = item_id
    await manager.dialog().switch_to(state=DialogSG.type)


def get_items():
    return [
        ("0-9", 1),
        ("a-z", 2),
        ("A-Z", 3),
        ("!№;%:*@#$", 4)
    ]


multiselect = Multiselect(
    Format("✅ {item[0]}"),  # E.g `✓ Apple`
    Format("{item[0]}"),
    id="",
    item_id_getter=operator.itemgetter(1),
    items=get_items(),
    on_click=on_type_selected
)

dialog = Dialog(
    Window(
        Format("А теперь реши, сколько будет символов в пароле?"),
        Row(
            Back(Const("<<<"), id="back1"),
            Select(
                Format("{item}"),
                items=["4", "5", "6"],
                item_id_getter=lambda x: x,
                id="pass_len",
                on_click=on_len_changed,
            ),
            SwitchTo(Const(">>>"), id="next1", state=DialogSG.first),
        ),
        state=DialogSG.len_pass,
        getter=get_data
    ),
    Window(
        Format("А теперь реши, сколько будет символов в пароле?"),
        Row(
            SwitchTo(Const("<<<"), id="back2", state=DialogSG.len_pass),
            Select(
                Format("{item}"),
                items=["7", "8", "9"],
                item_id_getter=lambda x: x,
                id="pass_len",
                on_click=on_len_changed,
            ),
            SwitchTo(Const(">>>"), id="next2", state=DialogSG.second),
        ),
        state=DialogSG.first,
        getter=get_data
    ),
    Window(
        Format("А теперь реши, сколько будет символов в пароле?"),
        Row(
            SwitchTo(Const("<<<"), id="back3", state=DialogSG.first),
            Select(
                Format("{item}"),
                items=["10", "11", "12"],
                item_id_getter=lambda x: x,
                id="pass_len",
                on_click=on_len_changed,
            ),
            Button(Const(" "), id="next3"),
        ),
        state=DialogSG.second,
        getter=get_data
    ),
    Window(
        Const("Какие символы ты хочешь добавить?\n\n"
              "1. Цифры\n"
              "2. Буквы, размером с семечку\n"
              "3. Буквы побольше\n"
              "4. Спецсимволы (<code>%№;:!</code>)"),
        multiselect,
        Row(Button(Const("<< Вернутсься <<"), id="back", on_click=start),
            Button(Const("Запросить пароль"), id="get_pass", on_click=del_text)
            ),
        state=DialogSG.type,
        getter=get_data
    ),
    Window(
        Multi(
            Format("Сгенерируйте пароль или парольную фразу"),
        ),
        Row(
            SwitchTo(Const("Случайный пароль"), id="restart", state=DialogSG.len_pass),
            Button(Const('Парольная фраза'), on_click=get_phrase_pass, id="phrase"),
        ),
        Row(
            Button(Const('Вернуться к выбору команд'), on_click=on_finish, id="finish"),
        ),
        getter=get_data,
        state=DialogSG.finish,
    ),
)
