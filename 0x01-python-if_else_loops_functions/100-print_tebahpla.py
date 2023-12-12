#!/usr/bin/python3
for x in range(122, 96, -1):
    char = x
    if x % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
