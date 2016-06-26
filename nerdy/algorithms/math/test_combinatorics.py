
from . import *

def test_permutations():

    for i in range(100):
        assert permutations(i) == factorial(i)

def test_permutations_with_repetition():

    assert permutations_with_repetition([]) == 1
    assert permutations_with_repetition([1]) == 1
    assert permutations_with_repetition([1, 1, 1, 1, 1, 1]) == factorial(6)

    assert permutations_with_repetition([2]) == 1
    assert permutations_with_repetition([10000]) == 1

    assert permutations_with_repetition([2, 2]) == 6
    assert permutations_with_repetition([2, 2, 2]) == 90
    assert permutations_with_repetition([3, 3]) == 20
    assert permutations_with_repetition([1, 2, 3]) == 60

