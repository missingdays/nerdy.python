'''
    type: algorithm
    theme: math
    sub-theme: calculate
    name: Least common multiply
    author of code: Evgeny @missingdays Bovykin

'''

from nerdy.algorithms.math import gcd

def lcm(a, b):
    """
    Finds least common multiply
    """
    return a * b / gcd(a, b)