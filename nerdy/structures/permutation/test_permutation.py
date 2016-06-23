
from math import factorial

from . import Permutation

n = 5
def test_permutation_init():

    permutation = Permutation(n)

    for i in range(n):
        assert permutation[i] == i+1

def test_permutation_equal():

    p1, p2 = Permutation(1), Permutation(1)

    assert p1 == p2

    p1, p2 = Permutation(2).next(), Permutation(2).next()

    assert p1 == p2

    p1, p2 = Permutation(n), Permutation(n)

    for i in range(n):
        p1 = p1.next()
        p2 = p2.next()

    assert p1 == p2

    p1, p2 = Permutation(1), Permutation(2)
    
    assert p1 != p2

    p1, p2 = Permutation(2), Permutation(2).next()

    assert p1 != p2

    p1, p2 = Permutation(n), Permutation(n).next()

    for i in range(factorial(n)):
        assert p1 != p2
        p1 = p1.next()
        p2 = p2.next()

def test_permutation_next():

    permutation = Permutation(n)

    permutation = permutation.next()
    assert permutation[0] == 1
    assert permutation[1] == 2
    assert permutation[2] == 3
    assert permutation[3] == 5
    assert permutation[4] == 4

    permutation = permutation.next()
    assert permutation[0] == 1
    assert permutation[1] == 2
    assert permutation[2] == 4
    assert permutation[3] == 3
    assert permutation[4] == 5

    permutation = permutation.next()
    assert permutation[0] == 1
    assert permutation[1] == 2
    assert permutation[2] == 4
    assert permutation[3] == 5
    assert permutation[4] == 3

    permutation.numbers = list(range(n, 0, -1))
    permutation = permutation.next()

    assert permutation == range(1, n+1)
