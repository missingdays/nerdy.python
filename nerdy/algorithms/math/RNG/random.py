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


class Generator():
    '''
    Generates pseudo-random numbers in range [0, 1)
    Seed it with something random (for example, current time) to get different results
    '''
    def __init__(self, seed=0, p=25713, i=13849, mod=65536):
        self.seed = seed
        self.p = p
        self.i = i
        self.mod = mod

    def next(self):
        self.seed = (self.seed * self.p + self.i) % self.mod
        return self.seed / self.mod

    @property
    def seed(self):
        return self._seed
    @seed.setter
    def seed(self, seed):
        self._seed = seed