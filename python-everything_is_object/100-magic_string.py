#!/usr/bin/python3
def magic_string(word="BestSchool", n=[0]):
    n[0] += 1
    return ", ".join([word] * n[0])
