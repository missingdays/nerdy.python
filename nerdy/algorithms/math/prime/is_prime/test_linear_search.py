
from linear_search import is_prime

def test_linear_search_is_prime():

    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)

    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert not is_prime(12)
    
    assert not is_prime(11*11)
    assert not is_prime(13*13)

    assert is_prime(3571)
    assert is_prime(10000019)

    assert not is_prime(3571 * 10000019)
