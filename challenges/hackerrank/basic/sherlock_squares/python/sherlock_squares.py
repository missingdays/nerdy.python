#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

from math import ceil, sqrt

# For every test case
for i in range(int(input())):

    # Get two numbers
    nums = list(map(int, input().split()))

    # Calculate difference between theirs sqrts
    # rounded up
    diff = ceil(sqrt(nums[1])) - ceil(sqrt(nums[0]))

    # But if top number is square integer
    if ceil(sqrt(nums[1])) == sqrt(nums[1]):

        # Include it as well
        diff += 1
    print(diff)

