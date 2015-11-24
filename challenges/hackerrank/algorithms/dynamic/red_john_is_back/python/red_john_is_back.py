#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

class Calculator():
    def __init__(self):
        self.values = {}
        
    def calculate(self, n):
        if n in self.values:
            return self.values[n]
        v = 0
        if n < 4:
            v = 1
        else:
            v = self.calculate(n-1) + self.calculate(n-4)
        self.values[n] = v
        return v
    
calculator = Calculator()    
    
for i in range(int(input())):
    n = int(input())
    
    v = calculator.calculate(n)
    
    primes = {}
    
    for i in range(2, v+1):
        primes[i] = True
    
    for p in primes:
        factors = range(p, v+1, p)
        
        for f in factors[1:]:
            primes[f] = False

    c = 0
    for p in primes:
        if primes[p]:
            c += 1
    print(c)  
