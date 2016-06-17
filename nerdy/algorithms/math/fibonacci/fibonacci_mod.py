#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

def fib_mod(n, m):
    """
    Fast Fibonacci mod m computing
    """
    
    a11 = 1
    a12 = 1
    a21 = 1
    a22 = 0
    r11 = 1
    r12 = 0
    q11 = 0 
    q12 = 0
    q21 = 0 
    q22 = 0
    while n > 0:
        if (n&1) == 1:
            q11 = (r11 * a11 + r12 * a21) % m
            q12 = (r11 * a12 + r12 * a22) % m
            r11 = q11
            r12 = q12
        q11 = (a11 * a11 + a12 * a21) % m
        q12 = (a11 * a12 + a12 * a22) % m
        q21 = (a21 * a11 + a22 * a21) % m
        q22 = (a21 * a12 + a22 * a22) % m
        a11 = q11
        a12 = q12
        a21 = q21
        a22 = q22
 
        n >>= 1

    return r12
