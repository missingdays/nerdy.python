#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

def print_arr(arr):
    for elem in arr:
        print(elem, end=" ")
    print("")

for i in range(int(input())):

    stones = int(input()) - 1
    a = int(input())
    b = int(input())

    if b > a:
        a,b = b,a

    stone_a = 0
    stone_b = stones 
    
    answ = []

    for k in range(stones + 1):

        last = 0
    
        for j in range(stone_a):

            last += a

        stone_a += 1

        for j in range(stone_b):

            last += b

        stone_b -= 1

        answ.append(last)

    print_arr(answ)
