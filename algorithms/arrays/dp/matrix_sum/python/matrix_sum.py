#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 missingdays <missingdays@missingdays>
#
# Distributed under terms of the MIT license.

"""

"""

def copy(a):
    b = [[] for i in range(len(a))]

    for i in range(len(a)):
        for j in range(len(a[i])):
            b[i].append(a[i][j])

    return b

def biggest_sum(a):
    n = len(a)

    b = copy(a)

    for i in range(n):
        for j in range(n):
            if i > 0:
                b[i][j] += b[i-1][j]

            if j > 0:
                b[i][j] += b[i][j-1]

            if i > 0 and j > 0:
                b[i][j] -= b[i-1][j-1]

    max_sum = -float("inf")

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    
                    subRect = b[k][l]

                    if i > 0:
                        subRect -= b[i-1][j]

                    if j > 0:
                        subRect -= b[i][j-1]

                    if i > 0 and j > 0:
                        subRect += b[i-1][j-1]

                    max_sum = max(max_sum, subRect)
    
    return max_sum

if __name__ == "__main__":

    assert biggest_sum([[1]]) == 1
    assert biggest_sum([[1, 1], [1, 1]]) == 4
    assert biggest_sum([[1, -1], [-1, 1]]) == 1
    assert biggest_sum([[10, -1], [-1, 10]]) == 18
    assert biggest_sum([[-1, -2], [1, 2]]) == 2
    assert biggest_sum([[1, 10, 10], [-2, -3, 5], [1, 1, -1]]) == 23
