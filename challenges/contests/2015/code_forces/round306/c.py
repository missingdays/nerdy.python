#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def check(s):
    for i in range(len(s)-2):
        for j in range(i+1, len(s)-1):
            for k in range(j+1, len(s)):
                if int(s[i] + s[j] + s[k]) % 8 == 0:
                    return int(s[i]+s[j] + s[k])
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if int(s[i]+s[j]) % 8 == 0:
                return int(s[i]+s[j])
    return -1        

s = input()
if "0" in s:
    print("YES")
    print(0)
elif "8" in s:
    print("YES")
    print(8)
else:
    answ = check(s)
    if answ >= 0:
        print("YES")
        print(answ)
    else:
        print("NO")
