#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

# Numbers of ints
N = int(input())

# Length of list we will be minimizing
K = int(input())

nums = []

# Read nums from input
for i in range(N):
    nums.append(int(input()))

# Sort them
nums.sort()

# Assume minimum diff is the biggest element - 0
min_d = nums[N-1]

# Check every (max - min) function 
for i in range(N-K):

    # If it's smaller then minimum diff
    if nums[i+K-1] - nums[i] < min_d:

        # Minimum diff is current diff
        min_d = nums[i+K-1] - nums[i]

print(min_d)
