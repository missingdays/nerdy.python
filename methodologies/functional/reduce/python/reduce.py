#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
Comparison reduce in functional programming vs cycles in imperative
"""

# Imperative functions

def imperative_sum(a):
    s = 0
    for elem in a:
        s += elem
    return s

def imperative_mul(a):
    m = 1
    for elem in a:
        m *= elem
    return m

# Functional

def reduce(a, f, initial):
    if len(a) == 0:
        return initial
    return reduce(a[1:], f, f(initial, a[0]))

def functional_sum(a):
    s = lambda a, b: a + b
    return reduce(a, s, 0)

def functional_mul(a):
    m = lambda a, b: a * b
    return reduce(a, m, 1)

# Are they equal?

a1 = [1, 2, 3, 4, 5]
a2 = [-1, 0, 10, 15]

print(imperative_sum(a1) == functional_sum(a1))
print(imperative_sum(a2) == functional_sum(a2))

print(imperative_mul(a1) == functional_mul(a1))
print(imperative_mul(a2) == functional_mul(a2))
