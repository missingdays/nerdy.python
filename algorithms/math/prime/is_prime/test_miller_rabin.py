
from miller_rabin import is_prime as miller_rabin_is_prime
from linear_search import is_prime as linear_search_is_prime

def test_miller_radin_is_prime():

    for i in range(2, 1000):
        assert miller_rabin_is_prime(i) == linear_search_is_prime(i)

    assert miller_rabin_is_prime(3571)
    assert miller_rabin_is_prime(10000019)

    assert not miller_rabin_is_prime(3571 * 10000019)
