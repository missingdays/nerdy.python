
import collections

from . import *

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

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(20) == 2432902008176640000

def test_factorization():
    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

    assert compare([2, 3], prime_factors(6))
    assert compare([2, 2], prime_factors(4))
    assert compare([2, 2, 2], prime_factors(8))
    assert compare([2, 3, 5, 7], prime_factors(210))
    assert compare([2, 5, 7], prime_factors(70))
    assert compare([11, 13], prime_factors(143))
    assert compare([31, 31], prime_factors(961))
    assert compare([523], prime_factors(523))
    assert compare([523, 523, 523, 523], prime_factors(74818113841))

def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    assert fibonacci(7) == 8
    assert fibonacci(8) == 13
    assert fibonacci(9) == 21
    assert fibonacci(10) == 34
