from aiogram import types
from aiogram.dispatcher.filters import Text

from data.settings import SBER_TOKEN
from keybords.inline.donate import donate_count
from keybords.inline.inline_buttons import check_password_back
from loader import dp


@dp.message_handler(commands="donate")
async def get_donate(message: types.Message):
    await message.answer("Спасибо, что решился на такой смелый поступок!\n\n"
                         "Вот тебе реквизиты для оплаты:\n"
                         "Номер карты:  <code>2202202347093035</code>  (копируется при нажатии)\n\n"
                         "Можешь переводить столько, сколько не жалко! Хозяин будет рад! ❤",
                         reply_markup=check_password_back)


@dp.message_handler(commands="test_donate")
async def get_donate(message: types.Message):
    markup = donate_count("1000-2000")
    await message.answer("Сколько ты хочешь перевести?",
                         reply_markup=markup)


@dp.callback_query_handler(Text(startswith="donate"))
async def get_count(call: types.CallbackQuery):
    count = call.data.split(":")[1]
    await dp.bot.send_invoice(chat_id=call.from_user.id,
                              title="Отблагодарить разработчика",
                              description="Номер карты 4111 1111 1111 1111 / 12/24 / 123 / 12345678",
                              provider_token=SBER_TOKEN,
                              payload="donate",
                              photo_url="https://images.saymedia-content.com/.image/t_share/MTgxODA5MDI3MTQ2MDY1MjI0/tv-series-review-spongebob-squarepants.jpg",
                              currency="rub",
                              photo_size=512,
                              need_name=False,
                              need_email=False,
                              need_phone_number=False,
                              need_shipping_address=False,
                              start_parameter="example",
                              prices=[
                                  types.LabeledPrice(label="Донат",
                                                     amount=int(count) * 100)
                              ])


@dp.pre_checkout_query_handler()
async def checkout_process(pre_checkout_query: types.PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=types.ContentTypes.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await message.answer("Моему хозяину пришла ваша денюжка!\n"
                         f"Он позвонил мне и попросил передать огромное спасибо за "
                         f"{round(int(message.successful_payment.total_amount) / 100)}₽!")
    await dp.bot.send_message(chat_id=700186952,
                              text=f"@{message.from_user.username} задонатил целых "
                                   f"{round(int(message.successful_payment.total_amount) / 100)} рублей!!!")
