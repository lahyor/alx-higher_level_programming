#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_dict = sorted(a_dictionary)
    for key in ordered_dict:
        print("{}: {}".format(key, a_dictionary[key]))
