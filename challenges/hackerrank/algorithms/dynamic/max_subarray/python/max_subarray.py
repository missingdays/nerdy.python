#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Maximum subarray problem solution
"""

def max_subarray(array):
    curr_sum = 0
    curr_index = 0
    best_sum = 0
    best_start_index = 0
    best_ending_index = 0
 
    for i in range(len(array)):
        val = curr_sum + array[i]

        if val > 0:
            if curr_sum == 0:
                curr_index = i
            curr_sum = val
        else:
            curr_sum = 0
 
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_start_index = curr_index
            best_ending_index = i
    return array[best_start_index:best_ending_index+1]

def sum_positive(array):
    s = 0
    for elem in array:
        if elem > 0:
            s += elem
    if s == 0:
        mv = array[0]
        for elem in array:
            if elem > mv:
                mv = elem
        return mv
    else:
        return s

for i in range(int(input())):
    n = input()
    inp = list(map(int, input().split()))
    
    print(sum(max_subarray(inp)), end=" ")
    print(sum_positive(inp))
