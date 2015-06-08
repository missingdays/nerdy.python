#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
The time in words solution
"""

words = {

    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty"


}

def parse_minutes(M):
    if M in words:
        return words[M]
    else:
        return words[M // 10 * 10] + " " + words[M % 10]

H = int(input())
M = int(input())

if M == 0:
    print(words[H] + " o' clock")
else:
    if M == 15:
        print("quarter past " + words[H])
    elif M == 45:
        print("quarter to " + words[H+1])
    elif M == 30:
        print("half past " + words[H])
    elif M < 30:
        print(parse_minutes(M) + " minutes past " + words[H])
    else:
        print(parse_minutes(60-M) + " minutes to " + words[H+1])
