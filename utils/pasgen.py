import random


def add_symbol_to_set(a, b):
    symbol_set = set()
    for i in range(a, b):
        symbol = chr(i)
        symbol_set.add(symbol)
    return symbol_set


def add_symbol_to_list(a, b):
    symbol_set = []
    for i in range(a, b):
        symbol = chr(i)
        symbol_set.append(symbol)
    random.shuffle(symbol_set)
    return symbol_set


def create_new_dict(s_dict: dict, choose_numbers: str):
    new_dict = {}
    for i in choose_numbers:
        new_dict[int(i)] = s_dict[int(i)]
    return new_dict


# n - symbol amount
# numbers_choose / 1 - number / 2 - lower / 3 - upper / 4 - sign / example: 124
def passgen(n, numbers_choose):
    symbol_number = add_symbol_to_list(49, 58)
    symbol_lower = add_symbol_to_list(65, 79)
    symbol_lower = add_symbol_to_list(80, 90) + symbol_lower
    symbol_upper = add_symbol_to_list(97, 111)
    symbol_upper = add_symbol_to_list(112, 122) + symbol_upper
    symbol_sign = add_symbol_to_list(58, 65)

    symbol_number_set = add_symbol_to_set(49, 58)
    symbol_lower_set_one = add_symbol_to_set(65, 79)
    symbol_lower_set_two = add_symbol_to_set(80, 90)
    symbol_lower_set = symbol_lower_set_one.union(symbol_lower_set_two)
    symbol_upper_set_one = add_symbol_to_set(97, 111)
    symbol_upper_set_two = add_symbol_to_set(112, 122)
    symbol_upper_set = symbol_upper_set_one.union(symbol_upper_set_two)
    symbol_sign_set = add_symbol_to_set(58, 65)

    symbol_dict = {1: symbol_number,
                   2: symbol_upper,
                   3: symbol_lower,
                   4: symbol_sign}

    symbol_dict_set = {1: symbol_number_set,
                       2: symbol_upper_set,
                       3: symbol_lower_set,
                       4: symbol_sign_set}

    new_symbol_dict = create_new_dict(symbol_dict, numbers_choose)
    back_up_password = create_new_dict(symbol_dict_set, numbers_choose)

    password = ""

    for i in range(n):
        elements = new_symbol_dict[random.choice(list(new_symbol_dict.keys()))]
        element = random.choice(elements)
        password += element

    united_list = [[-1]]

    back_up_same_password = password
    same_elements = []
    if len(set(password)) != len(password):
        for i in password:

            if i not in same_elements:
                same_elements.append(i)
                back_up_same_password = back_up_same_password.replace(i, " ", 1)

            else:

                if i in united_list[0] or i in same_elements:
                    united_list.append([back_up_same_password.find(i)])
                    back_up_same_password = back_up_same_password.replace(i, " ", 1)
                    united_list[0].append(i)
                else:
                    united_list.append([password.index(i)])
                    united_list[0].append(i)

    else:
        for key, value in back_up_password.items():
            united = list(value & set(password))
            if len(united) > 1:
                sub_list = []
                for i in united:
                    element_index = password.index(i)
                    sub_list.append(element_index)
                united_list.append(sub_list)
    del united_list[0]

    count = 0
    for key, value in back_up_password.items():
        if len(value & set(password)) == 0:

            if len(set(password)) == 1:
                sub_list = united_list[count]
                index_in_generate_password = sub_list[0]
                password = password.replace(password[index_in_generate_password], back_up_password[key].pop(), 1)

                if len(sub_list) > 2:
                    sub_list.remove(index_in_generate_password)
                elif len(united_list) == 1:
                    continue
                else:
                    united_list.remove(sub_list)
            else:
                sub_list = random.choice(united_list)
                index_in_generate_password = random.choice(sub_list)
                password = password.replace(password[index_in_generate_password], back_up_password[key].pop(), 1)

                if len(sub_list) > 2:
                    sub_list.remove(index_in_generate_password)
                elif len(united_list) == 1:
                    continue
                else:
                    united_list.remove(sub_list)
        count += 1

    return password
