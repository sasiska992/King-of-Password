import random


def from_russian_to_english(text):
    layout = dict(zip(map(ord, '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''),
                      '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''))
    return text.translate(layout)


for i in range(100):
    with open('adjective_list.txt', "r", encoding='utf-8') as file:
        adjective_list = list(file.readlines())
        adjective = adjective_list[random.randint(1, len(adjective_list) - 1)]
        adjective = adjective.replace('\n', ' ')

    with open("noun_list.txt", "r", encoding='utf-8') as file:
        noun_list = list(file.readlines())
        noun = noun_list[random.randint(1, len(noun_list) - 1)]
        noun = noun.replace('\n', ' ')

    with open("verb_list.txt", "r", encoding='utf-8') as file:
        verb_list = list(file.readlines())
        verb = verb_list[random.randint(1, len(verb_list) - 1)]
        verb = verb.replace('\n', ' ')

    with open("last_noun_list.txt", "r", encoding='utf-8') as file:
        last_noun_list = list(file.readlines())
        last_noun = last_noun_list[random.randint(1, len(last_noun_list) - 1)]
        last_noun = last_noun.replace('\n', ' ')

    random_numbers = [i for i in range(100)]

    random_number = random.choice(random_numbers)
    two_to_four = ["2", "3", "4"]
    after_ten = [i for i in range(10, 20)]
    if str(random_number)[-1] in two_to_four and random_number not in after_ten:
        funny_password = adjective + noun + verb + last_noun + f"{random_number} раза"
    else:
        funny_password = adjective + noun + verb + last_noun + f"{random_number} раз"
    with open("funny_password.txt", "a", encoding='utf-8') as file:

        file.writelines(funny_password + "\n")
