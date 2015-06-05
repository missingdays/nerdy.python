#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

import random

# Main mix function
def mixArray(array):

    # For every element in array
    for i in range(len(array)):

        # Choose a random number between current index and last
        rand = random.randrange(i, len(array))
        # Swap them
        array[i], array[rand] = array[rand], array[i]

    return array

print(mixArray([1,2,3,4,5]))
