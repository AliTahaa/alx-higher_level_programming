#!/usr/bin/python3
def _subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(roman_d.keys())

    num = 0
    last_rom = 0
    numbers = [0]

    for _char in roman_string:
        for roman_letter in list_keys:
            if roman_letter == _char:
                if roman_d.get(_char) <= last_rom:
                    num += _subtract(numbers)
                    numbers = [roman_d.get(_char)]
                else:
                    numbers.append(roman_d.get(_char))

                last_rom = roman_d.get(_char)

    num += _subtract(numbers)

    return (num)
