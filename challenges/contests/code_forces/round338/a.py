#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

[n, m] = list(map(int, input().split()))

l = [0 for i in range(m)]

for i in range(n):
    a = list(map(int, input().split()))

    for i in range(1, a[0]+1):
        l[a[i]-1] = True

if(all(l)):
    print("YES")
else:
    print("NO")
