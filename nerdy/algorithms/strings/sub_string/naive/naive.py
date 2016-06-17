#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

'''
    type: algorithm
    theme: string
    sub-theme: sub string search
    name: naive
    author of code: Evgeny @missingdays Bovykin

'''

def substring_index(original, substring):
    """
    Finds first encounter of substring in original string using linear search
    """

    for i in range(len(original) - len(substring) + 1):
        for j in range(len(substring)):
            if original[i+j] != substring[j]:
                break
        else:
            return i
    return -1    
