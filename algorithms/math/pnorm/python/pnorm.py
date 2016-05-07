#!/bin/python3
"""
Norm is a general way to calculate a length of some vector.
Any common distances like Manhattan or Euclidean can be expressed in it.
"""
def pnorm(vector, p):
    powers = [pow(i, p) for i in vector]
    s = sum(powers)
    return pow(s, 1.0/p)

"""
2d pnorm
"""
def pnorm_2(x, y, p):
    return pnorm([x, y], p)


def manhattan_distance(x, y):
    return pnorm_2(x, y, 1)

def euclidean_distance(x, y):
    return pnorm_2(x, y, 2)

