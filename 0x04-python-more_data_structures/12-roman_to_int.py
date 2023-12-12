#!/usr/bin/python3
def to_subtract(list_num):
    sub_tow = 0
    maxi_list = max(list_num)

    for x in list_num:
        if maxi_list > x:
            sub_tow += x

    return (maxi_list - sub_tow)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listOfKeys = list(rom_num.keys())

    num = 0
    last_roman = 0
    list_numb = [0]

    for b in roman_string:
        for r_numb in listOfKeys:
            if r_numb == b:
                if rom_num.get(b) <= last_roman:
                    num += to_subtract(list_numb)
                    list_numb = [rom_num.get(b)]
                else:
                    list_numb.append(rom_num.get(b))

                last_roman = rom_num.get(b)

    num += to_subtract(list_numb)

    return (num)
