
from . import gcd

def test_gcd():

    assert gcd(0, 0) == 0

    assert gcd(1, 0) == 1
    assert gcd(0, 1) == 1

    assert gcd(2, 1) == 1
    assert gcd(1, 2) == 1

    assert gcd(4, 2) == 2
    assert gcd(2, 4) == 2

    assert gcd(5, 5) == 5
    assert gcd(5, 5) == 5

    assert gcd(3, 5) == 1
    assert gcd(5, 3) == 1

    assert gcd(2*3*5, 2*3*7) == 2*3
    assert gcd(2*3*5*11, 2*3*5*7) == 2*3*5

    assert gcd(10, 10*2) == 10
    assert gcd(10*2, 10) == 10

    assert gcd(983, 200) == 1
