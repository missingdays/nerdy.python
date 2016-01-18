#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def perfect(number):

    if len(number) == 1 and number[0] == "0":
        return True

    if number[0] != "1":
        return False

    for i in range(1, len(number)):
        if number[i] != "0":
            return False

    return True

def zeros(number):
    return len(number) - 1           

def calc(n, numbers):

    answ = []
    found = -1

    for i in range(n):
        if not perfect(numbers[i]):
            answ.append(numbers[i])
            found = i

    if found == -1:
        answ.append("1")           

    for i in range(n):
        if i != found:
            answ.append("0" * zeros(numbers[i]))
        if numbers[i] == "0":
            return "0"

    return "".join(answ)

n = int(input())

numbers = input().split()

print(calc(n, numbers))