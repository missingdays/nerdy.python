#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Sherlock and gdc solution
"""

def gcd(a, b):

    while b != 0:
        a, b = b, a % b
    return a


def check(nums):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if gcd(nums[k], nums[j]) == 1 and nums[k] != nums[j]:
                return True
    return False 
    
for i in range(int(input())):

    n = int(input())

    nums = list(map(int, input().split()))

    if check(nums):
        print("YES")
    else:
        print("NO")
