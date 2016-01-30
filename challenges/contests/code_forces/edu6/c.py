#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def good(nums):
    for num in nums:
        if nums[num] > 1:
            return True
    return False

n = int(input())

a = [int(i) for i in input().split()]

s = []

l, r = 0, 0
nums = {}

for i in range(n):
    num = a[i]

    if num in nums:
        break
    else:
        nums[num] = True
else:
    print(-1)
    exit()

nums = {}

while r < n:
    while r < n:
        num = a[r]

        if num in nums:
            r += 1
            break
        else:
            nums[num] = True

        r += 1

    r -= 1

    s.append([l, r])
    r += 1
    l = r

    nums = {}

length = len(s)

last = s[length-1]

for i in range(last[0], last[1]+1):
    num = a[i]
    if num in nums:
        print(length)
        break
    else:
        nums[num] = True
else:
    s.pop()

    s[length-2][1] = n-1

    print(length-1)

for st in s:
    for c in st:
        print(c+1, end=" ")
    print()

