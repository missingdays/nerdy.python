#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

# Pi string
pi = "31415926535897932384626433833"

# For every test case
for i in range(int(input())):

    # Current index of the number we should get
    pi_c = 0

    # Assume input string is the song
    song = True

    # For every word in the input string
    for word in input().split():

        # If length of the word doesn't match current number
        if len(word) != int(pi[pi_c]):
            # It's not a song!
            song = False

        # Increase number counter
        pi_c += 1

    if song:
        print("It's a pi song.")
    else:
        print("It's not a pi song.")
