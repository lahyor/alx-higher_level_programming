#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ref = 0
    for c in range(x):
        try:
            print("{}".format(my_list[c]), end="")
            ref += 1
        except IndexError:
            break
    print("")
    return (ref)
