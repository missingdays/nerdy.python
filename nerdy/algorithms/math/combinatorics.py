
from . import *

def permutations(n):
    return factorial(n)

def permutations_with_repetition(ns):
    return factorial(sum(ns)) // product(factorial(n) for n in ns)
