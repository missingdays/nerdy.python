#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def calc(s):
    count = 0
    for c in s: 
        if c == "3":
            count += 1
    return count

s1 = input()
s2 = input()

s3 = [ "" for i in range(len(s2))]

for i in range(len(s2)):
    if s1[i] != s2[i]:
        s3[i] = "3"
    else:
        s3[i] = s1[i]

threes = calc(s3)
if threes % 2 == 1:
    print("impossible")
else:
    count = 0
    for i in range(len(s3)):
        if s3[i] == "3":
            if count % 2 == 0  :
                s3[i] = s2[i] 
                count += 1
            else:   
                s3[i] = s1[i] 
                count += 1
    print(''.join(s3))
