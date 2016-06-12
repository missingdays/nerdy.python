
import random

def is_prime(n, test_number=100):
    """
    Uses Miller-Rabin test to check whether number n is prime.

    The idea is that if for some x < n
        x^2 = 1  mod n
    and 
        x != +-1 mod n
    then we can say that n is not prime.
    More information can be found at this article
    https://www.cs.cornell.edu/courses/cs4820/2010sp/handouts/MillerRabin.pdf 
    """

    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False

    s = 0
    t = n-1

    while t%2 == 0:
        s += 1
        t //= 2

    # Now n-1 = 2^s*t

    for _ in range(test_number):
        x = random.randrange(2, n)

        if is_composite(x, s, t, n):
            return False

    return True

def is_composite(x, s, t, n):
    # If Ferma's little theorem holds
    # then number is prime
    if pow(x, t, n) == 1:
        return False

    for i in range(s):
        if pow(x, 2**i*t, n) == n-1:
            return False
    return True
