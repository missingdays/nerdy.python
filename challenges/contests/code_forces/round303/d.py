#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def sum_array(a):
    s = 0
    for elem in a:
        s += elem
    return s

n = int(input())

queue = list(map(int, input().split()))

queue.sort()

sat = [ True for i in range(n)]
s = 0
for i in range(n):
    if queue[i] < s:
        sat[i] = False
    s += queue[i]
free = 0
while sat[free] and free<n-1:
    free += 1

next_person = free + 1
while next_person < n-1:
    s = sum_array(queue[:free])
    while next_person < n-1 and queue[next_person] < s:
        next_person += 1
    if queue[next_person] >= s:
        queue[next_person], queue[free] = queue[free], queue[next_person]
        sat[free] = True
    while sat[free] and free < n - 1:
         free += 1
    next_person += 1    

count = 0
for elem in sat:
    if elem:
        count += 1
print(count) 
