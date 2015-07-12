#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def pali(elem):
    for i in range(len(elem) // 2):
        if elem[i] != elem[len(elem) - i - 1]:
            return False
    return True    

def check(l):
    for elem in l:
        if not pali(elem):
            return False
    return True    


s = input()
k = int(input())
if len(s) % k == 0:
    k = len(s) // k
    l = [s[i:i+k] for i in range(0, len(s), k)]
    yes = check(l)

    if yes: 
        print("YES")
    else:
        print("NO")
else:
    print("NO")

