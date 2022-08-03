import random


def from_russian_to_english(text):
    layout = dict(zip(map(ord, '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''),
                      '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''))
    return text.translate(layout)


def translating():
    with open("funny_password.txt", "r", encoding='utf-8') as file:
        russian_passwords = list(file.readlines())
        russian_password = russian_passwords[random.randint(0, len(russian_passwords) - 1)]
        fool_password = russian_password.replace('\n', '').replace(" ", "", 1)
        fool_password = fool_password.replace(fool_password[0], fool_password[0].upper(), 1)

    russian_ending = fool_password.split(" ")[-2] + " " + fool_password.split()[-1]
    numbers = [str(i) for i in range(100)]
    sings = [':', '@', ';', '=', '<', '>', '?', "{", "}", "#", "$", "%", "^", "&", "*", "(", ")", "+", "№", "_"]

    len_simbols = 0
    russian_part_password = ""
    for i in russian_password:
        len_simbols += 1
        if i == " " and russian_password[0] == " ":
            first_letters_after_space = len_simbols
            third_letters_after_space = len_simbols + 3
            count_words = russian_password[first_letters_after_space:third_letters_after_space].split(" ")
            if count_words[0] in numbers or count_words[0] == "раз":
                continue
            else:
                russian_part_password += russian_password[first_letters_after_space:third_letters_after_space] + " "
    russian_part_password += russian_ending
    english_part_password = ""
    j = 0
    for i in russian_part_password:
        j += 1
        if i != " ":
            english_part_password += from_russian_to_english(i)

        if i == " " and j != len(russian_part_password):
            english_part_password += "-"

    russian_part_password = russian_part_password.replace(russian_part_password[0], russian_part_password[0].upper(), 1)

    sing_element = f"{random.choice(sings)}"
    sing_russian_element = f" {sing_element}"
    english_sing_element = f"-{sing_element}"
    russian_part_password += sing_russian_element
    fool_password += sing_russian_element
    english_part_password += f"{english_sing_element}"

    return [fool_password, russian_part_password, english_part_password]
