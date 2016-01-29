#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def child_to_cry(a):
    for i in range(len(a)):
        if a[i][2] < 0:
            return i
    return -1

n = int(input())

a = []

heroes = []

for i in range(n):
    a.append([int(i) for i in input().split()])
    a[i].append(i)

while len(a) > 0:
    child_i = child_to_cry(a)

    if child_i == -1:
        child = a.pop(0)

        heroes.append(child[3] + 1)

        for i in range(len(a)):
            a[i][2] -= child[0]
            child[0] -= 1

            if child[0] == 0:
                break
    else:
        child = a.pop(child_i)

        for i in range(child_i, len(a)):
            a[i][2] -= child[1]

print(len(heroes))
for hero in heroes:
    print(hero, end=" ")
print()
