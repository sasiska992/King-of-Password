import asyncio
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utils.choose_sticker import googling_sticers


async def two_ip(password: str, message):
    message1 = await message.answer("Выполняется проверка пароля...\nПодождите...")
    message2 = await message.answer_sticker(sticker=random.choice(googling_sticers))
    options = webdriver.ChromeOptions()

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70"
    )
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.headless = True
    service = Service(executable_path="utils/chromedriver.exe")
    driver = webdriver.Chrome(service=service,
                              options=options
                              )

    driver.get("https://2ip.ru/passcheck/")

    message3 = await message.answer("Отлично, делаю запрос...")
    check_pass = driver.find_element(By.NAME, "pass")
    check_pass.send_keys(password)

    await asyncio.sleep(1.5)

    message4 = await message.answer("Ничоси, вот это у тебя пароль...")

    await asyncio.sleep(1.5)
    result = driver.find_element(By.CLASS_NAME, "pass-checker_info__reason")
    dif_pass = driver.find_element(By.CLASS_NAME, "pass-checker_info__time").text.split("за")

    long_time = float(dif_pass[1].split("лет")[0].split(" ")[2])
    time_value = dif_pass[1].split(" ")[3]
    bad_number = int(f"{'%.25f' % long_time}".split(".")[0])
    good_number = f"{bad_number:,}"

    message5 = await message.answer("Отравляю собранную информацию по паролю...")

    await asyncio.sleep(1.5)
    await message1.delete()
    await message2.delete()
    await message3.delete()
    await message4.delete()
    await message5.delete()
    message6 = await message.answer("Секундочку, надо укомплектовать данные...")
    await asyncio.sleep(1.5)
    time_hacking = f"Ваш пароль может быть взломан за {good_number} {time_value}"
    return [result.text, time_hacking, message6]
