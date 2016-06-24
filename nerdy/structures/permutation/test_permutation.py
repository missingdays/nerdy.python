
from math import factorial

from . import Permutation

n = 7
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

    n = 5

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

def test_permutation_rank():

    p = Permutation(1)

    assert p.rank() == 0

    p = Permutation(2)

    assert p.rank() == 0
    assert p.next().rank() == 1
    assert p.next().next().rank() == 0

    p = Permutation(n)

    current_rank = 0

    for i in range(factorial(n)):
        assert current_rank == p.rank()

        p = p.next()
        current_rank += 1

        current_rank %= factorial(n)

def test_permutation_from_rank():

    p = Permutation.from_rank(n=0, rank=0)
    assert p == Permutation(0)

    p = Permutation.from_rank(n=1, rank=0)
    assert p == Permutation(1)

    p = Permutation.from_rank(n=2, rank=0)
    assert p == Permutation(2)

    p = Permutation.from_rank(n=2, rank=1)
    assert p == Permutation(2).next()

    p = Permutation.from_rank(n=3, rank=0)
    assert p == Permutation(3)

    p = Permutation.from_rank(n=3, rank=1)
    assert p == Permutation(3).next()

    expected_p = Permutation(n=n)
    for i in range(factorial(n)):
        p = Permutation.from_rank(n=n, rank=i)

        assert p == expected_p
    
        expected_p = expected_p.next()
