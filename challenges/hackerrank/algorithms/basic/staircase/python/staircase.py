#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('#', end='')
    print() # new line    
