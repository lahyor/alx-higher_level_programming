#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_dict = {}
    for i, value in a_dictionary.items():
        mult_dict.update({i: (value * 2)})
    return mult_dict
