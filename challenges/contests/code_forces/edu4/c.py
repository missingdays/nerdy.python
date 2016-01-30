#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

opening = {
        "[": "]",
        "<": ">",
        "{": "}",
        "(": ")",
}

closing = {
        "]": "[",
        ">": "<",
        "}": "{",
        ")": "(",
}

s = input()

stack = []

answ = 0

for c in s:
    if c in opening:
        stack.append(c)
    else:
        if len(stack) == 0:
            print("Impossible")
            exit()

        op = stack.pop()

        if c != opening[op]:
            answ += 1

if len(stack) != 0:
    print("Impossible")
    exit()
print(answ)
