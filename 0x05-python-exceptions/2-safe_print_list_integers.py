#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ref = 0
    for c in range(0, x):
        try:
            print("{:d}".format(my_list[c]), end="")
            ref += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ref)
