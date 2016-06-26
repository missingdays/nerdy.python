
from . import *

def test_is_prime_linear_search():

    for i in range(2, 1000):
        assert is_prime_miller_rabin(i) == is_prime_linear_search(i)

    assert is_prime_miller_rabin(3571)
    assert is_prime_miller_rabin(10000019)

    assert not is_prime_miller_rabin(3571 * 10000019)

def test_is_prime_linear_search():

    assert is_prime_linear_search(2)
    assert is_prime_linear_search(3)
    assert is_prime_linear_search(5)
    assert is_prime_linear_search(7)
    assert is_prime_linear_search(11)
    assert is_prime_linear_search(13)

    assert not is_prime_linear_search(4)
    assert not is_prime_linear_search(6)
    assert not is_prime_linear_search(8)
    assert not is_prime_linear_search(9)
    assert not is_prime_linear_search(10)
    assert not is_prime_linear_search(12)
    
    assert not is_prime_linear_search(11*11)
    assert not is_prime_linear_search(13*13)

    assert is_prime_linear_search(3571)
    assert is_prime_linear_search(10000019)

    assert not is_prime_linear_search(3571 * 10000019)
