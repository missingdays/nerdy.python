
from . import Permutation

n = 5
def test_permutation_init():

    permutation = Permutation(n)

    for i in range(n):
        assert permutation[i] == i+1

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
    
    for e1, e2 in zip(permutation, range(1, n+1)):
        assert e1 == e2

