#!/usr/bin/python3
def uppercase(str):
    for c in str:
        upper = chr(ord(c) - 32) if 97 <= ord(c) <= 122 else c
        print("{}".format(upper), end="")
    print()
