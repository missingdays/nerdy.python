#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""
    type: algorithm
    theme: math
    sub-theme: random
    name: gen_random
    author of code: Evgeny @missingdays Bovykin
"""

from time import time

'''
    Generates pseudo-random numbers in range [0, 1)
    Seed it with something random like time to get random-like results
'''
class Generator():
    def __init__(self, seed=0, p=25713, i=13849, m=65536):
        self.seed = seed
        self.p = p
        self.i = i
        self.m = m

    def gen(self):
        self.seed = (self.seed * self.p + self.i) % self.m
        return self.seed / self.m

    def set_seed(self, seed):
        self.seed = seed

generator = Generator()

# These are always the same
print(generator.gen())
print(generator.gen())
print(generator.gen())

# These differ

generator.set_seed(time())
print(generator.gen())
print(generator.gen())
print(generator.gen())
