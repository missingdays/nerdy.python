#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.


a, b, c = list(map(int, input().split()))

if a + b < c:
    print((a+b)*2)
elif a + c < b:
    print((a+c)*2)
elif b + c < a:
    print((c+b)*2)
else:
    print(a+b+c)
