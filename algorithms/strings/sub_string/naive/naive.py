#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

'''
    type: algorithm
    theme: string
    sub-theme: search of sub string
    name: naive
    author of code: Evgeny @missingdays Bovykin

'''

def index(original, sub):
    ori_len = len(original)
    sub_len = len(sub)
    for i in range(0, ori_len - sub_len + 1):
        yes = True
        for j in range(0, sub_len):
            if original[i+j] != sub[j]:
                yes = False
                break
        if yes:
            return i
    return -1    

print(index("hello", "l"))
print(index("hello world", "world"))
print(index("hello world", "wrld"))
i = raw_input("now you > ").split()
print(index(i[0], i[1]))
