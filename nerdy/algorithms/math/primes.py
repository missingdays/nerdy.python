
import random

def is_prime(n):
    return is_prime_miller_rabin(n)

def is_prime_miller_rabin(n, test_number=100):
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

        if _is_composite(x, s, t, n):
            return False

    return True

def _is_composite(x, s, t, n):
    # If Ferma's little theorem holds
    # then n is prime
    if pow(x, t, n) == 1:
        return False

    for i in range(s):
        if pow(x, 2**i*t, n) == n-1:
            return False
    return True

def is_prime_linear_search(n):
    """
    Checks whether number is prime using simple linear search
    """

    # We need to check only first sqrt(n) numbers
    # Prove:
    #     Assume n divides some a > n/2. Than n divides n/a, that we will call b.
    #     Now lets assume that b is also > n/2.
    #     a > n/2
    #     b > n/2
    #     a*b > n
    #     So here we get contradiction. We know that a*b = n, but assuming that b > n/2 leads to a*b > n. So b can't be bigger that n/2, so 
    #     if n has divider bigger than n/2, it also has divider less than n/2.
    upper_bound = int(n**0.5)+ 1

    for divider in range(2, upper_bound):
        if n % divider == 0:
            return False
    
    return True

