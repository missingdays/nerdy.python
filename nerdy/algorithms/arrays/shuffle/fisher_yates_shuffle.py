#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

import random

def shuffle(array):
    """
    Shuffles array using Fisher-Yates algorithm

    Time:
    O(n)
    Space:
    O(1) -> shuffles array is place
    """

    for i in range(len(array)):
        rand = random.randrange(i, len(array))
        array[i], array[rand] = array[rand], array[i]

    return array

def shuffled(array):
    """
    Returns new copy of shuffled array using Fisher-Yates algorithm
    """

    return shuffle(list(array))
