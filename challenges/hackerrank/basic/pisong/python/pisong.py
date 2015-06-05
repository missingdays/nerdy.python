#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

pi = "31415926535897932384626433833"

for i in range(int(input())):
    pi_c = 0
    song = True
    for word in input().split():
        if len(word) != int(pi[pi_c]):
            song = False
        pi_c += 1
    if song:
        print("It's a pi song.")
    else:
        print("It's not a pi song.")
